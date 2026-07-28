import numpy as np
import pandas as pd
from faker import Faker
import random

# Fixed seed - same dataset every time this runs, for the whole team
np.random.seed(42)
random.seed(42)
fake = Faker("en_IN")
Faker.seed(42)

N_PATIENTS = 2000
N_ADMISSIONS = 2300

# ---------- 1. Departments ----------
departments = pd.DataFrame({
    "Department_ID": [f"D{i:02d}" for i in range(1, 9)],
    "Department_Name": ["Cardiology", "Orthopedics", "Pediatrics", "General Medicine",
                         "Neurology", "Gynecology", "Oncology", "ENT"],
    "Floor": [2, 1, 3, 1, 4, 3, 5, 2],
    "Building": ["A", "A", "B", "A", "B", "B", "C", "A"],
})

# Diagnosis/Treatment mapped realistically per department
dept_diagnosis = {
    "Cardiology": ["Hypertension", "Heart Failure", "Arrhythmia", "Coronary Artery Disease"],
    "Orthopedics": ["Fracture", "Joint Replacement", "Sprain", "Osteoarthritis"],
    "Pediatrics": ["Fever", "Asthma", "Infection", "Growth Concern"],
    "General Medicine": ["Fever", "Diabetes", "Viral Infection", "Anemia"],
    "Neurology": ["Migraine", "Epilepsy", "Stroke", "Nerve Disorder"],
    "Gynecology": ["Pregnancy Care", "PCOS", "Menstrual Disorder", "Fibroids"],
    "Oncology": ["Chemotherapy Cycle", "Tumor Removal", "Radiation Therapy", "Biopsy Follow-up"],
    "ENT": ["Sinusitis", "Hearing Loss", "Tonsillitis", "Ear Infection"],
}
dept_treatment = {
    "Cardiology": ["Angioplasty", "Medication", "ECG Monitoring", "Bypass Surgery"],
    "Orthopedics": ["Surgery", "Physiotherapy", "Casting", "Joint Replacement"],
    "Pediatrics": ["Observation", "Medication", "Vaccination", "Nebulization"],
    "General Medicine": ["Medication", "IV Therapy", "Observation", "Lab Monitoring"],
    "Neurology": ["Medication", "Therapy", "MRI Monitoring", "Surgery"],
    "Gynecology": ["Ultrasound Monitoring", "Surgery", "Medication", "Therapy"],
    "Oncology": ["Chemotherapy", "Radiation", "Surgery", "Palliative Care"],
    "ENT": ["Surgery", "Medication", "Hearing Aid Fitting", "Observation"],
}
# Base cost per treatment complexity (used to derive realistic billing later)
treatment_base_cost = {
    "Angioplasty": 180000, "Medication": 3000, "ECG Monitoring": 8000, "Bypass Surgery": 250000,
    "Surgery": 90000, "Physiotherapy": 12000, "Casting": 6000, "Joint Replacement": 200000,
    "Observation": 5000, "Vaccination": 1500, "Nebulization": 2500,
    "IV Therapy": 7000, "Lab Monitoring": 4000,
    "Therapy": 15000, "MRI Monitoring": 20000,
    "Ultrasound Monitoring": 6000,
    "Chemotherapy": 120000, "Radiation": 150000, "Palliative Care": 40000,
    "Hearing Aid Fitting": 25000,
}

# ---------- 2. Doctors ----------
n_doctors = 36
doctors = pd.DataFrame({
    "Doctor_ID": [f"DOC{i:03d}" for i in range(1, n_doctors + 1)],
    "Doctor_Name": [fake.name() for _ in range(n_doctors)],
    "Department_ID": np.random.choice(departments["Department_ID"], n_doctors),
    "Specialization": None,
    "Experience_Years": np.random.randint(1, 35, n_doctors),
})
doctors["Specialization"] = doctors["Department_ID"].map(
    dict(zip(departments["Department_ID"], departments["Department_Name"]))
)

# ---------- 3. Staff ----------
n_staff = 70
staff = pd.DataFrame({
    "Staff_ID": [f"STF{i:03d}" for i in range(1, n_staff + 1)],
    "Staff_Name": [fake.name() for _ in range(n_staff)],
    "Department_ID": np.random.choice(departments["Department_ID"], n_staff),
    "Role": np.random.choice(["Nurse", "Ward Assistant", "Technician", "Receptionist"], n_staff, p=[0.5, 0.2, 0.2, 0.1]),
    "Shift": np.random.choice(["Morning", "Evening", "Night"], n_staff),
})

