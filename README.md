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

tbd