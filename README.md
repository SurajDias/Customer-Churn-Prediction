# Customer Churn Prediction System

An end-to-end Machine Learning project that predicts whether a customer is likely to churn (leave a service) using historical data.  
The project includes data analysis, model training, and an interactive Streamlit web application for real-time predictions and insights.

---

## Project Overview

Customer churn is a critical business problem where companies lose customers to competitors.  
This project aims to:

- Analyze customer behavior patterns  
- Predict churn probability using Machine Learning  
- Visualize insights using Exploratory Data Analysis (EDA)  
- Provide an interactive dashboard for decision-making  

---

## Features

- Exploratory Data Analysis (EDA) with visual insights  
- Machine Learning model using Random Forest with calibration  
- Class imbalance handling using up-sampling  
- Feature scaling and one-hot encoding  
- Streamlit web application for live predictions  
- Simple login authentication system  
- Cyber-risk score simulation using extended feature logic  

---

## Project Structure

Customer-Churn-Prediction/
│
├── Telco-Customer-Churn.csv # Dataset
├── churn_model.py # Model training and saving
├── eda_analysis.py # Exploratory data analysis and visualization
├── churn_app.py # Streamlit web application
│
├── churn_model.pkl # Trained machine learning model
├── model_columns.pkl # Model feature columns
├── scaler.pkl # StandardScaler object
│
├── churn_distribution.png
├── churn_by_contract.png
├── charges_vs_tenure.png
├── cyber_vs_churn.png
│
└── README.md


---

## Dataset

- Dataset: Telco Customer Churn Dataset  
- Source: Public telecom customer dataset  
- Target Variable: Churn (Yes / No)

Key features include:
- Tenure  
- Monthly and Total Charges  
- Contract type  
- Payment method  
- Internet service  

---

## Exploratory Data Analysis (EDA)

EDA includes:
- Churn distribution analysis  
- Churn versus contract type  
- Monthly charges versus tenure  
- Simulated cybersecurity risk comparison  

Visualizations are saved as PNG files and displayed in the Streamlit dashboard.

---

## Machine Learning Model

- Algorithm: Random Forest Classifier  

Preprocessing steps:
- Missing value handling  
- One-hot encoding  
- Feature scaling  

Additional techniques:
- Class imbalance handling using up-sampling  
- Model calibration using CalibratedClassifierCV  

Evaluation:
- Accuracy  
- Classification report  

The trained model and preprocessing objects are saved using joblib.

---

## Streamlit Web Application

The Streamlit app provides the following functionalities:

### Login System
Simple authentication to access the dashboard.

### Churn Prediction
Users input customer details to obtain:
- Churn probability  
- Retention or churn classification  
- Adjusted prediction using business logic  

### Cyber Risk Score
A simulated risk score based on:
- Failed logins  
- Security alerts  
- Two-factor authentication  
- Data breach involvement  

### Insights Dashboard
Displays EDA visualizations for better understanding of customer churn behavior.

---

## How to Run the Project

### 1. Install Dependencies
```bash
pip install pandas numpy scikit-learn streamlit matplotlib seaborn joblib pillow


Train the Model 
python churn_model.py

Generate EDA Visuals 
python eda_analysis.py

Run the Streamlit Application
streamlit run churn_app.py

###Use Cases

Customer retention strategy

Business decision support

Data science portfolio project

Academic mini or major project

Interview and placement showcase

###Technologies Used

Python

Pandas, NumPy

Scikit-learn

Matplotlib, Seaborn

Streamlit

Joblib

##Author

Suraj Dias
B.E. Student | Machine Learning and Data Science Enthusiast

GitHub: https://github.com/SurajDias

##License

This project is for educational and learning purposes.