# ---------- 4. Beds ----------
n_beds = 180
beds = pd.DataFrame({
    "Bed_ID": [f"B{i:03d}" for i in range(1, n_beds + 1)],
    "Department_ID": np.random.choice(departments["Department_ID"], n_beds),
    "Ward": np.random.choice(["General Ward", "ICU", "Private Room"], n_beds, p=[0.6, 0.15, 0.25]),
    "Bed_Type": np.random.choice(["Standard", "Electric", "ICU Bed"], n_beds, p=[0.6, 0.25, 0.15]),
    "Bed_Status": "Available",  # set properly after admissions are generated
})

# ---------- 5. Resources (optional) ----------
resource_names = ["Ventilator", "X-Ray Machine", "MRI Scanner", "Wheelchair", "Oxygen Cylinder",
                   "ECG Machine", "Dialysis Machine", "Infusion Pump"]
resources = pd.DataFrame({
    "Resource_ID": [f"R{i:02d}" for i in range(1, len(resource_names) * 2 + 1)],
    "Resource_Name": resource_names * 2,
    "Department_ID": np.random.choice(departments["Department_ID"], len(resource_names) * 2),
    "Quantity": np.random.randint(2, 15, len(resource_names) * 2),
})
resources["Available_Quantity"] = resources["Quantity"] - np.random.randint(0, 3, len(resources))
resources["Available_Quantity"] = resources["Available_Quantity"].clip(lower=0)

# ---------- 6. Patients ----------
indian_cities = {
    "Mumbai": "Maharashtra", "Delhi": "Delhi", "Bengaluru": "Karnataka", "Pune": "Maharashtra",
    "Hyderabad": "Telangana", "Ahmedabad": "Gujarat", "Chennai": "Tamil Nadu", "Kolkata": "West Bengal",
    "Jaipur": "Rajasthan", "Lucknow": "Uttar Pradesh",
}
city_list = list(indian_cities.keys())

patients = pd.DataFrame({
    "Patient_ID": [f"P{i:05d}" for i in range(1, N_PATIENTS + 1)],
    "Patient_Name": [fake.name() for _ in range(N_PATIENTS)],
    "Age": np.random.randint(1, 95, N_PATIENTS),
    "Gender": np.random.choice(["Male", "Female"], N_PATIENTS),
    "Blood_Group": np.random.choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], N_PATIENTS,
                                     p=[0.22, 0.05, 0.3, 0.05, 0.28, 0.03, 0.05, 0.02]),
    "City": np.random.choice(city_list, N_PATIENTS),  # even-ish real distribution, no city skewed as "sicker"
    "Contact_Number": [fake.phone_number() for _ in range(N_PATIENTS)],
})
patients["State"] = patients["City"].map(indian_cities)

# ---------- 7. Admissions ----------
start_date = pd.Timestamp("2024-01-01")
end_date = pd.Timestamp("2025-12-31")
date_range_days = (end_date - start_date).days

admission_rows = []
for i in range(1, N_ADMISSIONS + 1):
    dept = departments.sample(1).iloc[0]
    dept_name = dept["Department_Name"]
    dept_id = dept["Department_ID"]

    doctor = doctors[doctors["Department_ID"] == dept_id].sample(1).iloc[0]
    bed = beds[beds["Department_ID"] == dept_id].sample(1).iloc[0]
    patient = patients.sample(1).iloc[0]

    admission_date = start_date + pd.Timedelta(days=np.random.randint(0, date_range_days))
    # realistic stay length varies by department
    stay_ranges = {"Cardiology": (2, 10), "Orthopedics": (3, 14), "Pediatrics": (1, 6),
                   "General Medicine": (1, 7), "Neurology": (2, 12), "Gynecology": (1, 5),
                   "Oncology": (1, 15), "ENT": (1, 4)}
    low, high = stay_ranges[dept_name]
    stay_length = np.random.randint(low, high + 1)
    discharge_date = admission_date + pd.Timedelta(days=int(stay_length))

    diagnosis = random.choice(dept_diagnosis[dept_name])
    treatment = random.choice(dept_treatment[dept_name])

    admission_rows.append({
        "Admission_ID": f"ADM{i:05d}",
        "Patient_ID": patient["Patient_ID"],
        "Admission_Date": admission_date.date(),
        "Discharge_Date": discharge_date.date(),
        "Department_ID": dept_id,
        "Doctor_ID": doctor["Doctor_ID"],
        "Bed_ID": bed["Bed_ID"],
        "Diagnosis": diagnosis,
        "Treatment": treatment,
        "Admission_Status": "Discharged",  # default; a subset flipped to Admitted below
    })

admissions = pd.DataFrame(admission_rows)

# A realistic subset still currently admitted (recent admissions, no discharge yet conceptually)
admissions = admissions.sort_values("Admission_Date").reset_index(drop=True)
still_admitted_idx = admissions.tail(40).index  # most recent 40 -> currently admitted
admissions.loc[still_admitted_idx, "Admission_Status"] = "Admitted"

