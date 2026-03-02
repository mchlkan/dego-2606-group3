# NovaCred Model Governance and Data Audit (DEGO Group Project - Group 3)
DEGO 2606 Group Project – Credit Application Governance Analysis (NovaCred)

---

## 1. Team and Roles

**Team Lead — Michael Kania**  
Email: 72782@novasbe.pt

**Data Engineer - Dominik Hohlenstein**  
Email: 70135@novasbe.pt

**Data Scientist — Niklas Klaus Jürgen Düttmann**  
Email: 71916@novasbe.pt

**Governance Officer — Mohamed Aannaque**  
Email: 71359@novasbe.pt

---

## 2. Project Overview

### 2.1 Objective

The objective of this project is to conduct a comprehensive governance audit of NovaCred’s credit approval dataset and decision pipeline.

This audit focuses on three core areas:

1. Data quality risks affecting model reliability
2. Bias and fairness risks affecting protected groups
3. Privacy and regulatory compliance risks under GDPR and the EU AI Act

The goal is to identify, quantify, and document governance risks and propose actionable mitigation measures.

---

### 2.2 Scope

This project evaluates NovaCred’s historical credit application dataset used to support automated credit approval decisions.

The audit includes:

- Assessment of data completeness, consistency, and validity
- Detection of potential disparate impact across demographic groups
- Identification of personal data and regulatory compliance risks
- Evaluation of governance and auditability practices

This project does not modify the production model but evaluates risks in the supporting data and pipeline.

---

### 2.3 Dataset Description

The dataset consists of historical credit application records used by NovaCred’s automated loan decision system. Each record represents one loan application and is stored in a nested JSON structure containing applicant information, financial attributes, behavioral data, and the corresponding decision outcome.

The dataset is organized into the following main components:

| Component | Name | Type | Description | Exemplary Variables |
|----------|------|------|-------------|---------------------|
| Identifier | `_id` | String | Unique identifier for each credit application | application ID |
| Applicant Information | `applicant_info` | Nested object | Contains personal and demographic information about the applicant | full_name, email, gender, date_of_birth, zip_code |
| Financial Information | `financials` | Nested object | Contains financial characteristics used to assess creditworthiness | annual_income, credit_history_months, debt_to_income, savings_balance |
| Behavioral Information | `spending_behavior` | Array of objects | Contains categorized spending data reflecting the applicant’s expenditure patterns | category, amount |
| Decision Outcome | `decision` | Nested object | Contains the automated loan decision and associated decision parameters | loan_approved, interest_rate, approved_amount, rejection_reason |

Due to its nested structure, the dataset requires preprocessing and flattening before analysis. The presence of personal, demographic, and financial attributes makes it suitable for assessing data quality, fairness risks, and governance considerations in automated credit decision systems.

---

## 3. Repository Structure

```
project-root/
│
├── data/
│   ├── raw/              # Raw dataset (excluded from Git; may contain PII)
│   └── processed/        # Processed analysis datasets
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
├── environment.yml       # Conda environment specification
├── requirements.txt      # Python dependencies
└── README.md             # Project audit report
```

---

## 4. Governance and Reproducibility

This project follows reproducible and auditable development practices aligned with model governance principles. The raw dataset is excluded from version control due to the presence of sensitive and personally identifiable information. All analysis is conducted using a fully specified environment and modular code structure to ensure traceability, reproducibility, and auditability of findings.

Version control is managed through protected branches and peer-reviewed pull requests to ensure controlled and documented changes throughout the project lifecycle.

---

## 5. Reproducibility Instructions

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

### 6.1 Completeness  
tbd

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

tbd
