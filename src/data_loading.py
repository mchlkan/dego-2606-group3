"""
data_loading.py — Data Loading Module

This module provides the standard data loading interface for the NovaCred
governance audit project. All analysis notebooks should use this module
to ensure consistent data access.

The loader reads the raw nested JSON dataset, flattens all nested structures
into a single flat DataFrame (one row per application), and pivots spending
behavior categories into individual columns. No data cleaning, type correction, 
deduplication, or imputation is performed at this stage.

Usage:
    from src.data_loading import load_raw_data

    df = load_raw_data("data/raw/raw_credit_applications.json")
"""

import json
import logging
import os
import pandas as pd

# configuring module-level logger to capture warnings about skipped records during flattening
logger = logging.getLogger(__name__)


def load_raw_data(path: str) -> pd.DataFrame:
    """
    Load and flatten the raw NovaCred credit applications dataset.

    Reads a nested JSON file containing credit application records and
    returns a flat pandas DataFrame with one row per application. Nested
    objects (applicant_info, financials, decision) are flattened into
    prefixed columns. The spending_behavior array is pivoted so that each
    spending category becomes its own column (e.g., spending_rent,
    spending_groceries).

    Parameters
    ----------
    path : str
        File path to the raw JSON dataset.

    Returns
    -------
    pd.DataFrame
        Flat DataFrame with one row per credit application.

    Raises
    ------
    FileNotFoundError
        If the specified file path does not exist.
    ValueError
        If the JSON file is empty, cannot be parsed, or does not contain
        a list of records.

    """

    # Validating file path before attempting to load
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Dataset not found at '{path}'. "
            f"Ensure the raw JSON file is placed in the data/raw/ directory."
        )

    # Loading JSON data with error handling for malformed JSON
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Failed to parse JSON file at '{path}'. "
            f"The file may be corrupted or not valid JSON. Details: {e}"
        )

    # Validating structure of loaded data
    if not isinstance(raw_data, list):
        raise ValueError(
            f"Expected a list of records but got {type(raw_data).__name__}. "
            f"The JSON file should contain an array of application objects."
        )

    if len(raw_data) == 0:
        raise ValueError("The JSON file contains an empty array — no records to load.")

    logger.info(f"Loaded {len(raw_data)} raw records from '{path}'.")

    # Flattening each record with error handling to skip malformed records
    flat_records = []

    for i, record in enumerate(raw_data):
        try:
            flat_row = _flatten_record(record)
            flat_records.append(flat_row)
        except Exception as e:
            logger.warning(
                f"Skipped record at index {i} (_id={record.get('_id', 'unknown')}): {e}"
            )

    if len(flat_records) == 0:
        raise ValueError("No records could be flattened. Check the dataset structure.")

    logger.info(
        f"Successfully flattened {len(flat_records)}/{len(raw_data)} records."
    )

    # Building DataFrame from the list of flat records
    df = pd.DataFrame(flat_records)

    return df


def _flatten_record(record: dict) -> dict:
    """
    Flatten a single nested application record into a flat dictionary.

    Extracts and prefixes fields from nested objects (applicant_info,
    financials, decision) and pivots the spending_behavior array into
    individual columns named as spending_<category>.

    Parameters
    ----------
    record : dict
        A single raw application record from the JSON dataset.

    Returns
    -------
    dict
        Flat dictionary representing one row of the output DataFrame.
    """

    flat = {}

    # Top-level fields
    flat["id"] = record.get("_id")
    flat["processing_timestamp"] = record.get("processing_timestamp")
    flat["loan_purpose"] = record.get("loan_purpose")
    flat["notes"] = record.get("notes")

    # Applicant info (nested object)
    applicant = record.get("applicant_info", {})
    flat["full_name"] = applicant.get("full_name")
    flat["email"] = applicant.get("email")
    flat["ssn"] = applicant.get("ssn")
    flat["ip_address"] = applicant.get("ip_address")
    flat["gender"] = applicant.get("gender")
    flat["date_of_birth"] = applicant.get("date_of_birth")
    flat["zip_code"] = applicant.get("zip_code")

    # Financials (nested object)
    financials = record.get("financials", {})
    flat["annual_income"] = financials.get("annual_income")
    flat["credit_history_months"] = financials.get("credit_history_months")
    flat["debt_to_income"] = financials.get("debt_to_income")
    flat["savings_balance"] = financials.get("savings_balance")

    # Spending behavior (array of objects → pivoted columns)
    # Each category becomes its own column: spending_<category_name>
    spending = record.get("spending_behavior", [])
    if isinstance(spending, list):
        for entry in spending:
            if isinstance(entry, dict) and "category" in entry:
                col_name = "spending_" + entry["category"].lower().replace(" ", "_")
                flat[col_name] = entry.get("amount")

    # Decision (nested object)
    decision = record.get("decision", {})
    flat["loan_approved"] = decision.get("loan_approved")
    flat["interest_rate"] = decision.get("interest_rate")
    flat["approved_amount"] = decision.get("approved_amount")
    flat["rejection_reason"] = decision.get("rejection_reason")

    return flat