# ---------- Update Bed_Status based on real admissions ----------
occupied_beds = admissions.loc[admissions["Admission_Status"] == "Admitted", "Bed_ID"].unique()
beds["Bed_Status"] = np.where(beds["Bed_ID"].isin(occupied_beds), "Occupied", "Available")

# ---------- 8. Billing ----------
billing_rows = []
for i, row in admissions.iterrows():
    base_cost = treatment_base_cost.get(row["Treatment"], 10000)
    stay_len = (pd.Timestamp(row["Discharge_Date"]) - pd.Timestamp(row["Admission_Date"])).days
    stay_len = max(stay_len, 1)
    total_amount = base_cost + (stay_len * np.random.randint(800, 1500))
    total_amount = round(total_amount * np.random.uniform(0.95, 1.05), 2)  # small natural variation

    insurance_coverage = round(total_amount * np.random.choice([0, 0.3, 0.5, 0.8, 1.0],
                                                                 p=[0.3, 0.2, 0.2, 0.2, 0.1]), 2)
    if row["Admission_Status"] == "Admitted":
        # ongoing admission -> partial/no payment yet, not a final bill
        paid_amount = round(np.random.uniform(0, insurance_coverage if insurance_coverage > 0 else total_amount * 0.2), 2)
        payment_status = "Pending"
    else:
        paid_amount = total_amount - insurance_coverage if insurance_coverage < total_amount else total_amount
        paid_amount = round(paid_amount, 2)
        payment_status = "Paid" if paid_amount >= (total_amount - insurance_coverage) - 1 else "Partial"

    billing_rows.append({
        "Bill_ID": f"BILL{i+1:05d}",
        "Patient_ID": row["Patient_ID"],
        "Admission_ID": row["Admission_ID"],
        "Total_Amount": total_amount,
        "Insurance_Coverage": insurance_coverage,
        "Paid_Amount": paid_amount,
        "Payment_Status": payment_status,
    })

billing = pd.DataFrame(billing_rows)

# ================= Realistic messiness (controlled, not chaotic) =================

# 1. Missing values in a few non-critical fields (~2-3%)
def add_missing(df, col, frac=0.02):
    idx = df.sample(frac=frac, random_state=42).index
    df.loc[idx, col] = np.nan
    return df

patients = add_missing(patients, "Contact_Number", 0.03)
patients = add_missing(patients, "Blood_Group", 0.02)
staff = add_missing(staff, "Shift", 0.02)

# 2. A handful of exact duplicate rows
dup_patients = patients.sample(n=20, random_state=1)
patients = pd.concat([patients, dup_patients], ignore_index=True)

dup_admissions = admissions.sample(n=15, random_state=1)
admissions = pd.concat([admissions, dup_admissions], ignore_index=True)

# 3. Inconsistent casing/spacing in category fields
def messy_case(val):
    r = np.random.random()
    if r < 0.1:
        return val.lower()
    elif r < 0.15:
        return f" {val} "
    return val

admissions["Department_ID"] = admissions["Department_ID"]  # keep IDs clean (keys shouldn't be messy)
staff["Role"] = staff["Role"].apply(messy_case)
beds["Ward"] = beds["Ward"].apply(messy_case)

# 4. A few genuine outliers (not everywhere)
outlier_idx = admissions.sample(n=5, random_state=2).index
admissions.loc[outlier_idx, "Discharge_Date"] = admissions.loc[outlier_idx, "Admission_Date"].apply(
    lambda d: (pd.Timestamp(d) + pd.Timedelta(days=int(np.random.randint(30, 60)))).date()
)

# ================= Save =================
import os
os.makedirs("/home/claude/data", exist_ok=True)

departments.to_csv("/home/claude/data/departments.csv", index=False)
doctors.to_csv("/home/claude/data/doctors.csv", index=False)
staff.to_csv("/home/claude/data/staff.csv", index=False)
beds.to_csv("/home/claude/data/beds.csv", index=False)
resources.to_csv("/home/claude/data/resources.csv", index=False)
patients.to_csv("/home/claude/data/patients.csv", index=False)
admissions.to_csv("/home/claude/data/admissions.csv", index=False)
billing.to_csv("/home/claude/data/billing.csv", index=False)

print("Departments:", departments.shape)
print("Doctors:", doctors.shape)
print("Staff:", staff.shape)
print("Beds:", beds.shape)
print("Resources:", resources.shape)
print("Patients:", patients.shape)
print("Admissions:", admissions.shape)
print("Billing:", billing.shape)
print("\nAll 8 CSVs saved to /home/claude/data/")
