import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import joblib

# Load dataset
df = pd.read_csv('Telco-Customer-Churn.csv')

# Clean + prepare
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Add simulated cyber features (for visualization)
np.random.seed(42)
df["FailedLogins"] = np.random.randint(0, 10, len(df))
df["SecurityAlerts"] = np.random.randint(0, 5, len(df))
df["DataBreachNotice"] = np.random.choice([0, 1], size=len(df), p=[0.9, 0.1])

# ---------------------------
# Plot settings
# ---------------------------
sns.set(style="darkgrid")
plt.rcParams["axes.facecolor"] = "#1e272e"
plt.rcParams["figure.facecolor"] = "#1e272e"
plt.rcParams["axes.labelcolor"] = "#d2dae2"
plt.rcParams["xtick.color"] = "#d2dae2"
plt.rcParams["ytick.color"] = "#d2dae2"
plt.rcParams["text.color"] = "#00e6ff"

# ---------------------------
# 1. Churn Distribution
# ---------------------------
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Churn", palette="cool")
plt.title("Churn Distribution (0 = Retained, 1 = Churned)")
plt.tight_layout()
plt.savefig("churn_distribution.png")
plt.close()

# ---------------------------
# 2. Churn by Contract Type
# ---------------------------
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Contract", hue="Churn", palette="Blues")
plt.title("Churn by Contract Type")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("churn_by_contract.png")
plt.close()

# ---------------------------
# 3. Monthly Charges vs Tenure (colored by Churn)
# ---------------------------
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="tenure", y="MonthlyCharges", hue="Churn", palette="coolwarm")
plt.title("Monthly Charges vs Tenure (colored by Churn)")
plt.tight_layout()
plt.savefig("charges_vs_tenure.png")
plt.close()

# ---------------------------
# 4. Cybersecurity Insight — Failed Logins vs Churn
# ---------------------------
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="Churn", y="FailedLogins", palette="flare")
plt.title("Cybersecurity Insight: Failed Logins vs Churn")
plt.tight_layout()
plt.savefig("cyber_vs_churn.png")
plt.close()

print("✅ EDA visualizations generated successfully!")
print("📂 Saved as churn_distribution.png, churn_by_contract.png, charges_vs_tenure.png, cyber_vs_churn.png")
