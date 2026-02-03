# Customer Churn Prediction System

An end-to-end Machine Learning project that predicts whether a customer is likely to churn (leave a service) using historical data.
The project includes data analysis, model training, and an interactive Streamlit web application for real-time predictions and insights.

 Project Overview

Customer churn is a critical business problem where companies lose customers to competitors.
This project aims to:

Analyze customer behavior patterns

Predict churn probability using Machine Learning

Visualize insights using EDA

Provide an interactive dashboard for decision-making

 Features

 Exploratory Data Analysis (EDA) with visual insights

 Machine Learning model (Random Forest + Calibration)

 Class imbalance handling using up-sampling

 Feature scaling & one-hot encoding

 Streamlit web app for live predictions

 Simple login authentication system

 Cyber-risk score simulation (extended feature logic)

##🗂️ Project Structure
Customer-Churn-Prediction/
│
├── Telco-Customer-Churn.csv     # Dataset
├── churn_model.py               # Model training & saving
├── eda_analysis.py              # EDA & visualization
├── churn_app.py                 # Streamlit web application
│
├── churn_model.pkl              # Trained ML model
├── model_columns.pkl            # Model feature columns
├── scaler.pkl                   # StandardScaler object
│
├── churn_distribution.png
├── churn_by_contract.png
├── charges_vs_tenure.png
├── cyber_vs_churn.png
│
└── README.md

 Dataset

Dataset: Telco Customer Churn Dataset

Source: Public telecom customer dataset

Target Variable: Churn (Yes / No)

Key features include:

Tenure

Monthly & Total Charges

Contract type

Payment method

Internet service

 Exploratory Data Analysis (EDA)

EDA includes:

Churn distribution analysis

Churn vs contract type

Monthly charges vs tenure

Simulated cybersecurity risk comparison

Visualizations are saved as PNG files and displayed in the dashboard.

Machine Learning Model

Algorithm: Random Forest Classifier

Preprocessing:

Missing value handling

One-hot encoding

Feature scaling

Class Imbalance Handling: Up-sampling

Model Calibration: CalibratedClassifierCV

Evaluation: Accuracy & classification report

The trained model and preprocessing objects are saved using joblib.

 Streamlit Web Application

The Streamlit app provides:

 Login System

Simple authentication to access the dashboard.

 Churn Prediction

Users input customer details to get:

Churn probability

Retention/churn classification

Adjusted prediction using business logic

 Cyber Risk Score

A simulated risk score based on:

Failed logins

Security alerts

Two-factor authentication

Data breach involvement

 Insights Dashboard

Displays EDA visualizations for better understanding of churn behavior.

 How to Run the Project
1️⃣ Install Dependencies
pip install pandas numpy scikit-learn streamlit matplotlib seaborn joblib pillow

2️⃣ Train the Model (Optional)
python churn_model.py

3️⃣ Generate EDA Visuals (Optional)
python eda_analysis.py

4️⃣ Run the Streamlit App
streamlit run churn_app.py

📌 Use Cases

Customer retention strategy

Business decision support

Data science portfolio project

Academic mini/major project

Interview & placement showcase

 Technologies Used

Python

Pandas, NumPy

Scikit-learn

Matplotlib, Seaborn

Streamlit

Joblib

 Author

Suraj Dias
B.E. Student | Machine Learning & Data Science Enthusiast

GitHub: https://github.com/SurajDias

📜 License

This project is for educational and learning purposes.
