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
