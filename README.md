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
8. [Privacy and Governance Assessment](#8-privacy-and-governance-assessment)
   - 8.1 [Identification of Personal Data (PII)](#81-identification-of-personal-data-pii)
   - 8.2 [Pseudonymization Demonstration](#82-pseudonymization-demonstration)
   - 8.3 [GDPR Compliance Assessment](#83-gdpr-compliance-assessment)
   - 8.4 [EU AI Act Risk Classification](#84-eu-ai-act-risk-classification)
   - 8.5 [Data Protection Risks](#85-data-protection-risks)
   - 8.6 [Recommended Governance Controls](#86-recommended-governance-controls)
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

In the data quality assessment, we evaluate the dataset across four dimensions: completeness, consistency, validity, and accuracy. We quantify each issue and classify by severity (Low, Moderate, High, Critical) based on its potential impact on decision integrity, model reliability, and auditability. Full technical details, code, and per-record analysis are available in `notebooks/01-data-quality.ipynb`.

### 6.1 Completeness

Decision-critical financial fields are nearly complete: `debt_to_income`, `credit_history_months`, and `savings_balance` are fully populated across all 502 records. `annual_income` is missing for 5 records (1.0%), but investigation revealed that these 5 records contain an undocumented `annual_salary` field instead indicating a schema inconsistency in the data collection pipeline rather than true data loss. No record is missing income information entirely.

The dataset also contains empty strings in several string-type fields that are not detected by standard null checks. After normalization, effective missingness is: `email` — 7 records (1.4%), `date_of_birth` — 5 records (1.0%), `gender` — 3 records (0.6%), and `zip_code` — 2 records (0.4%). Identity fields `ssn` and `ip_address` are each missing for 5 records (1.0%).

Conditional completeness checks on decision outcome fields revealed zero violations: All approved records contain `interest_rate` and `approved_amount`, and all rejected records contain a `rejection_reason`. This indicates well-structured data capture logic in the core credit workflow.

Among metadata fields, `processing_timestamp` is present in only 62 of 502 records (12.4%) and `loan_purpose` in only 50 records (10.0%). These structural gaps weaken the audit trail and reduce interpretability of decisions.

Spending behavior data is sparse at the per-category level (84–99% missing per category), but this reflects the data collection design. Each applicant likely reports 1–4 spending categories out of 15 available. All 502 records contain at least some spending data. A co-occurrence analysis identified 5 records with 3 or more missing critical fields simultaneously, suggesting systematic data collection failures for specific applicants.

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
tbd

### 6.3 Validity  
tbd

### 6.4 Accuracy  
tbd

### 6.5 Summary of Issues and Impact  
tbd

---

## 7. Bias and Fairness Analysis

### 7.1 Methodology  
tbd

### 7.2 Gender Bias Analysis  
tbd

### 7.3 Age Bias Analysis  
tbd

### 7.4 Proxy Discrimination Risks  
tbd

### 7.5 Fairness Metrics Summary  
tbd

---

## 8. Privacy and Governance Assessment

### 8.1 Identification of Personal Data (PII)  
_TBD_

### 8.2 GDPR Compliance Assessment  
tbd

### 8.3 EU AI Act Risk Classification  
tbd

### 8.4 Data Protection Risks  
tbd

### 8.5 Recommended Governance Controls  
tbd

---

## 9. Recommendations

### 9.1 Data Quality Improvements  
tbd

### 9.2 Bias Mitigation Measures  
tbd

### 9.3 Privacy Safeguards  
tbd

### 9.4 Governance Framework Recommendations  
tbd

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