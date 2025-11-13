import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils.class_weight import compute_class_weight
from sklearn.utils import resample

# ---------------------------
# LOAD & CLEAN DATA
# ---------------------------
data = pd.read_csv('Telco-Customer-Churn.csv')
print("Data loaded:", data.shape)

# Remove customerID (non-numeric unique field)
if 'customerID' in data.columns:
    data.drop('customerID', axis=1, inplace=True)

# Convert TotalCharges to numeric and handle missing
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data['TotalCharges'] = data['TotalCharges'].fillna(data['TotalCharges'].median())

# Encode target column
data['Churn'] = data['Churn'].map({'Yes': 1, 'No': 0})

# One-hot encode categorical features
data = pd.get_dummies(data, drop_first=True)

# ---------------------------
# BALANCING THE DATASET
# ---------------------------
churned = data[data['Churn'] == 1]
retained = data[data['Churn'] == 0]

# Oversample churned class (to about 50-50)
churned_upsampled = resample(churned,
                             replace=True,
                             n_samples=len(retained),
                             random_state=42)
balanced_data = pd.concat([retained, churned_upsampled])
balanced_data = balanced_data.sample(frac=1, random_state=42).reset_index(drop=True)

print("Balanced data shape:", balanced_data.shape)

# ---------------------------
# SPLIT + SCALE
# ---------------------------
X = balanced_data.drop('Churn', axis=1)
y = balanced_data['Churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---------------------------
# CLASS BALANCING WEIGHTS
# ---------------------------
weights = compute_class_weight(
    class_weight='balanced', classes=np.array([0, 1]), y=y_train
)
class_weights = {0: weights[0], 1: weights[1]}
print("Class weights:", class_weights)

# ---------------------------
# MODEL TRAINING + CALIBRATION
# ---------------------------
base_model = RandomForestClassifier(
    n_estimators=400,
    max_depth=14,
    random_state=42,
    class_weight=class_weights
)

calibrated_model = CalibratedClassifierCV(base_model, method='sigmoid', cv=5)
calibrated_model.fit(X_train_scaled, y_train)

# ---------------------------
# EVALUATION
# ---------------------------
y_pred = calibrated_model.predict(X_test_scaled)
y_prob = calibrated_model.predict_proba(X_test_scaled)[:, 1]

# Stretch probabilities for smoother range (visual realism)
y_prob_adjusted = np.clip(0.8 * y_prob + 0.1, 0, 1)

acc = accuracy_score(y_test, y_pred)
print(f"\n✅ Balanced + Calibrated Model trained successfully! Accuracy: {acc:.3f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ---------------------------
# SAVE MODEL + OBJECTS
# ---------------------------
joblib.dump(calibrated_model, "churn_model.pkl")
joblib.dump(list(X.columns), "model_columns.pkl")
joblib.dump(scaler, "scaler.pkl")

print("\n🎯 All files saved: churn_model.pkl, model_columns.pkl, scaler.pkl (Balanced + Calibrated)")
