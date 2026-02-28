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

## 8. Privacy and Governance Assessment

### 8.1 Identification of Personal Data (PII)  

There are various kinds of personal data contained in the dataset, which fall under the category of personal data as defined under the General Data Protection Regulation (GDPR). Personal data is defined under the GDPR as information relating to an identified or identifiable natural person.

#### Direct Identifiers (High Risk)

The following fields directly identify an individual:

- `full_name`
- `email`
- `ssn`

These characteristics uniquely identify an individual without the need for any additional information. For instance, the Social Security Number (SSN) is considered highly sensitive personal data due to the possibility of misuse for identity theft or financial fraud. These fields require strong security measures and should not be used in analytics environments without pseudonymization.

#### Personal Data and Quasi-Identifiers (Moderate to High Risk)

The dataset also includes attributes that may not directly identify a person alone but can enable re-identification when combined with other data:

- `date_of_birth`
- `ip_address`
- `zip_code`
- `employment_status`
- `annual_income`
- `credit_score`
- `loan_amount`

When multiple quasi-identifiers are combined (e.g., zip code + date of birth + employment status), the risk of re-identification increases substantially. This poses privacy risks even after direct identifiers are removed.
   
### 8.2 GDPR Compliance Assessment  

Based on the dataset and its current structure, several governance and compliance gaps are observable when assessed against key GDPR principles.

#### 1. Lack of Explicit Consent Tracking

There is no field indicating whether the applicant has provided consent for data processing. GDPR requires a lawful basis for processing personal data, and where consent is used, it must be explicit and properly documented. The absence of a consent flag or timestamp creates uncertainty regarding the lawfulness of processing.

#### 2. Absence of a Data Retention Policy

The dataset does not include metadata such as collection timestamps or defined retention periods. According to the GDPR storage limitation principle, personal data must be retained only for as long as necessary for the specified purpose. Without retention rules, there is a risk of excessive data storage.

#### 3. Storage of Sensitive Identifiers in Raw Format

Highly sensitive identifiers such as `ssn` and `email` are stored in raw, non-pseudonymized form. This increases exposure risk in the event of unauthorized access or data breaches. GDPR encourages pseudonymization and data minimization to reduce such risks.

#### 4. Missing Audit Trail for Automated Decisions

There are no fields capturing information such as:

- decision timestamp  
- model version  
- reviewer identity  

Without these elements, it becomes difficult to demonstrate accountability, ensure transparency, or explain credit decisions to affected individuals.

#### 5. Lack of Documented Human Oversight

Automated credit scoring may significantly affect individuals’ financial opportunities. Under GDPR, individuals have the right not to be subject solely to automated decision-making without safeguards. The dataset does not indicate the existence of a human review process or override mechanism.

---

Overall, while the dataset may support analytical modeling, it lacks several structural governance elements required for full GDPR compliance, particularly in relation to accountability, transparency, and data protection safeguards.

### 8.3 EU AI Act Risk Classification  
According to the EU’s AI Act, the credit scoring systems fall under the list of high-risk AI systems, as they may have significant effects on individuals’ access to financial services.
High-risk systems need to have the following elements implemented:
   - A documented risk management process
   - Data governance and quality management
   - Technical documentation
   - Logging and traceability
   - Human oversight procedures
   - Bias monitoring and fairness evaluation
The existing structure of the data set does not show the implementation of the above elements. For instance, the logging of decisions is not present, as is the documentation of oversight procedures.

### 8.4 Data Protection Risks  
Some of the primary identified risks from this dataset include:
   - Identity Theft Risk due to Raw SSN Storage
   - Re-identification Risk due to Quasi-Identifiers
   - Lack of Explainability of Automated Decisions
   - Discrimination Risk if Fairness is not Monitored
   - Over-collection of Personal Data beyond Necessity
These risks could lead to legal, reputational, and trust-related consequences if not properly addressed.

### 8.5 Recommended Governance Controls  
To minimize the risk of non-compliance and operation, the following control mechanisms can be adopted:
   1. Pseudonymization of SSN and email data before use in analytics
   2. Removal of full_name data from the model datasets
   3. Development of a data retention policy
   4. Implementation of role-based access control for sensitive data
   5. Logging of credit decisions with timestamp and model version
   6. Human review process for borderline and rejected cases
   7. Monitoring of fairness and bias in the credit model
   8. Documenting the lawful basis for processing data according to the GDPR
These control mechanisms would greatly improve the alignment and accountability within the credit decision process.

---

## 9. Recommendations

### 9.1 Data Quality Improvements  
tbd

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
