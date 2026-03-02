# Project Plan

This document outlines the task breakdown, ownership, timeline, and deliverable checklist for the project.

---

## Timeline Overview (as of 01/03/2026)

| Phase | Target | Status |
|-------|--------|--------|
| Setup — Repo, environment, structure, docs | Complete | Done |
| Data Loading — Canonical loader and flattening | This week | Done |
| Analysis — Data quality, bias, privacy notebooks | This week | Ongoing (70%) |
| README — Fill in all analysis sections | This week | Ongoing (60%) |
| Presentation — Record 6-min video | Before deadline | Not started |
| Final Review — Code runs, README polished, repo clean | Before deadline | Not started |

---

## Notebook Ownership

| Notebook | Owner |
|----------|-------|
| `01-data-quality.ipynb` | Dominik Hohlenstein (Data Engineer) |
| `02-bias-analysis.ipynb` | Niklas Klaus Jürgen Düttmann (Data Scientist) |
| `03-privacy-demo.ipynb` | Mohamed Aannaque (Governance Officer) |
| README + Presentation | Michael Kania (Product Lead) |

---

## Task Breakdown by Role

### Michael Kania — Product Lead

| Task | Output | Priority |
|------|--------|----------|
| Build `src/data_loading.py` with `load_raw_data()` function | Reusable loader (Dominik to review) | High |
| Write and maintain all README analysis sections based on team findings | Completed audit report | High |
| Write Executive Summary once all analyses are finalized | Standalone briefing for stakeholders | High |
| Coordinate and produce the 6-min video presentation | Video with all members speaking | High |
| Prepare for Q&A as Product Lead | Understand all sections, able to explain any part | High |
| Coordinate team workflow, review PRs, track progress | Smooth collaboration | Ongoing |

### Dominik Hohlenstein — Data Engineer

| Task | Output | Priority |
|------|--------|----------|
| Review and commit `src/data_loading.py` | Working & reusable data_loading.py | High |
| Complete `01-data-quality.ipynb` | Full data quality analysis notebook | High |
| Identify all data quality issues (along completeness, consistency, validity, accuracy) | Quantified findings with counts and percentages | High |
| Propose and demonstrate remediation steps in code | Working fixes for identified issues | High |
| Handle `spending_behavior` array flattening strategy | Decide on pivot/aggregation approach | High |
| Create processed dataset in `data/processed/` | Clean CSV or parquet for other notebooks to consume | Medium |

### Niklas Klaus Jürgen Düttmann — Data Scientist

| Task | Output | Priority |
|------|--------|----------|
| Complete `02-bias-analysis.ipynb` | Full bias analysis notebook | High |
| Calculate Disparate Impact Ratio for gender | DI value with four-fifths rule interpretation | High |
| Analyze age-based discrimination patterns | Age group approval rate comparison | High |
| Investigate proxy discrimination (zip code, spending) | Correlation analysis between proxies and outcomes | High |
| Analyze interaction effects (age × gender) | Combined group analysis | Medium |
| Create clear visualizations for all bias findings | Charts for README and presentation | Medium |

### Mohamed Aannaque — Governance Officer

| Task | Output | Priority |
|------|--------|----------|
| Complete `03-privacy-demo.ipynb` | Full privacy analysis notebook | High |
| Identify and classify all PII fields | Table of direct identifiers and quasi-identifiers | High |
| Demonstrate pseudonymization on at least one PII column | Working code with explanation | High |
| Map findings to GDPR articles (Art. 5, 6, 17, 22) | Compliance assessment | High |
| Classify system under EU AI Act risk framework | Risk level with justification | Medium |
| Propose governance controls (audit trails, oversight, retention) | Actionable recommendations | Medium |

---

## Deliverable Checklist (from project description; as of 01/03/2026)

### GitHub Repository

- [x] Repository is public
- [x] Repository has a description set on GitHub
- [x] Minimum 10 meaningful commits across the project
- [x] All team members have commits under their own accounts
- [x] Commit messages are clear and descriptive
- [x] Commit history shows steady progress (not a single bulk upload)
- [ ] All code runs without errors

### Notebooks

- [ ] `01-data-quality.ipynb` — Identifies and quantifies all data quality issues, proposes remediation
- [ ] `02-bias-analysis.ipynb` — DI ratio, age bias, proxy analysis, interaction effects, visualizations
- [ ] `03-privacy-demo.ipynb` — PII identification, pseudonymization demo, GDPR mapping

### README

- [ ] Executive Summary with key metrics
- [ ] Data Quality Audit sections filled with findings
- [ ] Bias and Fairness sections filled with findings
- [ ] Privacy and Governance sections filled with findings
- [ ] Recommendations are concrete and actionable
- [ ] Conclusion synthesizes findings across all three areas
- [ ] Contributions table completed with specific contributions per member

### Presentation

- [ ] Video is under 6 minutes
- [ ] All team members appear and speak
- [ ] Key visualizations from analysis are shown
- [ ] Specific numbers and metrics are cited
- [ ] Structure: Intro (30s) → Data Quality (90s) → Bias (90s) → Governance (90s) → Conclusion (30s)

### Submission

- [ ] Repository URL submitted on Moodle before 23:59 the day before Session 6
- [ ] Video uploaded (YouTube unlisted, or Google Drive link in README, or in `presentation/` folder)
- [ ] Final commit is before the deadline
- [ ] Peer evaluation completed within 48 hours after Session 6