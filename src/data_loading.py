"""
data_loading.py — Canonical Data Loading Module

This module provides the standard data loading interface for the NovaCred
governance audit project. All analysis notebooks should use this module
to ensure consistent data access across the project.

The loader reads the raw nested JSON dataset, flattens all nested structures
into a single flat DataFrame (one row per application), and pivots spending
behavior categories into individual columns. No data cleaning, type correction,
or imputation is performed — the output reflects the raw data as-is to preserve
auditability.

Usage:
    from src.data_loading import load_raw_data

    df = load_raw_data("data/raw/raw_credit_applications.json")
"""

import json
import logging
import os

import pandas as pd

# Configure module-level logger
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

    No data cleaning, type correction, deduplication, or imputation is
    applied. The output preserves the raw data as-is for audit purposes.

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

    Examples
    --------
    >>> from src.data_loading import load_raw_data
    >>> df = load_raw_data("data/raw/raw_credit_applications.json")
    >>> df.shape
    (502, ...)
    """

    # --- Validate file path ---
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Dataset not found at '{path}'. "
            f"Ensure the raw JSON file is placed in the data/raw/ directory."
        )

    # --- Load JSON ---
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Failed to parse JSON file at '{path}'. "
            f"The file may be corrupted or not valid JSON. Details: {e}"
        )

    # --- Validate structure ---
    if not isinstance(raw_data, list):
        raise ValueError(
            f"Expected a list of records but got {type(raw_data).__name__}. "
            f"The JSON file should contain an array of application objects."
        )

    if len(raw_data) == 0:
        raise ValueError("The JSON file contains an empty array — no records to load.")

    logger.info(f"Loaded {len(raw_data)} raw records from '{path}'.")

    # --- Flatten each record ---
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

    # --- Build DataFrame ---
    df = pd.DataFrame(flat_records)

    return df


def _flatten_record(record: dict) -> dict:
    """
    Flatten a single nested application record into a flat dictionary.

    Extracts all keys from nested objects (applicant_info, financials,
    decision) to capture both documented and undocumented fields. The
    spending_behavior array is pivoted into individual columns named as
    spending_<category>.

    This approach ensures that schema inconsistencies (e.g., annual_salary
    appearing instead of annual_income) are preserved in the output rather
    than silently dropped.

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

    # --- Top-level fields ---
    flat["id"] = record.get("_id")
    flat["processing_timestamp"] = record.get("processing_timestamp")
    flat["loan_purpose"] = record.get("loan_purpose")
    flat["notes"] = record.get("notes")

    # --- Applicant info (nested object) ---
    # All keys are extracted to capture any undocumented fields
    applicant = record.get("applicant_info", {})
    if isinstance(applicant, dict):
        for key, value in applicant.items():
            flat[key] = value

    # --- Financials (nested object) ---
    # All keys are extracted to capture any undocumented fields
    # (e.g., annual_salary appearing instead of annual_income in some records)
    financials = record.get("financials", {})
    if isinstance(financials, dict):
        for key, value in financials.items():
            flat[key] = value

    # --- Spending behavior (array of objects → pivoted columns) ---
    # Each category becomes its own column: spending_<category_name>
    # Categories are lowercased and spaces replaced with underscores
    spending = record.get("spending_behavior", [])
    if isinstance(spending, list):
        for entry in spending:
            if isinstance(entry, dict) and "category" in entry:
                col_name = "spending_" + entry["category"].lower().replace(" ", "_")
                flat[col_name] = entry.get("amount")

    # --- Decision (nested object) ---
    # All keys are extracted to capture any undocumented fields
    decision = record.get("decision", {})
    if isinstance(decision, dict):
        for key, value in decision.items():
            flat[key] = value

    return flat