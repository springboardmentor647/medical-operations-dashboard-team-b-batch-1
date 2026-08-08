# Medical Operations Dashboard — Team B Batch 1

## Milestone 1 — Work Completed

Milestone 1 focused on establishing the core data foundation for the **Medical Operations Intelligence Dashboard**. During this milestone, the team generated a synthetic healthcare dataset, performed data cleaning and validation, and developed an initial set of operational and financial **Key Performance Indicators (KPIs)**.

---

### 1. Dataset Generation

A synthetic healthcare dataset was generated to represent realistic hospital operations, including patient, admission, staff, billing, insurance, bed, and operational information.

#### Dataset Overview

| Attribute         | Details                         |
| ----------------- | ------------------------------- |
| **Total Records** | 5,000                           |
| **Total Columns** | 32                              |
| **Dataset Type**  | Synthetic Healthcare Dataset    |
| **Primary Use**   | Hospital Operations & Analytics |

The dataset was designed to support healthcare operational analysis, KPI development, and dashboard development.

---

### 2. Data Cleaning & Preparation

The generated dataset was cleaned and prepared to ensure consistency, reliability, and analysis readiness.

The following data preparation activities were performed:

* Converted `Admission_Date` and `Discharge_Date` into appropriate datetime formats.
* Converted `Contact_Number` into string format to preserve complete contact information.
* Checked the dataset for missing values.
* Identified and reviewed duplicate records.
* Validated patient age values for logical consistency.
* Performed general data quality checks.
* Reviewed relevant fields for consistency and usability in downstream analysis.

These preprocessing steps helped improve the quality and reliability of the dataset before further analysis.

---

### 3. Data Validation

Business and logical validation rules were applied to verify the consistency of financial information within the dataset.

The following relationships were validated:

* `Paid_Amount` should not exceed `Total_Amount`.
* `Insurance_Coverage + Paid_Amount` should equal `Total_Amount`.

These validation checks helped ensure that the financial records were logically consistent and suitable for further analysis and reporting.

---

### 4. KPI Development

Initial **Key Performance Indicators (KPIs)** were identified and calculated to provide a high-level overview of hospital operations and financial performance.

#### KPIs Developed

| KPI                             | Purpose                                                            |
| ------------------------------- | ------------------------------------------------------------------ |
| **Total Admissions**            | Measures the total number of hospital admissions.                  |
| **Currently Admitted Patients** | Tracks the number of patients currently admitted.                  |
| **Average Length of Stay**      | Measures the average duration of patient hospitalization.          |
| **Bed Occupancy Percentage**    | Indicates the utilization level of available hospital beds.        |
| **Total Revenue**               | Represents the total revenue generated from hospital billing.      |
| **Collection Rate Percentage**  | Measures the proportion of billed revenue that has been collected. |

These KPIs provide an initial overview of important **operational, capacity, and financial metrics** and establish the foundation for the project dashboard.

---

### 5. Cleaned Dataset

After completing the data cleaning and validation process, the cleaned dataset was exported for further analysis and dashboard development.

#### Output Dataset

```text
medical_operations_dashboard_cleaned.csv
```

The data cleaning and preprocessing workflow is documented in the following Jupyter Notebook:

```text
notebooks/Data_Cleaning.ipynb
```

---

### 6. KPI Summary

The initial KPI calculations and summary were prepared using **Microsoft Excel**.

The KPI summary provides an initial overview of the hospital's operational and financial performance and will serve as a foundation for:

* Dashboard development
* Further data analysis
* KPI visualization
* Operational performance monitoring

---

## 🎯 Milestone 1 Outcome

By the end of **Milestone 1**, the team successfully established the initial project foundation by preparing and validating the healthcare dataset and developing the first set of operational and financial **Key Performance Indicators (KPIs)**.

### Completed Deliverables

* ✅ Generated a synthetic healthcare dataset containing **5,000 records and 32 columns**
* ✅ Performed data cleaning and preprocessing
* ✅ Checked missing values and duplicate records
* ✅ Validated patient age values
* ✅ Applied financial and business validation rules
* ✅ Developed initial operational KPIs
* ✅ Developed initial financial KPIs
* ✅ Exported the cleaned dataset
* ✅ Documented the cleaning process in a Jupyter Notebook
* ✅ Prepared the initial KPI summary in Microsoft Excel

---

## 🔍 Next Milestone

The prepared dataset and KPI definitions will be used in the next milestone for:

* 🔍 **Exploratory Data Analysis (EDA)**
* 📊 **Detailed Data Visualization**
* 📈 **Dashboard Development**
* 🏥 **Deeper Healthcare Operational Insights**

The next phase will focus on transforming the validated healthcare data into meaningful visual insights and actionable information for understanding hospital operations.

---

## 📁 Relevant Project Files

```text
medical-operations-dashboard-team-b-batch-1/
│
├── data/
│   └── medical_operations_dashboard_cleaned.csv
│
├── notebooks/
│   └── Data_Cleaning.ipynb
│
└── README.md
```

> **Note:** The project structure may be updated as additional notebooks, datasets, dashboards, and documentation are added in subsequent milestones.

---

## 📌 Conclusion

Milestone 1 established a reliable and validated data foundation for the **Medical Operations Intelligence Dashboard**.

Through dataset generation, data cleaning, validation, and KPI development, the project is now prepared to move into the next stage of **exploratory analysis, visualization, and dashboard development**.

The insights generated in the upcoming milestones will help provide a clearer understanding of **patient flow, hospital capacity, resource utilization, and financial performance**.
