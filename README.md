# NovaCred Model Governance and Data Audit (DEGO Group Project - Group 3)

**Group 3 | DEGO 2606 Group Project – Credit Application Governance Analysis (NovaCred)**

# Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Team and Roles](#2-team-and-roles)
3. [Project Overview](#3-project-overview)
   - 3.1 [Objective](#31-objective)
   - 3.2 [Scope](#32-scope)
   - 3.3 [Dataset Description](#33-dataset-description)
4. [Repository Structure](#4-repository-structure)
5. [Governance and Reproducibility](#5-governance-and-reproducibility)
   - 5.1 [Version Control and Collaboration](#51-version-control-and-collaboration)
   - 5.2 [Reproducibility Instructions](#52-reproducibility-instructions)
   - 5.3 [Data Pipeline](#53-data-pipeline)
6. [Data Quality Audit](#6-data-quality-audit)
   - 6.1 [Methodology](#61-methodology)
   - 6.2 [Completeness](#62-completeness)
   - 6.3 [Consistency](#63-consistency)
   - 6.4 [Validity](#64-validity)
   - 6.5 [Accuracy](#65-accuracy)
   - 6.6 [Consolidated Risk Summary](#66-consolidated-risk-summary)
   - 6.7 [Remediation Applied](#67-remediation-applied)
7. [Bias and Fairness Analysis](#7-bias-and-fairness-analysis)
   - 7.1 [Methodology](#71-methodology)
   - 7.2 [Gender Bias Analysis](#72-gender-bias-analysis)
   - 7.3 [Age Bias Analysis](#73-age-bias-analysis)
   - 7.4 [Proxy Discrimination and Intersectional Effects](#74-proxy-discrimination-and-intersectional-effects)
   - 7.5 [Consolidated Fairness Summary](#75-consolidated-fairness-summary)
   - 7.6 [Remediation Applied](#76-remediation-applied)
8. [Privacy and Governance](#8-privacy-and-governance)
   - 8.1 [Methodology](#81-methodology)
   - 8.2 [PII Identification and Classification](#82-pii-identification-and-classification)
   - 8.3 [Pseudonymisation Demonstration](#83-pseudonymisation-demonstration)
   - 8.4 [Re-identification Risk](#84-re-identification-risk)
   - 8.5 [GDPR Compliance Assessment](#85-gdpr-compliance-assessment)
   - 8.6 [EU AI Act High-Risk Classification](#86-eu-ai-act-high-risk-classification)
   - 8.7 [Consolidated Risk Summary](#87-consolidated-risk-summary)
   - 8.8 [Remediation Applied](#88-remediation-applied)
9. [Recommendations](#9-recommendations)
   - 9.1 [Data Quality Controls](#91-data-quality-controls)
   - 9.2 [Bias Mitigation Measures](#92-bias-mitigation-measures)
   - 9.3 [Privacy Safeguards](#93-privacy-safeguards)
   - 9.4 [Governance Framework](#94-governance-framework)
10. [Conclusion](#10-conclusion)
11. [Contributions](#11-contributions)

---

## 1. Executive Summary

NovaCred's automated credit decisioning system presents material governance risks across data quality, fairness, and privacy that require immediate remediation before continued operation. This audit assessed 502 raw credit application records across three dimensions and identified systemic failures in data controls, direct evidence of discriminatory decisioning, and critical gaps in privacy and regulatory compliance.

The data quality assessment identified 16 distinct issues across completeness, consistency, validity, and accuracy. The most consequential findings are structural rather than isolated errors: 87.6% of records lack a processing timestamp, eliminating the audit trail needed to investigate complaints or demonstrate regulatory compliance. Two duplicated application IDs undermine primary key integrity. Five records store income under an undocumented field name, and three of those records were approved for loans between 45,000 and 63,000 without the canonical income field populated, indicating that the approval pipeline does not enforce basic input validation before making legally significant credit decisions. Overall dataset risk is assessed as Moderate-High. All issues were remediated programmatically, producing a cleaned 500-record dataset for downstream analysis.

The bias analysis reveals a four-fifths rule violation in loan approvals by gender (Disparate Impact ratio = 0.77). This alone would warrant investigation, but the critical finding is the conditional result: after controlling for annual income, debt-to-income ratio, credit history, savings balance, and age, male applicants remain nearly twice as likely to be approved as female applicants with identical financial profiles (OR = 1.98, p = 0.0004). This is not explainable by legitimate credit risk differences and constitutes direct evidence of discriminatory decisioning. The aggregate gender disparity masks worse outcomes at the subgroup level, with female applicants aged 26-35 facing the most severe disadvantage (DI = 0.620). ZIP code is near-perfectly collinear with gender (chi-square = 324.67, p < 0.001), creating a structural proxy discrimination risk in any future model iteration even though it does not independently predict approval in the current data. No pricing discrimination was detected in interest rates. Overall bias and fairness risk is assessed as High.

The privacy and governance audit identifies critical gaps in data protection, decision transparency, and regulatory readiness. Direct identifiers (full name, email, SSN, IP address) remain in the analytical dataset at 98-100% coverage with no pseudonymisation applied at ingestion, meaning any unauthorized access would expose identifiable applicant records. Of 208 rejected applications, 169 (81.2%) cite only algorithm_risk_score as the rejection reason, which provides no actionable basis for an applicant to understand or contest the decision. This undermines the Art. 22 safeguards required for automated decisions with legal effects. The system qualifies as high-risk under EU AI Act Annex III, point 5(b), but six of seven mandatory governance obligations under Art. 9-15 are not evidenced in repository artifacts. No lawful basis documentation, consent tracking, retention enforcement, or human oversight workflow exists at the dataset or repository level. Even after removing direct identifiers, the dataset remains highly re-identifiable through financial attribute combinations alone (k = 1 for multiple quasi-identifier sets). Overall privacy and governance risk is assessed as Critical.

Taken together, these findings indicate that NovaCred is operating a discriminatory, poorly documented, and insufficiently governed credit decisioning system that processes identifiable personal data without adequate technical or organisational safeguards. The 30 recommendations in Section 9 are organized across data quality controls, bias mitigation measures, privacy safeguards, and a cross-cutting governance framework. The highest priority actions are to suspend automated approvals pending a root-cause model audit, enforce privacy by default at the dataset layer, replace opaque rejection reasons with a controlled taxonomy, and initiate a Data Protection Impact Assessment under GDPR Art. 35 before any further deployment.

---

## 2. Team and Roles

**Team Lead — Michael Kania**  
Email: 72782@novasbe.pt

**Data Engineer - Dominik Hohlenstein**  
Email: 70135@novasbe.pt

**Data Scientist — Niklas Klaus Jürgen Düttmann**  
Email: 71916@novasbe.pt

**Governance Officer — Mohamed Aannaque**  
Email: 71359@novasbe.pt

## 3. Project Overview

### 3.1 Objective

The objective of this project is to conduct a comprehensive governance audit of NovaCred's credit approval dataset and automated decision pipeline.

The audit focuses on three core areas:

1. **Data Quality**: Identify completeness, consistency, validity, and accuracy issues and assess their impact on model reliability.
2. **Bias and Fairness**: Evaluate whether model outcomes exhibit disparate impact across protected groups, including gender and age, and investigate proxy discrimination.
3. **Privacy and Governance**: Identify personally identifiable information (PII), assess GDPR compliance risks, evaluate EU AI Act implications, and propose actionable governance controls.

The goal is to identify, quantify, and document governance risks and propose concrete mitigation measures. This project does not modify the production model but evaluates the risks present in the supporting data and decision pipeline.

### 3.2 Scope

This project evaluates NovaCred's historical credit application dataset used to support automated credit approval decisions.

The audit includes:

- Assessment of data completeness, consistency, validity, and accuracy
- Detection of potential disparate impact across demographic groups
- Analysis of proxy variables that may correlate with protected attributes
- Identification of personal data and regulatory compliance risks under GDPR
- Evaluation of the system's risk classification under the EU AI Act
- Assessment of governance, auditability, and human oversight practices

### 3.3 Dataset Description

The dataset consists of historical credit application records used by NovaCred’s automated loan decision system. Each record represents one loan application and is stored in a nested JSON structure containing applicant information, financial attributes, behavioral data, and the corresponding decision outcome.

The dataset is organized into the following main components:

| Component | Field | Type | Description |
|-----------|-------|------|-------------|
| **Identifier** | `_id` | String | Unique application identifier (e.g., `app_001`) |
| **Applicant Information** | `applicant_info` | Nested object | Personal and demographic data |
| | `.full_name` | String | Applicant full name |
| | `.email` | String | Email address |
| | `.ssn` | String | Social Security Number |
| | `.ip_address` | String | IP address at time of application |
| | `.gender` | String | Gender |
| | `.date_of_birth` | String | Date of birth |
| | `.zip_code` | String | ZIP / postal code |
| **Financial Information** | `financials` | Nested object | Financial attributes for creditworthiness assessment |
| | `.annual_income` | Number | Annual income |
| | `.credit_history_months` | Integer | Months of credit history |
| | `.debt_to_income` | Number | Debt-to-income ratio |
| | `.savings_balance` | Number | Current savings balance |
| **Behavioral Information** | `spending_behavior` | Array of objects | Categorized monthly spending data |
| | `[].category` | String | Spending category |
| | `[].amount` | Number | Monthly spending amount |
| **Decision Outcome** | `decision` | Nested object | Automated loan decision and parameters |
| | `.loan_approved` | Boolean | Approval outcome (`true` / `false`) |
| | `.interest_rate` | Number | Assigned interest rate (if approved) |
| | `.approved_amount` | Number | Approved loan amount (if approved) |
| | `.rejection_reason` | String | Reason for denial (if rejected) |


Due to its nested structure, the dataset requires preprocessing and flattening before analysis. The presence of personal, demographic, and financial attributes makes it suitable for assessing data quality, fairness risks, and governance considerations in automated credit decision systems.

## 4. Repository Structure

```
project-root/
│
├── data/
│   ├── raw/              # Raw dataset (excluded from Git; contains PII)
│   └── processed/        # Cleaned and processed analysis datasets
│
├── notebooks/
│   ├── 01-data-quality.ipynb
│   ├── 02-bias-analysis.ipynb
│   └── 03-privacy-demo.ipynb
│
├── src/                  # Reusable data loading and processing code
│
├── docs/                 # Workflow and project planning documentation
│
├── presentation/         # Video presentation file or link
│
├── reports/              # Reports & charts
│   └── figures
│
├── environment.yml       # Conda environment specification
├── requirements.txt      # Python dependencies
├── .gitignore            # Excludes raw data and sensitive files
└── README.md             # Project audit report (this document)
```

## 5. Governance and Reproducibility

### 5.1 Version Control and Collaboration

This project follows auditable development practices aligned with model governance principles.

The repository uses protected branch rules on GitHub:

- Direct pushes to `main` are blocked
- All changes are submitted via feature branches and Pull Requests
- Pull Requests require peer review before merging
- Force pushes and branch deletion on `main` are disabled

This ensures traceability, accountability, and controlled change management throughout the project lifecycle.

### 5.2 Reproducibility Instructions

To reproduce the analysis:

1. Create the conda environment using:
```
   conda env create -f environment.yml
   conda activate dego-group
```

2. Place the raw dataset in:
```
   data/raw/
```

3. Run the analysis notebooks in the following order:
```
   notebooks/01-data-quality.ipynb
   notebooks/02-bias-analysis.ipynb
   notebooks/03-privacy-demo.ipynb
```
### 5.3 Data Pipeline

The three analysis notebooks form a sequential pipeline where each notebook consumes the output of the previous one. No notebook modifies its input file; each produces a new dataset with progressively reduced exposure.

| Step | Notebook | Input | Key actions | Output |
|---|---|---|---|---|
| 1 | `01-data-quality.ipynb` | `raw_credit_applications.json` (502 records) | Deduplication, empty string normalization, income reconciliation, gender standardization, type casting, flagging of implausible values | `cleaned_credit_applications.parquet` (500 records) |
| 2 | `02-bias-analysis.ipynb` | Cleaned parquet (500 records) | Bias analysis, then removal of protected attributes (`gender`, `date_of_birth`, `age`) and proxy variable (`zip_code`) | `bias_remediated_credit_applications.parquet` (500 records) |
| 3 | `03-privacy-demo.ipynb` | Bias-remediated parquet (500 records) | Privacy audit, then removal of direct identifiers (`full_name`, `email`, `ssn`, `ip_address`) and sensitive spending fields (`alcohol`, `gambling`, `adult_entertainment`) | `remediated_credit_applications.parquet` (500 records) |

The raw dataset is excluded from version control via `.gitignore` because it contains unprotected PII. All processed outputs are stored in `data/processed/`.

## 6. Data Quality Audit

The data quality assessment evaluates the dataset across four dimensions: completeness, consistency, validity, and accuracy. Each issue is quantified and classified by severity (Low, Moderate, High, Critical) based on its potential impact on decision integrity, model reliability, and auditability. Full technical details, code, and per-record analysis are available in `notebooks/01-data-quality.ipynb`.

### 6.1 Methodology

The data quality assessment was conducted on the raw dataset of 502 credit application records prior to any cleaning or deduplication. Each record was loaded and flattened from nested JSON using the canonical loader in `src/data_loading.py`, which dynamically extracts all keys from the `applicant_info`, `financials`, and `decision` objects, pivots the `spending_behavior` array into per-category columns, and captures undocumented top-level fields (`processing_timestamp`, `loan_purpose`, `notes`). No cleaning or type correction is applied at load time, preserving the raw state for audit.

Issues are evaluated across four standard data quality dimensions: completeness (whether expected values are present), consistency (whether representations and constraints are uniform), validity (whether values fall within defined domains), and accuracy (whether values are plausible given domain context and cross-field relationships). Each finding is quantified with affected record counts and percentages, and classified using a four-level severity scale: Low, Moderate, High, or Critical. Hybrid ratings (Moderate-High) are used where a finding falls between levels.

All remediation is applied programmatically and documented in the notebook. The cleaned dataset is exported to `data/processed/cleaned_credit_applications.parquet` (500 records after deduplication) and serves as input for all downstream analyses.

### 6.2 Completeness

Decision-critical financial fields are nearly complete: `debt_to_income`, `credit_history_months`, and `savings_balance` are fully populated across all 502 records. `annual_income` is missing for 5 records (1.0%), but investigation revealed that these 5 records contain an undocumented `annual_salary` field instead indicating a schema inconsistency in the data collection pipeline rather than true data loss. No record is missing income information entirely.

The dataset also contains empty strings in several string-type fields that are not detected by standard null checks. After normalization, effective missingness is: `email` — 7 records (1.4%), `date_of_birth` — 5 records (1.0%), `gender` — 3 records (0.6%), and `zip_code` — 2 records (0.4%). Identity fields `ssn` and `ip_address` are each missing for 5 records (1.0%).

Conditional completeness checks on decision outcome fields revealed zero violations: all approved records contain `interest_rate` and `approved_amount`, and all rejected records contain a `rejection_reason`. This indicates well-structured data capture logic in the core credit workflow.

Among metadata fields, `processing_timestamp` is present in only 62 of 502 records (12.4%) and `loan_purpose` in only 50 records (10.0%). These structural gaps weaken the audit trail and reduce interpretability of decisions.

Spending behavior data is sparse at the per-category level (84–99% missing per category), but this reflects the data collection design, where each applicant reports 1–4 spending categories out of 15 available. All 502 records contain at least some spending data. A co-occurrence analysis identified 5 records with 3 or more missing critical fields simultaneously, suggesting systematic data collection failures for specific applicants.

| Finding | Evidence | Severity |
|---------|----------|----------|
| Schema inconsistency: `annual_income` vs `annual_salary` | 5 records (1.0%) | Moderate |
| Empty strings masking true missingness | 14 affected values across 4 fields | High |
| Missing `processing_timestamp` | 440 records (87.6%) | High |
| Missing `loan_purpose` | 452 records (90.0%) | Moderate |
| Clustered missingness (3+ critical fields) | 5 records (1.0%) | High |
| Missing `ssn` and `ip_address` | 5 records each (1.0%) | Moderate |
| Sparse spending categories | 84–99% per category (by design) | Low |

**Overall completeness risk: Moderate.** Core decision fields are nearly complete with consistent conditional logic. Primary risks arise from empty strings masking missingness, the schema split in income fields, and structural gaps in metadata.

### 6.3 Consistency

Two application IDs are duplicated, affecting 4 records in total. One pair (`app_042`) is flagged as a resubmission; the other (`app_001`) is flagged as a system-generated duplicate entry error, with the second record missing most identity fields. No full row-level duplicates were detected. Primary key violations of this kind undermine traceability, audit reliability, and the integrity of any downstream joins or aggregations.

The `gender` field uses four distinct encodings for two logical categories: `Male` (195), `Female` (193), `M` (53), and `F` (58), alongside 3 missing values. This inconsistency affects 111 records (22.1%) and would distort any grouping or aggregation used in bias analysis if left unstandardized.

The `date_of_birth` field contains three coexisting date formats across 497 non-null records: `YYYY-MM-DD` (340 records, 68.4%), `DD/MM/YYYY` (101 records, 20.3%), and `YYYY/MM/DD` (56 records, 11.3%). While all values are parseable, mixed formats increase the risk of silent parsing errors for ambiguous dates where day and month values are both ≤ 12.

The `annual_income` field contains mixed Python types within a single column: 488 integer values, 8 string values, and 1 float value. All string values are numerically parseable, but heterogeneous storage can cause implicit casting failures, aggregation instability, or silent exclusion from numeric operations.

| Finding | Evidence | Severity |
|---------|----------|----------|
| Duplicate application IDs | 2 IDs affecting 4 records (0.8%) | High |
| Inconsistent gender encoding | 111 records using M/F instead of Male/Female (22.1%) | Moderate |
| Inconsistent date formats in `date_of_birth` | 3 coexisting formats across 497 records | Moderate |
| Mixed Python types in `annual_income` | 488 int, 8 str, 1 float | Moderate |

**Overall consistency risk: Moderate.** Primary key duplication is the highest-severity finding. Representation-level inconsistencies in categorical encoding, date formats, and income data types introduce moderate analytical risk that is addressable through deterministic ingestion controls.

### 6.4 Validity

One record reports a `debt_to_income` ratio of 1.85, exceeding the valid domain constraint of [0, 1]. The affected application was approved with an `approved_amount` of 17,000 and an `interest_rate` of 3.2%, indicating that domain validation was not enforced prior to the approval decision.

Two records contain negative `credit_history_months` values (−10 and −3), which are logically impossible. One record contains a negative `savings_balance` of −5,000, which may indicate a data entry error or an undocumented overdraft representation.

One email address is syntactically invalid (missing the `@` symbol). No SSN format violations or invalid ZIP codes were detected after empty string normalization. No negative values were found in `annual_income`, `interest_rate`, or any spending category, and no extreme spending values (> 1,000,000) were observed.

Two of eight assessed fields have mismatched data types: `processing_timestamp` is stored as a string instead of datetime, and `annual_income` is stored as object instead of float. The remaining fields match their expected domain types.

| Finding | Evidence | Severity |
|---------|----------|----------|
| DTI outside valid domain [0, 1] | 1 record (0.2%) — approved application | Moderate |
| Negative `credit_history_months` | 2 records (0.4%) — minimum value of −10 | Moderate |
| Negative `savings_balance` | 1 record (0.2%) — value of −5,000 | Moderate |
| Invalid email format | 1 record (0.2%) — missing `@` symbol | Low–Moderate |
| Data type mismatches | 2 of 8 fields (`processing_timestamp`, `annual_income`) | Moderate |

**Overall validity risk: Moderate.** Violations are limited in frequency, but the DTI domain breach in an approved application and negative values in decision-critical fields indicate systematic gaps in ingestion-level validation.

### 6.5 Accuracy

All applicant ages fall within the plausible range of 18–100 years. No demographic accuracy concerns were identified.

When annualizing monthly spending (×12) for a like-for-like comparison with annual income, 1 record shows annualized spending exceeding reported income. The affected applicant reports an `annual_income` of 0 with positive spending, suggesting either a data entry error or a failure to distinguish between true zero income and missing income.

Three approved loans have null `annual_income` at the point of decision, with approved amounts between 45,000 and 63,000. All three correspond to the records where income was recorded under the undocumented `annual_salary` field (identified in Section 6.1). After reconciliation, these records do contain valid income values (45,000–75,000). The underlying data is not missing, but the approval pipeline processed these applications without the standard income field being populated — indicating a control gap in the decision workflow rather than a data loss.

All interest rates fall within the plausible range of 0–25%. No pricing anomalies were detected.

| Finding | Evidence | Severity |
|---------|----------|----------|
| Annualized spending exceeds reported income | 1 record — income = 0, annualized spending ≈ 16,668 | High |
| Approved loans with missing canonical income field | 3 records — income present in `annual_salary` but not `annual_income` | High |
| Age outside plausible range | 0 records | Low |
| Interest rate outside plausible range | 0 records | Low |

**Overall accuracy risk: Moderate–High.** Demographic and pricing variables are stable, but loan approvals without documented income in the canonical field and a spending-income contradiction represent material plausibility breaches in the decision logic.

### 6.6 Summary of Issues and Impact

The assessment identified 16 distinct data quality issues across all four dimensions. The consolidated risk profile is as follows:

| # | Dimension | Finding | Evidence | Severity |
|---|---|---|---|---|
| 1 | Completeness | Schema inconsistency: `annual_income` vs `annual_salary` | 5 records (1.0%) | Moderate |
| 2 | Completeness | Empty strings masking true missingness | 14 affected values across 4 fields | High |
| 3 | Completeness | Missing `processing_timestamp` | 440 of 502 records (87.6%) | High |
| 4 | Completeness | Missing `loan_purpose` | 452 of 502 records (90.0%) | Moderate |
| 5 | Completeness | Clustered missingness (3+ critical fields) | 5 records (1.0%) | High |
| 6 | Completeness | Missing `ssn` and `ip_address` | 5 records each (1.0%) | Moderate |
| 7 | Completeness | Sparse spending categories | 84-99% missing per category (by design) | Low |
| 8 | Consistency | Duplicate application IDs | 2 IDs affecting 4 records (0.8%) | High |
| 9 | Consistency | Inconsistent gender encoding | 111 records using M/F instead of Male/Female (22.1%) | Moderate |
| 10 | Consistency | Inconsistent date formats in `date_of_birth` | 3 coexisting formats across 497 records | Moderate |
| 11 | Consistency | Mixed Python types in `annual_income` | 488 int, 8 str, 1 float | Moderate |
| 12 | Validity | DTI outside valid domain [0, 1] | 1 record (0.2%), approved application | Moderate |
| 13 | Validity | Negative `credit_history_months` | 2 records (0.4%), minimum value of -10 | Moderate |
| 14 | Validity | Negative `savings_balance` | 1 record (0.2%), value of -5,000 | Moderate |
| 15 | Validity | Invalid email format | 1 record (0.2%), missing @ symbol | Low-Moderate |
| 16 | Accuracy | Annualized spending exceeds reported income | 1 record, income = 0, annualized spending of approximately 16,668 | High |

**Note**: Data type mismatches identified in Section 6.4 (`processing_timestamp` stored as string, `annual_income` stored as object) are consequences of issues #3 and #11 respectively and are not counted as separate findings.

**Overall dataset risk: Moderate–High.** 

### 6.7 Remediation Applied

All 16 issues were remediated programmatically in `notebooks/01-data-quality.ipynb`. The following actions were applied: Income fields `annual_income` and `annual_salary` were reconciled into a unified canonical field (5 records), empty strings were normalized to NaN across 4 fields (14 values), `gender` encoding was standardized from M/F to Male/Female (111 records), `date_of_birth` was parsed to ISO 8601 datetime across all three formats (497 records), `annual_income` was cast to numeric (9 records), and duplicate application IDs were resolved by retaining the most complete record (2 duplicates removed, reducing the dataset from 502 to 500 records). Logically impossible values were set to NaN: negative `credit_history_months` (2 records), negative `savings_balance` (1 record), invalid email (1 record), and zero income (1 record). Records with 3 or more missing critical fields (5 records), approved loans with missing canonical income (3 records), and DTI outside the valid domain (1 record) were flagged for manual review but not excluded. The processing_timestamp field was cast to datetime for the 62 records where it is present. The cleaned dataset is exported to `data/processed/cleaned_credit_applications.parquet` (500 records) and serves as input for Notebook 02.

*All analysis is documented and reproducible in `notebooks/01-data-quality.ipynb`.*

## 7. Bias and Fairness Analysis

### 7.1 Methodology

The bias analysis was conducted on 500 records after deduplication. Prior to any group-level computation, three pre-processing steps were applied: (1) inconsistent gender encoding was normalised (`M` → `Male`, `F` → `Female`, blank → `NaN`), (2) date of birth was parsed across three mixed formats (`YYYY-MM-DD`, `DD/MM/YYYY`, `YYYY/MM/DD`) to derive applicant age, and (3) one negative `credit_history_months` value was set to `NaN`.

The analysis covers four dimensions: selection rate fairness (Disparate Impact ratio), statistical significance of group differences (chi-square, Kruskal-Wallis, Welch's t-test), proxy discrimination (ZIP code, spending behaviour), and intersectional effects (gender × age group). Fairlearn's `demographic_parity_difference` was used as a standardised cross-validation metric.

### 7.2 Gender Bias Analysis

The overall loan approval rate across the dataset is **58.4%**. Broken down by gender, a substantial gap emerges:

| Gender | Approved | Total | Approval Rate |
|---|---|---|---|
| Male | 163 | 247 | **66.0%** |
| Female | 127 | 251 | **50.6%** |

**Disparate Impact ratio:** `50.6% / 66.0% = 0.7668`

The four-fifths (80%) rule classifies any DI ratio below 0.80 as indicative of potential disparate impact. At 0.77, NovaCred's historical approval data constitutes a formal four-fifths rule violation. A chi-square test of independence confirms that this gap is not attributable to chance: **χ²(1) = 11.51, p = 0.0007**, making the association between gender and approval outcome highly statistically significant.

**Conditional fairness test (Critical finding):** A logistic regression of `loan_approved` on gender plus all financial controls (annual income, debt-to-income ratio, credit history, savings balance, and age) was conducted on 488 records with complete data. After holding every financial risk variable constant, being male remains a **highly significant positive predictor of approval**: OR = **1.98** (95% CI: 1.36–2.89), Wald z = 3.56, **p = 0.0004**. Male applicants with identical financial profiles are nearly twice as likely to be approved as comparable female applicants. This result constitutes direct evidence of discriminatory decisioning that cannot be attributed to legitimate credit-risk differences, triggering mandatory action under GDPR Article 22 and EU AI Act Annex III.

**Interest rate pricing:** Among approved applicants, males received a mean rate of **4.63%** and females **4.49%** — a gap of +0.14 pp. A Welch's t-test yields p = 0.313 (not significant). A conditional OLS regression after financial controls finds β = +0.15 pp (p = 0.288) — also not significant. No pricing discrimination is evidenced. The bias is confined to the approval decision, not the pricing of approved loans.

### 7.3 Age Bias Analysis

Applicant age was derived from the `date_of_birth` field after mixed-format parsing (fixed reference date: 2025-12-31). Applicants were grouped into five standard age bands:

| Age Group | Approved | Total | Approval Rate |
|---|---|---|---|
| 18–25 | 10 | 23 | **43.5%** |
| 26–35 | 78 | 161 | **48.5%** |
| 36–50 | 149 | 221 | **67.4%** |
| 51–65 | 48 | 83 | 57.8% |
| 66+ | 4 | 8 | 50.0% |

Applicants under 35 are approved at approximately 44–48% — roughly 19–24 percentage points below the peak group (36–50 at 67.4%). A Kruskal-Wallis test across all five age groups yields H = 16.27, **p = 0.0027**, confirming statistically significant differences not attributable to random variation.

**Conditional fairness test:** A logistic regression of `loan_approved` on age plus all financial controls finds that age is **not independently predictive** after controls (OR = 1.00 per additional year, z = −0.36, **p = 0.720**). The observed age disparities appear to be attributable to correlated differences in financial risk profiles — e.g., younger applicants tend to have shorter credit histories — rather than direct age discrimination. Severity remains Moderate; intersectional and non-linear age effects are examined in Section 7.4 below.

### 7.4 Proxy Discrimination and Intersectional Effects

**ZIP Code — Data Minimisation Violation (High)**

ZIP codes in the dataset cluster into two geographic areas: NYC (prefix `10xxx`) and LA (prefix `90xxx`). The demographic composition is near-perfectly segregated by gender:

| Region | Approval Rate | Male Share | Female Share |
|---|---|---|---|
| NYC (10xxx) | **64.5%** (n=251) | **88.8%** | 11.2% |
| LA (90xxx) | 51.7% (n=230) | 6.5% | **93.5%** |

The chi-square test on the gender × region contingency table is overwhelmingly significant: **χ²(2) = 324.67, p < 0.001** — confirming that ZIP code and gender are nearly collinear in this dataset (Condition 1 met). However, a conditional logistic regression including gender and all financial controls finds that ZIP code does **not independently predict approval** after those controls (region_nyc OR = 1.14, z = 0.43, **p = 0.67**). Active proxy discrimination is not confirmed (Condition 2 not met). The 12.8 pp regional approval gap is fully explained by the underlying gender composition.

Despite the negative Condition 2 result, ZIP code must be removed from all model inputs: retaining a feature with this level of demographic collinearity violates GDPR Article 5(1)(c) (data minimisation) and creates a structural risk of encoding gender discrimination in any future model iteration.

**Sensitive Spending Categories — GDPR Art. 9 Concern (Moderate)**

The dataset contains `spending_adult_entertainment`, `spending_gambling`, and `spending_alcohol`. No spending category shows a statistically significant gender difference (no feature passed the Condition 1 Welch t-test at α = 0.05; smallest p-value: 0.077 for `spending_transportation`). Sample sizes for the three sensitive categories are too small for reliable testing (gambling: 0M/6F; adult entertainment: 4M/1F). Proxy discrimination via spending behaviour is not confirmed.

The data governance concern is independent of the proxy test: collecting lifestyle behavioural data without a demonstrated credit-relevance justification and an established lawful basis violates GDPR Article 9 and Article 5(1)(c). These categories require immediate DPO review.

**Intersectional Effects — Gender × Age (High)**

Single-attribute analysis understates the severity of compounded disadvantage. Computing the Disparate Impact ratio within each age band reveals three subgroup violations:

| Age Group | Female Rate | Male Rate | DI Ratio | Violation |
|---|---|---|---|---|
| 18–25 | 38.5% (n=13) | 50.0% (n=10) | 0.769 | **Yes** |
| 26–35 | 37.4% (n=83) | 60.3% (n=78) | **0.620** | **Yes — worst** |
| 36–50 | 62.9% (n=105) | 71.6% (n=116) | 0.879 | No |
| 51–65 | 50.0% (n=44) | 65.8% (n=38) | 0.760 | **Yes** |
| 66+ | 50.0% (n=4) | 50.0% (n=4) | 1.000 | No (n too small) |

Female applicants aged 26–35 face the most severe disadvantage in the entire audit (DI = 0.620). The overall gender DI of 0.77 masks three subgroup violations invisible at the aggregate level. EU AI Act Annex III requires subgroup-level fairness reporting for high-risk credit scoring systems.

### 7.5 Consolidated Fairness Summary

| Finding | Metric | Value | Threshold | Status |
|---|---|---|---|---|
| Gender Disparate Impact ratio | DI = female rate / male rate | **0.7668** | < 0.80 = violation | **VIOLATION** |
| Gender bias significance (descriptive) | Chi-square p-value | **0.0007** | < 0.05 = significant | **SIGNIFICANT** |
| Gender bias — conditional logistic | OR for gender after financial controls | **OR = 1.98, p = 0.0004** | p < 0.05 = Critical | **CRITICAL — discriminatory decisioning confirmed** |
| Age group bias significance (descriptive) | Kruskal-Wallis p-value | **0.0027** | < 0.05 = significant | **SIGNIFICANT** |
| Age — conditional logistic | OR for age after financial controls | OR = 1.00, p = 0.720 | p < 0.05 | Not significant — Moderate |
| Interest rate pricing by gender (descriptive) | Welch t-test p-value | 0.313 | < 0.05 = significant | No bias detected |
| Interest rate pricing by gender (conditional) | OLS β after financial controls | β = +0.15 pp, p = 0.288 | p < 0.05 | No bias detected |
| Demographic Parity Difference (gender) | DPD (Fairlearn) | **0.1539** | > 0.10 = concern | **CONCERN** |
| Demographic Parity Difference (age group) | DPD (Fairlearn) | **0.2394** | > 0.10 = concern | **CONCERN** |
| ZIP code — gender collinearity | Chi-square p-value | **p < 0.001** (χ²=324.67) | — | **Data minimisation violation** |
| ZIP code — approval prediction (conditional) | OR after gender + financial controls | OR = 1.14, p = 0.666 | p < 0.05 | Proxy not confirmed |
| Female 26–35 intersectional DI | DI ratio within age band | **0.620** | < 0.80 = violation | **VIOLATION** |
| Female 18–25 intersectional DI | DI ratio within age band | **0.769** | < 0.80 = violation | **VIOLATION** |
| Female 51–65 intersectional DI | DI ratio within age band | **0.760** | < 0.80 = violation | **VIOLATION** |

**Overall bias and fairness risk: High.**

### 7.6 Remediation Applied

The bias analysis confirmed discriminatory decisioning by gender and identified ZIP code as a data minimisation violation due to near-perfect collinearity with gender. As remediation, the bias-remediated dataset removes all protected attributes (`gender`, `date_of_birth`, `age`, and derived fields) and the proxy variable `zip_code` from the analytical dataset. This prevents downstream notebooks and any future model iteration from accessing these fields directly. The bias-remediated dataset is exported to `data/processed/bias_remediated_credit_applications.parquet` (500 records) and serves as input for Notebook 03.

*All analysis is documented and reproducible in `notebooks/02-bias-analysis.ipynb`.*

## 8. Privacy and Governance

This section summarises the privacy and governance audit conducted in `notebooks/03-privacy-demo.ipynb`. The assessment evaluates NovaCred's data handling practices, automated decision-making processes, and regulatory posture against GDPR (Reg. 2016/679) and the EU AI Act (Reg. 2024/1689). All findings are constrained to evidence available in the bias-remediated dataset and repository artifacts. Where controller-side documentation is required but absent (lawful basis records, consent logs, retention enforcement, access logs), the gap is flagged explicitly.

### 8.1 Methodology

The privacy audit followed a four-step approach. First, all columns in the bias-remediated dataset were classified under GDPR Art. 4(1) into four tiers: direct identifiers, quasi-identifiers (removed upstream during bias remediation), conditional sensitive fields, and non-PII financial and operational attributes. Second, population coverage checks quantified the re-identification surface area for each tier, and k-anonymity tests assessed residual uniqueness risk across both identifier-based and financial attribute combinations. Third, dataset-level evidence was mapped to specific GDPR obligations (Art. 5, 6, 7, 9, 17, 22, 25) and EU AI Act high-risk obligations (Art. 9-15). Fourth, a consolidated risk assessment was produced and a privacy-reduced analytical dataset was exported for downstream use.

### 8.2 PII Identification and Classification

Direct identifiers remain present in the bias-remediated dataset at near-complete coverage: `full_name` is populated for all 500 records (100.0%), `email` for 493 (98.6%), `ssn` for 496 (99.2%), and `ip_address` for 496 (99.2%). Any single field is sufficient to re-identify the vast majority of applicants without requiring combinations with other attributes. The absence of pseudonymisation at ingestion indicates a potential non-compliance with GDPR Art. 25 (data protection by design).

Three quasi-identifiers (`date_of_birth`, `zip_code`, `gender`) were present in the raw dataset and documented during classification, but were removed upstream during bias remediation in `02-bias-analysis.ipynb`. Their removal reduces the quasi-identifier surface in the current dataset but does not eliminate the privacy exposure that existed at collection time.

Conditional sensitive signals remain in the dataset. The behavioural spending fields `spending_alcohol` (11 records, 2.2%), `spending_gambling` (7 records, 1.4%), and `spending_adult_entertainment` (5 records, 1.0%) are sparsely populated but can enable inference about sensitive characteristics depending on context. Their presence creates disproportionate privacy risk relative to likely underwriting value and requires justification under Art. 5(1)(c) (data minimisation). The field `loan_purpose` is populated for 50 records (10.0%), and the value `medical` appears in 8 records (1.6%), creating conditional special-category exposure under Art. 9 where health-related information may be inferred.

### 8.3 Pseudonymisation Demonstration

Pseudonymisation was demonstrated as a technical safeguard aligned with GDPR Art. 25 and Recital 26. Four techniques were applied: SHA-256 hashing on `ssn`, keyed HMAC-SHA-256 on `email` (with a separate secret key held by the controller), replacement of `full_name` with an opaque reference token (`id`), and IP address generalisation to the /24 subnet by zeroing the host octet.

These transformations reduce direct disclosure risk while preserving internal record linkage for audit and consistency purposes. However, pseudonymisation does not constitute anonymisation under GDPR. The resulting dataset remains within GDPR scope because singling out and re-identification remain reasonably feasible given the means available. For low-entropy identifiers such as SSNs, keyed approaches (HMAC) reduce the risk of guess-and-check attacks because an adversary cannot validate candidate inputs without access to the secret key.

### 8.4 Re-identification Risk

Re-identification risk in the bias-remediated dataset is driven primarily by direct identifiers rather than classic quasi-identifier combinations. k-anonymity analysis confirms that single-field identifier sets (`full_name`, `email`, `ssn`, `ip_address`) each produce k equal to 1, meaning individual records are unique without requiring any attribute combination.

Residual quasi-identifier risk persists even after direct identifiers are removed. Financial attribute combinations produce critically low k-values: the triple `debt_to_income` + `savings_balance` + `loan_approved` yields 499 unique groups from 499 complete records (100.0% unique), and the four-attribute combination `annual_income` + `debt_to_income` + `credit_history_months` + `savings_balance` produces 492 unique groups from 492 complete records (100.0% unique). These results confirm that the remediated dataset remains highly re-identifiable through financial attributes alone, supporting the need for k-threshold enforcement before any row-level data export.

k-anonymity is a useful diagnostic but not a sufficient privacy guarantee. Even when k is greater than 1, datasets remain vulnerable to homogeneity attacks and background knowledge attacks. Stronger protections such as l-diversity and t-closeness should be considered for any external sharing of row-level data.

### 8.5 GDPR Compliance Assessment

The dataset-level evidence was mapped to seven GDPR obligations relevant to automated credit decisioning.

Art. 5 (processing principles): Direct identifiers at near-complete coverage materially increase exposure under Art. 5(1)(f) (integrity and confidentiality). Conditional sensitive spending fields create disproportionate privacy risk relative to likely underwriting value, raising concerns under Art. 5(1)(c) (data minimisation). The field `processing_timestamp` is missing for 438 of 500 records (87.6%), limiting traceability and weakening accountability under Art. 5(2).

Art. 6 and Art. 13 (lawful basis and transparency): No dataset fields indicate the lawful basis used for processing, consent status, or privacy notice versioning. This does not prove unlawful processing, but it means the controller's Art. 6 justification cannot be evidenced or audited from repository artifacts.

Art. 7 (consent): No consent tracking fields are present. If NovaCred relies on consent for any data sources or secondary purposes, no evidence exists to demonstrate that consent was freely given, specific, informed, unambiguous, and withdrawable as required by Art. 7.

Art. 9 (special category data): Conditional special-category exposure is present through `loan_purpose = medical` (8 records, 1.6%) and potentially through sensitive spending signals. No evidence of an applicable Art. 9 exception or necessity assessment is available.

Art. 17 (right to erasure): The dataset contains a stable record identifier (`id`) supporting record location, but `processing_timestamp` is missing for most records, limiting the ability to audit when records were processed. No repository artifacts demonstrate a deletion workflow across derived datasets, logs, and model outputs.

Art. 22 (automated decision-making): All 208 rejected applications record a `rejection_reason`, but 169 of 208 (81.2%) use `algorithm_risk_score`, which does not provide an actionable explanation to a data subject. Only 39 rejections (18.8%) use more specific reasons such as `insufficient_credit_history`, `high_dti_ratio`, or `low_income`. This transparency gap limits contestation and meaningful human review.

Art. 25 (privacy by design): Art. 25 compliance is not evidenced across five assessed dimensions: pseudonymisation at ingestion (not implemented), data minimisation by default (not implemented), purpose limitation at schema level (not evidenced), k-anonymity for analytical exports (not implemented, k = 1), and retention limits enforced technically (not evidenced).

### 8.6 EU AI Act High-Risk Classification

NovaCred's credit scoring system is classified as high-risk under EU AI Act Annex III, point 5(b), which covers AI systems intended to evaluate the creditworthiness of natural persons or establish their credit score. This classification triggers obligations under Art. 9-15 (risk management, data governance, technical documentation, record-keeping, transparency, human oversight, and accuracy/robustness).

Assessment of seven high-risk obligations against repository evidence found one partially met and six not evidenced. Art. 10 (data governance) is partially met because bias was detected upstream and protected/proxy attributes were removed, but monitoring, governance procedures, and documentation are absent. Art. 9 (risk management), Art. 11 (technical documentation), Art. 12 (record-keeping), Art. 13 (transparency), Art. 14 (human oversight), and Art. 15 (accuracy and robustness) are not evidenced in repository artifacts. The record-keeping gap is reinforced by the 87.6% missing `processing_timestamp`, which prevents reliable post-hoc auditing.

### 8.7 Consolidated Risk Summary

The table below consolidates all privacy and governance findings. Evidence is stated as metrics only; detailed regulatory analysis is in the referenced notebook sections.

| # | Finding | Evidence | Regulatory mapping | Severity |
|---|---|---|---|---|
| 1 | Direct identifiers present at near-complete coverage | 4 fields, 98-100% populated | GDPR Art. 4(1); Art. 25; Art. 5(1)(f) | Critical |
| 2 | Privacy by design not evidenced across 5 dimensions | No pseudonymisation, minimisation, purpose tagging, k-threshold, or retention enforcement | GDPR Art. 25 | Critical |
| 3 | Rejection reasons largely not meaningful | 169/208 rejections (81.2%) use `algorithm_risk_score` | GDPR Art. 22; EU AI Act Art. 13 | Critical |
| 4 | High-risk system with 6 of 7 obligations unmet | Annex III 5(b); 1 partial, 6 not evidenced | EU AI Act Art. 9-15 | Critical |
| 5 | Disparate impact confirmed by gender | DI = 0.77; 3 intersectional violations | EU AI Act Art. 10(2)(f) | Critical |
| 6 | Conditional sensitive behavioral fields collected | alcohol 11 (2.2%), gambling 7 (1.4%), adult ent. 5 (1.0%) | GDPR Art. 5(1)(c) | High |
| 7 | Health-related inference via loan_purpose | `medical` in 8/500 records (1.6%) | GDPR Art. 9 conditional | High |
| 8 | Lawful basis and notice traceability not evidenced | No consent, lawful basis, or notice fields present | GDPR Art. 6; Art. 13; Art. 5(2) | High |
| 9 | Weak dataset-level traceability | `processing_timestamp` missing 87.6% | GDPR Art. 5(2); EU AI Act Art. 12 | High |
| 10 | Retention policy not evidenced | No retention flags or deletion artifacts | GDPR Art. 5(1)(e) | High |
| 11 | Human review workflow not evidenced | No review, override, or escalation fields | GDPR Art. 22; EU AI Act Art. 14 | High |
| 12 | Residual financial quasi-identifiers yield near-total uniqueness | `debt_to_income` + `savings_balance` + `loan_approved` 499/499 unique (100.0%) | GDPR Art. 5(1)(c); Art. 25; Recital 26 | High |

**Overall privacy and governance risk: Critical.**

### 8.8 Remediation Applied

The privacy audit identified direct identifiers and conditional sensitive behavioural fields as the primary residual exposure in the bias-remediated dataset. As remediation, four direct identifiers (`full_name`, `email`, `ssn`, `ip_address`) and three conditional sensitive spending fields (`spending_alcohol`, `spending_gambling`, `spending_adult_entertainment`) were removed. The remediated dataset is exported to `data/processed/remediated_credit_applications.parquet` (500 records). This dataset represents the final privacy-reduced analytical output of the three-notebook pipeline. Remaining attributes still constitute personal data in a credit decisioning context and require appropriate access control, retention enforcement, and audit logging.

*All analysis is documented and reproducible in `notebooks/03-privacy-demo.ipynb`.*

## 9. Recommendations

This section consolidates forward-looking recommendations across all three audit dimensions. Each recommendation is mapped to the findings that motivate it and ordered by severity within its subsection. The recommendations below address production-level controls that NovaCred should implement to prevent recurrence and sustain compliance.

NovaCred's credit decisioning system cannot be deployed in its current state. The bias audit confirmed discriminatory decisioning by gender that persists after all financial controls (OR = 1.98, p = 0.0004), which must be remediated before any further automated credit decisions are made. A Data Protection Impact Assessment under GDPR Art. 35 is required and must be completed before processing resumes. Six of seven EU AI Act high-risk obligations under Art. 9-15 are not evidenced, including risk management, audit logging, transparency, and human oversight, all of which are legal preconditions for deployment under the conformity assessment framework. Direct identifiers remain unprotected in the analytical dataset, and 81.2% of rejection reasons are opaque, undermining both data subject rights and regulatory defensibility.

The subsections below provide 30 concrete recommendations organized across data quality controls (9.1), bias mitigation measures (9.2), privacy safeguards (9.3), and a cross-cutting governance framework (9.4).

### 9.1 Data Quality Controls

R1 - Enforce primary key uniqueness at ingestion (Critical). Two duplicated application IDs were identified in the raw dataset, affecting 4 records and undermining traceability. A database-level uniqueness constraint on `id` should be enforced at ingestion, with duplicates routed to a quarantine queue for manual review rather than silently accepted. Success criterion: no duplicate IDs enter any processed dataset.

R2 - Validate income presence and type at ingestion (Critical). Five records used an undocumented `annual_salary` field instead of `annual_income`, and three of those records were approved without the canonical income field populated. Income must be validated as present, numeric, and positive at ingestion. Records failing this check should be blocked from automated approval until reviewed. Success criterion: 100% of records have a valid canonical income value before any decision is made.

R3 - Enforce mandatory event timestamps (High). The `processing_timestamp` field is missing for 440 of 502 records (87.6%), which limits traceability and weakens the audit trail. Timestamps should be non-nullable and generated automatically at ingestion. Success criterion: timestamp completeness reaches 100%.

R4 - Standardise date formats at ingestion (High). Three coexisting date formats were identified in `date_of_birth` across 497 records. All dates should be converted to ISO 8601 at ingestion and stored as a parsed date type rather than free text. Success criterion: zero parsing failures and consistent age derivations across all records.

R5 - Standardise categorical encodings at ingestion (High). The `gender` field uses four encodings for two logical categories, affecting 111 records (22.1%). Controlled vocabulary mappings should be applied at intake for all categorical fields. Success criterion: no mixed encodings in processed datasets.

R6 - Enforce numeric domain constraints (High). One record has a `debt_to_income` ratio of 1.85, exceeding the valid [0, 1] domain, and two records have negative `credit_history_months` values. Domain validation rules should be enforced at ingestion to block out-of-range values. Success criterion: zero out-of-domain values in processed datasets.

R7 - Validate contact field formats (Medium). One email address is syntactically invalid (missing the @ symbol). Format validation should be applied at ingestion for contact fields. Success criterion: zero invalid email formats in processed datasets.

R8 - Add automated data quality monitoring (Medium). Scheduled completeness and validity checks should be implemented across all critical fields, with alerting on threshold breaches. Success criterion: alerts trigger on regressions and are reviewed within a defined SLA.

### 9.2 Bias Mitigation Measures

R1 - Suspend automated approvals and conduct root-cause model audit (Critical). The conditional logistic regression confirms that gender predicts loan approval independently of all financial risk controls (OR = 1.98, 95% CI: 1.36-2.89, p = 0.0004). This is not a descriptive disparity but statistical evidence that the decisioning mechanism discriminates on the basis of gender after accounting for every available measure of creditworthiness. NovaCred must place a governance hold on automated credit approvals pending investigation, audit all model features for gender-correlated effects, and document the root cause and remediation plan for regulators. No new automated credit decisions should be finalised until the source of the conditional disparity is identified and addressed. Regulatory basis: GDPR Article 22, EU AI Act Annex III.

R2 - Remove ZIP code from all model inputs immediately (High). ZIP code is near-perfectly collinear with gender (NYC: 88.8% male, LA: 93.5% female; chi-square = 324.67, p < 0.001). Although the conditional analysis shows ZIP does not independently predict approval at present (OR = 1.14, p = 0.67), retaining a feature with this level of demographic collinearity violates the GDPR data minimisation principle (Art. 5(1)(c)) and creates a structural risk that any future model trained on this data will encode gender discrimination. ZIP code must be removed immediately. Any geographic signal may only be reintroduced via a financially justified proxy (for example regional unemployment rate) after a privacy impact assessment.

R3 - Remediate intersectional disparities for high-risk subgroups (High). Three gender x age subgroups show DI ratio violations: female 26-35 (DI = 0.620, worst case), female 18-25 (DI = 0.769), and female 51-65 (DI = 0.760). These subgroup-level violations are invisible in aggregate gender analysis (overall DI = 0.77) and require targeted investigation. NovaCred must implement disaggregated monitoring at the gender x age level and treat each violating subgroup as a separate fairness incident requiring a remediation plan.

R4 - DPO review of sensitive spending categories and lawful basis assessment (High). The fields `spending_adult_entertainment`, `spending_gambling`, and `spending_alcohol` must be subject to an immediate Data Protection Officer review under GDPR Article 9. There is no demonstrated credit-relevance justification for collecting lifestyle behavioural data of this nature. These categories must be removed from any model feature set as a default position. Reinstatement requires a documented necessity assessment, a GDPR Article 9(2) lawful basis, and a proportionality review.

R5 - Implement disaggregated ongoing monitoring (High). The gender DI ratio (overall and by age band), Demographic Parity Difference, and conditional logistic OR for gender must be recomputed on every batch of credit decisions and tracked over time. Alert thresholds: DI below 0.85 triggers early warning, DI below 0.80 triggers mandatory review, and conditional OR with p below 0.05 triggers immediate escalation. Monitoring logs must be retained and available to regulators under EU AI Act Article 9.

R6 - Investigate age-based financial risk correlation (Moderate). Age disparities are explained by financial risk factors in the conditional model (p = 0.720), but the mechanism requires documentation. If shorter credit history is penalising young applicants, NovaCred should evaluate alternative creditworthiness signals (for example income trajectory or savings rate relative to age cohort) to avoid indirect age disadvantage. Age-disaggregated approval rates must be included in ongoing monitoring.

### 9.3 Privacy Safeguards

R1 - Enforce privacy by default at the dataset layer (Critical). Direct identifiers (`full_name`, `email`, `ssn`, `ip_address`) remain in the analytical dataset at 98-100% coverage, enabling re-identification without quasi-identifier combinations. NovaCred must separate direct identifiers into an access-restricted identity store and provide a pseudonymised analytical dataset as the default artifact for modelling and audit workflows. Access to raw identifiers should be role-restricted with access logging. Owner: Engineering and DPO. Done when: analytical datasets contain no direct identifiers, access to identity data is role-restricted, and access is logged and reviewable.

R2 - Replace opaque rejection reasons with a controlled taxonomy (Critical). Of 208 rejections, 169 (81.2%) use `algorithm_risk_score`, which provides no actionable explanation for contestation or human review. NovaCred must implement a controlled reason-code taxonomy with applicant-facing explanations and a defined contestation path that triggers human review. Owner: Engineering and Compliance. Done when: each rejection is stored with a specific reason code, explanations can be produced consistently, and contestation requests are tracked and resolved through a documented workflow.

R3 - Restrict conditional sensitive behavioural fields (Critical). The spending fields `spending_alcohol` (11 records, 2.2%), `spending_gambling` (7 records, 1.4%), and `spending_adult_entertainment` (5 records, 1.0%) create disproportionate privacy risk relative to likely underwriting value. NovaCred must justify the necessity of these fields under Art. 5(1)(c). If necessity is not demonstrated, they should be removed from routine analytics and modelling by default. If retained, access must be restricted and bound to a documented purpose. Owner: DPO and Data Science. Done when: either the fields are removed from analytical and modelling datasets, or necessity is documented and access is technically restricted with audit logging.

R4 - Initiate a DPIA for automated credit decisioning (Critical). A Data Protection Impact Assessment is required under GDPR Art. 35(3)(a) because the system performs systematic and extensive automated processing that produces significant effects on applicants. The DPIA must document necessity and proportionality, risk assessment for data subject rights, and mitigation measures. No further model deployment should occur until the DPIA is complete. Owner: DPO. Done when: DPIA elements under Art. 35(7) are documented, reviewed, and approved.

R5 - Implement complete decision audit logging (High). The `processing_timestamp` field is missing for 438 of 500 records (87.6%) in the post-deduplication dataset, preventing reliable post-hoc auditing. NovaCred must implement an append-only decision event log with non-nullable timestamps, model version identifiers, decision outputs, and reason codes. Log retention and integrity protections must be defined. Owner: Engineering. Done when: all decisions generate a complete audit record, timestamps are non-nullable, and logs are retained and tamper-evident according to policy.

R6 - Implement a human oversight process (High). No evidence of a review queue, override mechanism, or escalation workflow exists in repository artifacts. NovaCred must define review criteria for contested decisions and edge cases, implement a review queue, and log reviewer actions, overrides, and outcomes in the audit trail. Owner: Product and Compliance. Done when: a documented review process exists, review actions are logged, and oversight can be evidenced in audits.

R7 - Implement consent and purpose management (High). No consent tracking fields or purpose binding artifacts are present in the dataset. NovaCred must implement consent versioning and withdrawal handling for optional data sources and secondary analytics, with purpose binding enforced so secondary uses cannot occur without a documented lawful basis. Owner: Compliance and DPO. Done when: consent status and versioning are tracked, withdrawals propagate to downstream use, and purpose checks are enforced.

R8 - Adopt a retention schedule with automated deletion (High). No retention flags or deletion status fields exist in the dataset. NovaCred must adopt a retention schedule for identity data, underwriting features, decisions, and logs, and implement automated deletion with deletion audit logs across derived datasets and decision logs. Owner: Compliance and Engineering. Done when: retention is implemented in systems, deletion jobs run automatically, and deletion events are logged and reviewable.

R9 - Implement DSAR and deletion propagation (Medium). No repository evidence demonstrates an end-to-end data subject access request workflow or deletion propagation across derived datasets and logs. NovaCred must define a DSAR workflow covering the identity store, analytical datasets, training exports, and decision logs, and record DSAR processing events for auditability. Owner: Compliance and Engineering. Done when: DSAR requests can be fulfilled consistently and deletion propagation is evidenced across systems.

R10 - Produce technical documentation for high-risk AI system (Medium). No model card, data sheet, or technical specification exists in repository artifacts, leaving six of seven EU AI Act high-risk obligations (Art. 9-15) not evidenced. NovaCred must produce documentation describing intended use, training data provenance, performance metrics, limitations, and monitoring. Owner: Data Science. Done when: documentation exists in the repository and is maintained as part of release governance.

R11 - Establish ongoing fairness monitoring (Medium). The gender DI ratio, intersectional DI ratios, and conditional logistic OR must be monitored continuously to prevent bias regression. NovaCred must establish periodic fairness checks with defined thresholds and escalation procedures integrated into model governance and release processes. Owner: Data Science. Done when: monitoring runs on a defined schedule, thresholds are documented, and escalation actions are defined and used.

### 9.4 Governance Framework

This subsection proposes the operating model required to sustain GDPR and EU AI Act compliance beyond one-time technical fixes. It covers ownership, documentation, release gates, and monitoring routines for a high-risk creditworthiness assessment system.

NovaCred must assign four governance roles: an AI system owner responsible for end-to-end compliance and release sign-off, a privacy owner (DPO or delegate) responsible for DPIA maintenance, DSAR workflows, and retention policy governance, an engineering owner for audit logging, access logging, and retention automation, and a model risk owner for performance monitoring and periodic fairness checks.

Three governance artifacts must be maintained on an ongoing basis. The DPIA package under Art. 35 must be updated whenever processing changes materially. High-risk AI documentation aligned to Art. 9-15 obligations must cover logging design, transparency materials, and human oversight procedures. Model documentation (model card) and dataset documentation (data sheet) must be versioned and linked to decision records.

Release gates must block production deployment unless four conditions are met: the DPIA is current, audit logging is complete, the rejection reason taxonomy is implemented, and human oversight procedures are documented. All datasets, models, and policy artifacts must be versioned, and decisions must be linked to these versions in audit logs.

Monitoring must follow a defined cadence. Fairness metrics must be recomputed on each decision batch with escalation at defined thresholds. Audit log quality KPIs, including timestamp completeness and rejection reason code distribution, must be reviewed periodically. Retention and deletion job execution must be audited, and DSAR completion metrics must be tracked and reported.

An incident response workflow must be defined for privacy and AI governance issues, covering detection, escalation, remediation, and post-incident documentation. DSAR processing must follow a defined workflow covering the identity store, analytical datasets, derived datasets, and decision logs.

## 10. Conclusion

This audit assessed NovaCred's automated credit decisioning pipeline across data quality, fairness, and privacy using evidence available in the dataset and repository artifacts. The assessment identified 16 data quality issues (overall risk: Moderate-High), confirmed discriminatory decisioning by gender that persists after all financial controls (overall risk: High), and documented critical privacy and governance gaps including unprotected direct identifiers, opaque rejection reasons, and six of seven EU AI Act high-risk obligations not evidenced (overall risk: Critical).

The three most consequential findings are interconnected. The gender bias finding (OR = 1.98, p = 0.0004) means NovaCred is making systematically unfair credit decisions. The rejection transparency finding (81.2% opaque reasons) means affected applicants cannot meaningfully contest those decisions. The absence of audit logging (87.6% missing timestamps) means neither NovaCred nor a regulator can investigate when or how these decisions were made. Together, these create a governance failure that is greater than the sum of its parts: a system that discriminates, cannot explain itself, and cannot be audited.

All identified data quality issues were remediated programmatically across the three-notebook pipeline. Protected attributes and proxy variables were removed to prevent direct discriminatory feature access, and direct identifiers and sensitive behavioural fields were removed to reduce re-identification exposure. These dataset-level remediations address the immediate analytical risks but do not resolve the underlying governance deficits. The 30 recommendations in Section 9 provide a structured path from the current state to a compliant operating posture, organized by urgency and mapped to specific regulatory obligations. Remediation feasibility is high. The critical-priority actions (suspension of automated approvals, privacy by default, rejection reason taxonomy, and DPIA initiation) are technically implementable and should be completed before any further model deployment.

## 11. Contributions

| Team Member | Role | Key Contributions | Primary Sections Owned |
|------------|------|-------------------|----------------------|
| Michael Kania | Product Lead | README audit report, presentation, Q&A preparation, cross-notebook review and refinement, coordination | README, Presentation, Notebook 03 |
| Dominik Hohlenstein | Data Engineer | Data loading pipeline, data quality analysis, cleaning and remediation, repository structure | Notebook 01, `src/data_loading.py` |
| Niklas Klaus Juergen Duettmann | Data Scientist | Bias detection, fairness metrics, statistical testing, proxy and intersectional analysis | Notebook 02 |
| Mohamed Aannaque | Governance Officer | Privacy assessment, GDPR article mapping, EU AI Act classification | Notebook 03 |

_Detailed commit history is available in the repository's Git log._
