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
| Male | — | ~248 | **66.0%** |
| Female | — | ~251 | **50.6%** |

**Disparate Impact ratio:** `50.6% / 66.0% = 0.7668`

The four-fifths (80%) rule classifies any DI ratio below 0.80 as indicative of potential disparate impact. At 0.77, NovaCred's historical approval data constitutes a formal four-fifths rule violation. A chi-square test of independence confirms that this gap is not attributable to chance: **χ² p-value = 0.0007**, making the association between gender and approval outcome highly statistically significant.

**Interest rate pricing:** Among approved applicants, males received a mean rate of **4.63%** and females **4.49%**. A Welch's t-test yields **p = 0.3132** — no statistically significant pricing discrimination was found. The bias is confined to the selection decision, not the pricing of approved loans.

---

### 7.3 Age Bias Analysis

Applicant age was derived from the `date_of_birth` field after mixed-format parsing. Applicants were grouped into five standard age bands:

| Age Group | Approved | Total | Approval Rate |
|---|---|---|---|
| 18–25 | 10 | 22 | **45.5%** |
| 26–35 | 73 | 157 | **46.5%** |
| 36–50 | 153 | 225 | **68.0%** |
| 51–65 | 49 | 84 | 58.3% |
| 66+ | 4 | 8 | 50.0% |

Applicants under 35 are approved at approximately 46% — more than 20 percentage points below the peak group (36–50 at 68%). A Kruskal-Wallis test across all five age groups yields **p = 0.0007**, confirming that the differences are statistically significant and not attributable to random variation.

Age is a protected characteristic in many jurisdictions. A model that systematically disadvantages young adults requires a rigorous justification based on credit-relevant financial factors rather than age itself.

---

### 7.4 Proxy Discrimination Risks

**ZIP Code**

ZIP codes in the dataset cluster into two geographic areas: NYC (prefix `10xxx`) and LA (prefix `90xxx`). Approval rates differ substantially between these regions:

| Region | Approval Rate |
|---|---|
| NYC (10xxx) | **64.5%** |
| LA (90xxx) | 51.7% |
| Other | 57.9% |

A 12.8 percentage point gap between regions is a proxy discrimination risk: if the gender or demographic composition differs between these areas, ZIP code acts as a stand-in for a protected attribute in the model's decision. A chi-square test on the gender × region contingency table was conducted to assess this association (see `notebooks/02-bias-analysis.ipynb`, Section 6).

**Sensitive Spending Categories**

The dataset contains `spending_adult_entertainment`, `spending_gambling`, and `spending_alcohol`. These categories warrant scrutiny for two distinct reasons:

1. *Proxy discrimination:* If these features differ systematically by gender, including them in a credit scoring model encodes proxy bias. Analysis showed insufficient data for `spending_adult_entertainment` and `spending_gambling` to reach statistical conclusions. For `spending_alcohol`, no significant gender difference was found (p = 0.13).

2. *Data minimisation violation:* Regardless of statistical significance, collecting behavioural data on gambling and adult content without a clear credit-relevance justification is inconsistent with GDPR Article 5(1)(c). These features should be excluded from any model feature set until a lawful basis assessment is completed.

---

### 7.5 Fairness Metrics Summary

| Finding | Metric | Value | Threshold | Status |
|---|---|---|---|---|
| Gender Disparate Impact ratio | DI = female rate / male rate | **0.7668** | < 0.80 = violation | **VIOLATION** |
| Gender bias significance | Chi-square p-value | **0.0007** | < 0.05 = significant | **SIGNIFICANT** |
| Age group bias significance | Kruskal-Wallis p-value | **0.0007** | < 0.05 = significant | **SIGNIFICANT** |
| Interest rate pricing by gender | Welch t-test p-value | 0.3132 | < 0.05 = significant | No bias detected |
| Demographic Parity Difference | DPD (Fairlearn) | **0.1539** | > 0.10 = concern | **CONCERN** |
| Geographic proxy (ZIP code) | Approval rate gap NYC vs. LA | **12.8 pp** | — | Investigate |

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

**R1 — Investigate and remediate gender-based selection bias (Critical)**

The DI ratio of 0.77 constitutes a formal four-fifths rule violation. NovaCred must audit which model features are driving the gender gap. The recommended approach is to run a logistic regression of `loan_approved` on all features and inspect coefficients — any feature that loses significance when gender is added as a control is a candidate proxy. Until the root cause is identified, the current model should not be used for new credit decisions in jurisdictions where disparate impact is prohibited.

**R2 — Remove or justify ZIP code as a model feature (High)**

A 12.8 percentage point approval rate gap between NYC and LA areas requires investigation. If the chi-square test confirms that gender distribution differs across regions, ZIP code must be removed from the feature set or replaced with a financially justified substitute (e.g., regional unemployment rate). Geographic redlining is explicitly prohibited under the Fair Housing Act and equivalent EU legislation.

**R3 — Remove sensitive spending categories from the feature set (High)**

`spending_adult_entertainment`, `spending_gambling`, and `spending_alcohol` must be excluded from any model feature set immediately. There is no demonstrated credit-relevant justification for collecting these categories, and their inclusion violates GDPR Article 5(1)(c) (data minimisation). Their removal should be treated as a default position; reinstatement requires a documented necessity assessment and lawful basis review by the data protection officer.

**R4 — Apply age-neutral credit assessment criteria (Medium)**

The 20+ percentage point approval rate gap between applicants under 35 and the 36–50 group requires justification. If shorter credit history length is the driver (plausible for young applicants), the model should incorporate alternative creditworthiness signals such as income-to-rent ratio or savings trajectory rather than penalising age implicitly. A controlled analysis with `credit_history_months` as a covariate should be conducted before the next model iteration.

**R5 — Implement ongoing DI ratio monitoring (Medium)**

The DI ratio should be computed on every new batch of credit decisions and tracked over time. A threshold alert at DI < 0.80 should trigger a mandatory review before decisions in that batch are finalised. This monitoring should be logged and made available to regulators on request, as required under EU AI Act Article 9 (risk management system) for high-risk AI systems.

**R6 — Conduct intersectional fairness review (Medium)**

Single-attribute DI ratios do not capture compounded disadvantage at the intersection of gender and age. The interaction heatmap in `notebooks/02-bias-analysis.ipynb` (Section 8) should be reviewed specifically for the 18–35 female segment. If approval rates for this group fall more than 10 percentage points below the overall rate, a dedicated sub-group audit is warranted.

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