# Customer Churn Intelligence Dashboard

An interactive Streamlit application that predicts telecom customer churn using a calibrated machine learning model, with support for both single-customer lookups and batch scoring across uploaded datasets.


---

## Why This Project

Churn prediction is only useful if the output means something. Most churn models report a raw classifier score, which doesn't behave like a real probability. This project focuses on producing **calibrated, probability-like risk scores** and keeping training/inference feature alignment consistent — two things that are easy to get subtly wrong in an ML pipeline.

---

## Core Features

### 🤖 Churn Prediction Engine
- **Class-balanced training** — addresses real class imbalance (73.5% retained / 26.5% churned) via oversampling
- **Sigmoid-calibrated Random Forest** (400 trees × 5 calibration folds) — chosen specifically so `predict_proba` outputs behave like real probabilities, not just ranking scores
- **Feature-schema persistence** — the exact one-hot encoded column order is serialized alongside the model, so any new input (single customer or batch CSV) is deterministically aligned to the training schema before scoring

### 📊 Interactive Dashboard (4 Tabs)
1. **Single-Customer Prediction** — instant churn risk score for one customer record
2. **Data Insights** — exploratory visualizations (churn distribution, churn by contract type, tenure vs. charges)
3. **Batch Prediction** — upload a CSV, get back churn scores for every row, with downloadable CSV/PDF reports
4. **About** — model and methodology overview

---

## Tech Stack

| Layer | Technologies |
|---|---|
| App/UI | Streamlit |
| ML | scikit-learn (Random Forest, CalibratedClassifierCV, StandardScaler) |
| Data | pandas, NumPy |
| Reporting | ReportLab (PDF export), matplotlib, seaborn |
| Persistence | Joblib (model/scaler/schema serialization) |

---

## Architecture

```
Telco Customer CSV
      │
      ▼
Clean → One-Hot Encode → Oversample (balance classes) → Stratified Split
      │
      ▼
StandardScaler → Random Forest (400 trees) → Sigmoid Calibration
      │
      ▼
Serialized: model.pkl + feature_schema.pkl + scaler.pkl
      │
      ▼
Streamlit App ── aligns new input to schema ── scores via calibrated model
```

---

## What Makes This Technically Interesting

The core engineering problem this project solves is **train/inference consistency**: a one-hot encoded feature matrix is only valid if every column matches the exact order the model was trained on. Persisting the feature-schema list alongside the model and scaler — then reindexing any new input against it — prevents a whole class of silent, hard-to-debug prediction errors that happen when encoding is redone independently at inference time.

Sigmoid calibration was a deliberate choice over using raw Random Forest vote fractions, since tree-ensemble scores don't naturally behave like probabilities without calibration — this makes the output more meaningful for a risk-communication use case like churn scoring.

---

## Known Limitations

This is a learning-focused ML project, not a production scoring service:
- Reported accuracy metrics were computed on a resampled dataset and should be treated as directional, not a production-validated benchmark — proper held-out evaluation before oversampling is a planned improvement
- Single-customer predictions currently rely on a subset of the full feature set; expanding the input form to cover the complete training schema is a planned improvement
- No persistent database — batch data and predictions are processed in-memory per session

---

## Getting Started

```bash
pip install -r requirements.txt

# Train the model (optional — pretrained artifacts included)
python churn_model.py

# Run the app
streamlit run churn_app.py
```

---

## License

MIT
