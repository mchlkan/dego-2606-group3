# NovaCred Model Governance and Data Audit (DEGO Group Project - Group 3)

**Group 3 | DEGO 2606 Group Project – Credit Application Governance Analysis (NovaCred)**

---

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
6. [Data Quality Audit](#6-data-quality-audit)
   - 6.1 [Completeness](#61-completeness)
   - 6.2 [Consistency](#62-consistency)
   - 6.3 [Validity](#63-validity)
   - 6.4 [Accuracy](#64-accuracy)
   - 6.5 [Summary of Issues and Impact](#65-summary-of-issues-and-impact)
   - 6.6 [Remediation Steps](#66-remediation-steps)
7. [Bias and Fairness Analysis](#7-bias-and-fairness-analysis)
   - 7.1 [Methodology](#71-methodology)
   - 7.2 [Gender Bias — Disparate Impact Analysis](#72-gender-bias--disparate-impact-analysis)
   - 7.3 [Age Bias Analysis](#73-age-bias-analysis)
   - 7.4 [Proxy Discrimination Analysis](#74-proxy-discrimination-analysis)
   - 7.5 [Interaction Effects](#75-interaction-effects)
   - 7.6 [Fairness Metrics Summary](#76-fairness-metrics-summary)
8. [Privacy and Governance (NB03)](#8-privacy-and-governance-nb03)
   - 8.1 [Methodology](#81-methodology)
   - 8.2 [PII identification and classification](#82-pii-identification-and-classification)
   - 8.3 [Pseudonymisation demonstration](#83-pseudonymisation-demonstration)
   - 8.4 [Re-identification risk](#84-re-identification-risk)
   - 8.5 [GDPR article mapping](#85-gdpr-article-mapping)
   - 8.6 [EU AI Act high-risk classification](#86-eu-ai-act-high-risk-classification)
   - 8.7 [Governance controls and DPIA](#87-governance-controls-and-dpia)
   - 8.8 [Data remediation output](#88-data-remediation-output)
   - 8.9 [Consolidated risk summary](#89-consolidated-risk-summary)
- [9. Recommendations](#9-recommendations)
9. [Recommendations](#9-recommendations)
   - 9.1 [Data Quality Improvements](#91-data-quality-improvements)
   - 9.2 [Bias Mitigation Measures](#92-bias-mitigation-measures)
   - 9.3 [Privacy Safeguards](#93-privacy-safeguards)
   - 9.4 [Governance Framework Recommendations](#94-governance-framework-recommendations)
10. [Conclusion](#10-conclusion)
11. [Contributions](#11-contributions)

---

## 1. Executive Summary

tbd

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

---

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

---

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

---

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

---

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
---

## 6. Data Quality Audit

The data quality assessment evaluates the dataset across four dimensions: completeness, consistency, validity, and accuracy. Each issue is quantified and classified by severity (Low, Moderate, High, Critical) based on its potential impact on decision integrity, model reliability, and auditability. Full technical details, code, and per-record analysis are available in `notebooks/01-data-quality.ipynb`.

### 6.1 Completeness

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

### 6.2 Consistency

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

### 6.3 Validity

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

### 6.4 Accuracy

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

### 6.5 Summary of Issues and Impact

The assessment identified 16 distinct data quality issues across all four dimensions. The consolidated risk profile is as follows:

| Dimension | Overall Risk | Key Drivers |
|-----------|-------------|-------------|
| Completeness | Moderate | Empty string masking, audit trail gaps, schema inconsistency |
| Consistency | Moderate | Primary key duplication, categorical encoding fragmentation |
| Validity | Moderate | DTI domain violation, negative values in decision-critical fields |
| Accuracy | Moderate–High | Loan approvals without canonical income, spending-income contradiction |

**Overall dataset risk: Moderate–High.** The dataset is structurally sound in its core decision fields, but multiple high-severity issues directly affect auditability, underwriting defensibility, and governance compliance. The most critical findings are: (1) three loans approved without documented income in the canonical field, (2) two duplicated application IDs violating primary key integrity, (3) empty strings silently masking missing values, and (4) 87.6% of records lacking a processing timestamp.

### 6.6 Remediation Steps

All identified issues were remediated programmatically in `notebooks/01-data-quality.ipynb` (Section 10). The cleaned dataset is exported to `data/processed/cleaned_credit_applications.parquet` and serves as the input for all downstream analyses (Notebooks 02 and 03).

Remediation actions applied:

| Action | Target | Effect |
|--------|--------|--------|
| Reconcile `annual_income` and `annual_salary` into unified field | 5 records | All records now have a canonical income value |
| Normalize empty strings to NaN | 14 values across 4 fields | True missingness accurately reflected |
| Standardize gender encoding (M→Male, F→Female) | 111 records | Consistent categorical representation for bias analysis |
| Parse `date_of_birth` to ISO 8601 datetime | 497 records across 3 formats | Consistent temporal format for age derivation |
| Cast `annual_income` to numeric | 8 string values + 1 float | Homogeneous numeric type |
| Deduplicate on application ID (retain most complete record) | 2 duplicates removed | 500 unique records in cleaned dataset |
| Flag records with 3+ missing critical fields | 5 records | Flagged for manual review, not excluded |
| Flag approved loans with missing canonical income | 3 records | Flagged as decision logic anomaly |
| Flag DTI outside valid domain [0, 1] | 1 record | Flagged for manual review |
| Set negative `credit_history_months` to NaN | 2 records | Logically impossible values removed |
| Set negative `savings_balance` to NaN | 1 record | Implausible value removed |
| Set invalid email (missing @) to NaN | 1 record | Malformed value removed |
| Replace zero income with NaN | 1 record | Distinguishes true zero from missing |
| Cast `processing_timestamp` to datetime | 62 records | Correct temporal type |

Recommended controls for production implementation are prioritized in four tiers in the notebook (Section 10.2), ranging from P1 (block approvals without income, enforce primary key constraints) through P4 (schema versioning, automated monitoring).

---

## 7. Bias and Fairness Analysis

### 7.1 Methodology

The bias analysis was conducted on 500 records after deduplication. Prior to any group-level computation, three pre-processing steps were applied: (1) inconsistent gender encoding was normalised (`M` → `Male`, `F` → `Female`, blank → `NaN`), (2) date of birth was parsed across three mixed formats (`YYYY-MM-DD`, `DD/MM/YYYY`, `YYYY/MM/DD`) to derive applicant age, and (3) one negative `credit_history_months` value was set to `NaN`.

The analysis covers four dimensions: selection rate fairness (Disparate Impact ratio), statistical significance of group differences (chi-square, Kruskal-Wallis, Welch's t-test), proxy discrimination (ZIP code, spending behaviour), and intersectional effects (gender × age group). Fairlearn's `demographic_parity_difference` was used as a standardised cross-validation metric.

All analysis is documented and reproducible in `notebooks/02-bias-analysis.ipynb`.

---

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

---

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

---

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

---

### 7.5 Fairness Metrics Summary

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

---

## 8. Privacy and Governance (NB03)

This section summarises our privacy and governance audit based on `notebooks/03-privacy-demo.ipynb`. The assessment relies on evidence available in the bias-remediated dataset and repository artifacts. Where controller-side documentation is required (lawful basis records, consent logs, retention enforcement, DSAR workflows, access logs), we flag gaps as not evidenced.

### 8.1 Methodology

We followed a four-step approach:

1. We classified personal data under GDPR Art. 4(1), covering direct identifiers, upstream quasi-identifiers removed during bias remediation, and conditional sensitive fields that can enable sensitive inference depending on values.
2. We quantified exposure using coverage checks and value distributions to identify re-identification and inference hotspots.
3. We mapped the evidence to relevant GDPR obligations and assessed EU AI Act high-risk status and related obligations for creditworthiness assessment systems.
4. We translated gaps into an urgency-tier action plan and produced a privacy-reduced analytical dataset for downstream use.

### 8.2 PII identification and classification

Direct identifiers remain present in the bias-remediated dataset, enabling re-identification without requiring quasi-identifier combinations. The key direct identifiers are:

- `full_name`, `email`, `ssn`, `ip_address` (near-complete coverage)

We also documented upstream privacy exposure from the raw dataset. The following quasi-identifiers existed at collection time and were removed during bias remediation in `02-bias-analysis.ipynb`:

- `date_of_birth`, `zip_code`, `gender`

Conditional sensitive signals remain present:

- Behavioral spending fields are sparsely populated but present (`spending_alcohol` 11 records, 2.2%; `spending_gambling` 7 records, 1.4%; `spending_adult_entertainment` 5 records, 1.0%).
- `loan_purpose` is populated for 50 records (10.0%). The value `medical` appears in 8 records (1.6%), which may reveal health-related information depending on context.

### 8.3 Pseudonymisation demonstration

We demonstrate pseudonymisation as a technical safeguard aligned with GDPR Art. 25 and Recital 26. The following transformations reduce disclosure risk while preserving internal linkage:

- SHA-256 hashing applied to SSNs
- keyed HMAC-SHA-256 applied to emails
- replacement of `full_name` with an opaque reference token (`id`)
- IP generalisation to reduce precision

Pseudonymisation does not constitute anonymisation. It reduces disclosure risk, but the resulting dataset remains within GDPR scope.

### 8.4 Re-identification risk

Re-identification risk is driven primarily by direct identifiers rather than classic quasi-identifier combinations. In practice, this means that uniqueness exists without relying on multi-field linkage. For any external sharing or broad internal access, we treat the dataset as high re-identification risk by default.

We also note that k-anonymity is a diagnostic, not a guarantee. Even when k is greater than 1, homogeneity attacks and background knowledge attacks can still enable inference. Stronger protections include l-diversity and t-closeness and should be considered for any row-level dataset exports.

### 8.5 GDPR article mapping

We mapped the dataset-level evidence to key GDPR obligations:

- Art. 5 principles: direct identifiers increase integrity and confidentiality exposure, and conditional sensitive fields raise data minimisation and purpose limitation concerns.
- Art. 6 and Art. 13: lawful basis and transparency traceability are not evidenced because no fields indicate lawful basis, consent status, or privacy notice versioning.
- Art. 9 (conditional): `loan_purpose = medical` introduces conditional health-related inference risk depending on context.
- Art. 17: end-to-end deletion capability is not evidenced from repository artifacts, including deletion propagation to derived datasets and logs.
- Art. 22 safeguards: rejected applications have a recorded reason, but most reasons are not meaningful. There are 210 rejections (42.0% of 500 records). 170 of 210 (81.0%) use `algorithm_risk_score`, limiting contestation and review in practice.
- Art. 25: privacy by design and by default is not evidenced at the dataset layer because direct identifiers remain present in the analytical dataset.
- Art. 5(1)(e): retention enforcement is not evidenced. We propose a retention schedule to support storage limitation compliance.

### 8.6 EU AI Act high-risk classification

We classify the system as high-risk under the EU AI Act because it performs automated creditworthiness assessment for natural persons (Annex III, point 5(b)). High-risk obligations apply across risk management, data governance, technical documentation, logging, transparency, and human oversight (Art. 9 to Art. 15).

Based on repository artifacts, multiple obligations are not evidenced, including risk management documentation, technical documentation, and human oversight procedures. Logging is also weak at the dataset layer, with `processing_timestamp` missing for 438 of 500 records (87.6%).

### 8.7 Governance controls and DPIA

We prioritised governance controls by urgency. Detailed implementation guidance is provided in the Recommendations section.

Critical priority controls:
- Enforce privacy by default by separating identity data from analytical datasets and restricting raw identifier access.
- Replace opaque rejection reasons with a controlled taxonomy and implement applicant-facing explanations with a contestation workflow.
- Remove or restrict conditional sensitive behavioral fields until necessity is documented, and exclude them from routine analytics and modelling by default.

High priority controls:
- Implement complete decision audit logging with non-nullable timestamps, append-only decision events, and defined retention.
- Implement a documented human oversight process for contested decisions and edge cases, with review actions logged in the audit trail.
- Implement consent and purpose management for secondary uses, including consent versioning and withdrawal handling.
- Adopt a retention schedule with automated deletion and deletion audit logs.

Medium priority controls:
- Implement DSAR and deletion propagation workflow across derived datasets and logs.
- Produce technical documentation required for a high-risk system, including intended use, limitations, and monitoring.
- Establish periodic fairness monitoring to prevent regression over time.

A DPIA process under GDPR Art. 35 is required for automated credit decisioning that produces significant effects on applicants. The DPIA should document necessity and proportionality, risk assessment, and mitigation measures before operational deployment.

### 8.8 Data remediation output

We produce a privacy-reduced analytical dataset at `data/processed/remediated_credit_applications.parquet`. This output removes:

- direct identifiers: `full_name`, `email`, `ssn`, `ip_address`
- conditional sensitive behavioral fields: `spending_alcohol`, `spending_gambling`, `spending_adult_entertainment`

Protected attributes and key proxies (`gender`, `date_of_birth`, `age`, `zip_code`) are removed upstream in `02-bias-analysis.ipynb`.

### 8.9 Consolidated risk summary

The table below consolidates the highest-impact privacy and governance issues and maps them to relevant GDPR and EU AI Act obligations.

| Issue | Evidence | GDPR mapping | EU AI Act mapping | Risk level |
|---|---|---|---|---|
| Direct identifiers present in analytical dataset | `full_name`, `email`, `ssn`, `ip_address` present with near-complete coverage | Art. 4(1); Art. 25; Art. 5(1)(f) | Art. 10 (data governance) | Critical |
| Decision transparency gap for rejections | 210 rejections (42.0% of 500). 170 of 210 (81.0%) use `algorithm_risk_score` | Art. 22 safeguards; Art. 13 | Art. 13; Art. 14 | Critical |
| Weak dataset-level traceability | `processing_timestamp` missing for 438 records (87.6%) | Art. 5(2) | Art. 12 | High |
| Conditional sensitive behavioral fields present | alcohol 11 (2.2%), gambling 7 (1.4%), adult entertainment 5 (1.0%) | Art. 5(1)(c); Art. 5(1)(b) | Art. 10 | High |
| Conditional health-related inference | `loan_purpose` populated 50 (10.0%); `medical` 8 (1.6%), which may reveal health-related information depending on context | Art. 9 conditional; Art. 5(1)(c) | Art. 10 | High |
| Lawful basis and notice traceability not evidenced | no fields indicating lawful basis, consent status, or privacy notice versioning | Art. 6; Art. 13; Art. 5(2) | Art. 13 | High |
| Erasure workflow not evidenced | no repository evidence of DSAR and deletion propagation across derived datasets and logs | Art. 17; Art. 5(2) | n/a | Medium |
| Retention enforcement not evidenced | no retention flags or deletion status fields | Art. 5(1)(e); Art. 5(2) | Art. 12 | High |
| Human oversight not evidenced | no evidence of review queue, overrides, or escalation workflow | Art. 22 safeguards | Art. 14 | High |
| High-risk AI Act posture | creditworthiness assessment classified as high-risk (Annex III, point 5(b)) | n/a | Annex III, point 5(b); Art. 9 to Art. 15 | Critical |
| Consent and purpose management not evidenced | no consent tracking fields or purpose binding artifacts are present | Art. 7; Art. 13; Art. 5(1)(b); Art. 5(2) | Art. 13 | High |

---

## 9. Recommendations

### 9.1 Data Quality Improvements  

This subsection lists the recommended data quality controls derived from `notebooks/01-data-quality.ipynb`. The goal is to prevent recurrence of the highest-impact quality issues observed in the raw data and to improve traceability, validity, and consistency for downstream bias and privacy audits.

| Priority | Control | Target field(s) | Implementation detail | Success criterion |
|---|---|---|---|---|
| Critical | Enforce primary key uniqueness at ingestion and quarantine duplicates | `id` | Add database uniqueness constraint and ingestion-stage duplicate check with quarantine queue | No duplicate IDs enter the processed dataset |
| Critical | Validate income presence and type at ingestion | `annual_income` and any alternative income fields | Reject or route to review when income is missing, non-numeric, or non-positive | 100% of records have a valid canonical income value |
| High | Enforce mandatory event timestamps | `processing_timestamp` | Make timestamp non-nullable and generated automatically at ingestion | Timestamp completeness reaches 100% |
| High | Standardise date formats | `date_of_birth` | Convert to ISO 8601 at ingestion and store parsed date type, not free text | Zero parsing failures and consistent age derivations |
| High | Standardise categorical encodings | `gender` and other categorical fields | Apply controlled vocabulary and mapping rules at intake | No mixed encodings in processed datasets |
| High | Enforce numeric domain constraints | `debt_to_income`, `credit_history_months` | Validate ranges and block out-of-domain values | Zero out-of-domain values in processed datasets |
| Medium | Validate contact fields | `email` | Apply format validation and reject malformed entries | Zero invalid email formats in processed datasets |
| Medium | Add automated data quality monitoring | All critical fields | Scheduled checks with alerting on completeness/validity regressions | Alerts trigger on threshold breaches and are reviewed |

### 9.2 Bias Mitigation Measures

The following recommendations are derived directly from the findings in Section 7 and are ordered by severity.

**R1 — Suspend automated approvals and conduct root-cause model audit (Critical)**

The conditional logistic regression confirms that gender predicts loan approval independently of all financial risk controls (OR = 1.98, 95% CI: 1.36–2.89, p = 0.0004). This is not a descriptive disparity — it is statistical evidence that the decisioning mechanism discriminates on the basis of gender after accounting for every available measure of creditworthiness. NovaCred must: (1) place a governance hold on automated credit approvals pending investigation; (2) audit all model features for gender-correlated effects; (3) document the root cause and remediation plan for regulators. No new automated credit decisions should be finalised until the source of the conditional disparity is identified and addressed. Regulatory basis: GDPR Article 22; EU AI Act Annex III; ECOA.

**R2 — Remove ZIP code from all model inputs immediately (High)**

ZIP code is near-perfectly collinear with gender (NYC: 88.8% male, LA: 93.5% female; χ²(2) = 324.67, p < 0.001). Although the conditional analysis shows ZIP does not independently predict approval at present (OR = 1.14, p = 0.67), retaining a feature with this level of demographic collinearity violates the GDPR data minimisation principle (Art. 5(1)(c)) and creates a structural risk that any future model trained on this data will encode gender discrimination. ZIP code must be removed immediately; any geographic signal may only be reintroduced via a financially justified proxy (e.g., regional unemployment rate) after a privacy impact assessment.

**R3 — Remediate intersectional disparities for high-risk subgroups (High)**

Three gender × age subgroups show DI ratio violations: female 26–35 (DI = 0.620, worst case), female 18–25 (DI = 0.769), and female 51–65 (DI = 0.760). These subgroup-level violations are invisible in aggregate gender analysis (overall DI = 0.77) and require targeted investigation. NovaCred must implement disaggregated monitoring at the gender × age level and treat each violating subgroup as a separate fairness incident requiring a remediation plan.

**R4 — DPO review of sensitive spending categories and lawful basis assessment (High)**

`spending_adult_entertainment`, `spending_gambling`, and `spending_alcohol` must be subject to an immediate Data Protection Officer review under GDPR Article 9. There is no demonstrated credit-relevance justification for collecting lifestyle behavioural data of this nature. These categories must be removed from any model feature set as a default position; reinstatement requires a documented necessity assessment, a GDPR Article 9(2) lawful basis, and a proportionality review.

**R5 — Implement disaggregated ongoing monitoring (High)**

The gender DI ratio (overall and by age band), Demographic Parity Difference, and conditional logistic OR for gender must be recomputed on every batch of credit decisions and tracked over time. Alert thresholds: DI < 0.85 (early warning), DI < 0.80 (mandatory review), conditional OR p < 0.05 (immediate escalation). Monitoring logs must be retained and available to regulators under EU AI Act Article 9.

**R6 — Investigate age-based financial risk correlation (Moderate)**

Age disparities are explained by financial risk factors in the conditional model (p = 0.720), but the mechanism requires documentation. If shorter credit history is penalising young applicants, NovaCred should evaluate alternative creditworthiness signals (e.g., income trajectory, savings rate relative to age cohort) to avoid indirect age disadvantage. Age-disaggregated approval rates must be included in ongoing monitoring.

### 9.3 Privacy Safeguards  

This section provides the detailed governance recommendations, including implementation steps, ownership, and completion criteria. The recommendations are derived from `notebooks/03-privacy-demo.ipynb` and are prioritised by urgency.

### Critical priority

1. Privacy by default at the dataset layer  
Owner: Engineering and DPO  
Implementation: Separate direct identifiers into an identity store with strict access controls and access logging. Provide a pseudonymised analytical dataset as the default artifact for modelling and audit workflows.  
Done when: Analytical datasets contain no direct identifiers, access to identity data is role-restricted, and access is logged and reviewable.

2. Decision transparency and contestation workflow  
Owner: Engineering and Compliance  
Implementation: Replace opaque rejection reasons with a controlled reason-code taxonomy. Provide applicant-facing explanations and define a contestation path that triggers human review.  
Done when: Each rejection is stored with a specific reason code, explanations can be produced consistently, and contestation requests are tracked and resolved through a documented workflow.

3. Data minimisation for conditional sensitive behavioral fields  
Owner: DPO and Data Science  
Implementation: Justify necessity of behavioral spending fields. If not required, remove from routine analytics and modelling. If retained, restrict access and bind use to documented purpose.  
Done when: Either the fields are removed from analytical and modelling datasets, or necessity is documented and access is technically restricted with audit logging.

### High priority

4. Complete decision audit logging  
Owner: Engineering  
Implementation: Implement an append-only decision event log with non-nullable timestamps, model version identifiers, decision outputs, and reason codes. Define log retention and integrity protections.  
Done when: All decisions generate a complete audit record, timestamps are non-nullable, and logs are retained and tamper-evident according to policy.

5. Human oversight process  
Owner: Product and Compliance  
Implementation: Define review criteria for contested decisions and edge cases. Implement a review queue and log reviewer actions, overrides, and outcomes in the audit trail.  
Done when: A documented review process exists, review actions are logged, and oversight can be evidenced in audits.

6. Consent and purpose management for secondary uses  
Owner: Compliance and DPO  
Implementation: Implement consent versioning and withdrawal handling for optional data sources and secondary analytics. Enforce purpose binding so secondary uses cannot occur without a documented lawful basis.  
Done when: Consent status and versioning are tracked, withdrawals propagate to downstream use, and purpose checks are enforced.

7. Retention schedule and automated deletion  
Owner: Compliance and Engineering  
Implementation: Adopt a retention schedule for identity data, underwriting features, decisions, and logs. Implement automated deletion and deletion audit logs across derived datasets and decision logs.  
Done when: Retention is implemented in systems, deletion jobs run automatically, and deletion events are logged and reviewable.

### Medium priority

8. DSAR and deletion propagation workflow  
Owner: Compliance and Engineering  
Implementation: Define an end-to-end DSAR workflow that covers identity store, analytical datasets, training exports, and decision logs. Record DSAR processing events for auditability.  
Done when: DSAR requests can be fulfilled consistently and deletion propagation is evidenced across systems.

9. Technical documentation for a high-risk system  
Owner: Data Science  
Implementation: Produce a model card and technical documentation describing intended use, training data provenance, performance metrics, limitations, and monitoring.  
Done when: Documentation exists in the repository and is maintained as part of release governance.

10. Fairness monitoring to prevent regression  
Owner: Data Science  
Implementation: Establish periodic fairness checks with thresholds and escalation. Integrate monitoring into model governance and release processes.  
Done when: Monitoring runs on a defined schedule, thresholds are documented, and escalation actions are defined and used.

### 9.4 Governance Framework Recommendations  

This subsection proposes the operating model required to sustain GDPR and EU AI Act compliance beyond one-time technical fixes. It focuses on ownership, documentation, release gates, and monitoring routines for a high-risk creditworthiness assessment system.

**Roles and accountability**
- Assign an AI system owner responsible for end-to-end compliance and release sign-off.
- Assign a privacy owner (DPO or delegate) responsible for DPIA maintenance, DSAR workflows, and retention policy governance.
- Assign engineering ownership for audit logging, access logging, and retention automation.
- Assign model risk ownership for performance monitoring and periodic fairness checks.

**Required governance artifacts**
- Maintain a DPIA package (Art. 35) and update it when processing changes.
- Maintain high-risk AI documentation aligned to Art. 9–15 obligations, including logging design, transparency materials, and human oversight procedures.
- Maintain model documentation (model card) and dataset documentation (data sheet) with versioning.

**Release gates and change management**
- Block production release unless: DPIA is current, audit logging is complete, rejection reason taxonomy is implemented, and human oversight procedures are documented.
- Version datasets, models, and policy artifacts, and link decisions to these versions in audit logs.

**Monitoring and reporting cadence**
- Run periodic fairness monitoring and define escalation thresholds.
- Review audit log quality KPIs, including timestamp completeness and distribution of rejection reason codes.
- Perform retention and deletion job audits and track DSAR completion metrics.

**DSAR and incident workflows**
- Define a DSAR process covering identity store, analytical datasets, derived datasets, and decision logs.
- Define an incident response workflow for privacy and AI governance issues with escalation and documentation.

---

## 10. Conclusion

tbd

---

## 11. Contributions

| Team Member | Role | Key Contributions | Primary Sections Owned |
|------------|------|-------------------|----------------------|
| Michael Kania | Product Lead | _To be completed_ | README, Presentation, Coordination |
| Dominik Hohlenstein | Data Engineer | _To be completed_ | Data loading, Cleaning, Repository setup |
| Niklas Klaus Jürgen Düttmann | Data Scientist | _To be completed_ | Bias analysis, Fairness metrics |
| Mohamed Aannaque | Governance Officer | _To be completed_ | Privacy assessment, GDPR mapping |

_Detailed commit history is available in the repository's Git log._
