# Hospital Readmission Prediction

This repository contains a project aimed at predicting hospital readmission within 30 days using logistic regression. The project includes a dataset related to patient demographics, medical history, and hospital stay details, as well as a Jupyter Notebook that trains and evaluates a logistic regression model.

**Project Overview**:

The primary goal of this project is to use patient data to build a logistic regression model that predicts whether a patient will be readmitted to the hospital within 30 days of discharge.

**Dataset Description**:

The dataset contains the following key columns:

- Age: Age of the patient.
- Gender: Gender of the patient (Male, Female, Other).
- Medical History: List of patient’s medical conditions (e.g., heart disease, diabetes).
- Number of Previous Admissions: Number of times the patient was previously admitted to the hospital.
- Days Since Last Discharge: Number of days since the patient was last discharged from the hospital.
- Primary Diagnosis: Primary reason for the hospital admission.
- Readmitted within 30 Days: The target variable indicating whether the patient was readmitted within 30 days (0 = No, 1 = Yes).

**Model**:
A logistic regression model was trained on a subset of the data, with key features like Age, Number of Previous Admissions, and Days Since Last Discharge. The model was evaluated using accuracy and confusion matrix metrics. For simplicity, the model was saved using the pickle library.
