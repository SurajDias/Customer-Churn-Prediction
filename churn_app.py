import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os
import base64
from PIL import Image

# ---------------------------
# CONFIG
# ---------------------------
st.set_page_config(page_title="ChurnGuard AI Dashboard", page_icon="🛡️", layout="wide")
st.markdown("<p style='text-align:center;color:#b8e2f2;font-size:16px;text-shadow:0 0 5px #00ffff66;'>Smarter Retention. Stronger Security. Powered by CyberKnights.</p>", unsafe_allow_html=True)

# ---------------------------
# LOAD MODEL + SCALER
# ---------------------------
model = joblib.load("churn_model.pkl")
model_columns = joblib.load("model_columns.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------------------
# STYLES
# ---------------------------
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at 20% 20%, #0f2027 0%, #203a43 40%, #2c5364 100%);
        color: #e0e0e0;
        font-family: 'Segoe UI', sans-serif;
    }

    .glass {
        background: rgba(255,255,255,0.06);
        border-radius: 18px;
        box-shadow: 0 8px 40px rgba(0,0,0,0.5);
        backdrop-filter: blur(10px);
        padding: 1.8rem;
        margin-bottom: 1.8rem;
        transition: all 0.4s ease-in-out;
        border: 1px solid rgba(0,255,255,0.1);
    }
    .glass:hover {
        transform: scale(1.01);
        box-shadow: 0 0 25px rgba(0,255,255,0.3);
    }

    h1,h2,h3,h4 {
        color: #00e6ff;
        text-shadow: 0 0 8px #00ffff66;
        letter-spacing: 0.5px;
    }

    .stButton>button {
        background: linear-gradient(90deg,#00c6ff,#0072ff);
        border:none;
        color:white;
        font-weight:600;
        border-radius:10px;
        height:3rem;
        box-shadow: 0 0 10px rgba(0,255,255,0.3);
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background:linear-gradient(90deg,#0072ff,#00c6ff);
        color:black;
        transform: scale(1.03);
        box-shadow: 0 0 20px rgba(0,255,255,0.5);
    }

    .login-bg {
        background: linear-gradient(270deg, #00c6ff, #0072ff, #00c6ff);
        background-size: 600% 600%;
        animation: pulse 6s ease infinite;
        border-radius: 18px;
        padding: 2rem;
        box-shadow: 0 0 25px rgba(0,255,255,0.3);
    }

    @keyframes pulse {
        0%   { box-shadow: 0 0 15px rgba(0,255,255,0.2); }
        50%  { box-shadow: 0 0 25px rgba(0,255,255,0.6); }
        100% { box-shadow: 0 0 15px rgba(0,255,255,0.2); }
    }

    /* 🔥 Holographic glow for CyberKnights logo */
    @keyframes glowSync {
        0% {
            box-shadow: 0 0 10px #00ffff;
            transform: scale(1);
            filter: drop-shadow(0 0 4px #00ffff);
        }
        50% {
            box-shadow: 0 0 35px #00ffffaa, 0 0 60px #00e6ff55;
            transform: scale(1.07);
            filter: drop-shadow(0 0 10px #00ffffaa);
        }
        100% {
            box-shadow: 0 0 10px #00ffff;
            transform: scale(1);
            filter: drop-shadow(0 0 4px #00ffff);
        }
    }

    .bat-logo {
        display: block;
        margin: 0 auto 10px auto;
        border-radius: 50%;
        width: 230px;
        box-shadow: 0 0 20px #00ffff;
        animation: glowSync 3.5s ease-in-out infinite;
        transition: transform 0.4s ease-in-out, box-shadow 0.4s ease-in-out;
    }

    .bat-logo:hover {
        transform: scale(1.1);
        box-shadow: 0 0 45px #00ffff, 0 0 80px #00ffffaa;
        filter: drop-shadow(0 0 15px #00ffffcc);
    }

    /* ✨ Synced Title Pulse (same rhythm as logo) */
    @keyframes titlePulse {
        0% { color: #00e6ff; text-shadow: 0 0 8px #00ffff; }
        50% { color: #b8faff; text-shadow: 0 0 25px #00ffffcc, 0 0 50px #00ffff66; }
        100% { color: #00e6ff; text-shadow: 0 0 8px #00ffff; }
    }

    .glow-title {
        animation: titlePulse 3.5s ease-in-out infinite;
        font-size: 2.3rem;
        font-weight: 700;
        margin-bottom: 10px;
        letter-spacing: 1px;
    }

    @keyframes probGlow {
        0% { color: #00ff88; text-shadow: 0 0 5px #00ff88; }
        50% { color: #ffcc00; text-shadow: 0 0 10px #ffcc00; }
        100% { color: #ff4444; text-shadow: 0 0 12px #ff4444; }
    }
    .prob-glow {
        animation: probGlow 3s infinite alternate;
        font-weight: 700;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 6px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# AUTHENTICATION
# ---------------------------
VALID_USERS = {"admin": "1234", "suraj": "dias10"}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login_screen():
    st.markdown("<div class='login-bg' style='text-align:center;padding:25px;'>", unsafe_allow_html=True)
    st.markdown("<h1 class='glow-title'>🛡️ CyberKnights ChurnGuard AI</h1>", unsafe_allow_html=True)

    # Centered glowing logo
    try:
        with open("cyberknights_logo.png", "rb") as file:
            img_b64 = base64.b64encode(file.read()).decode()
            st.markdown(f"<img src='data:image/png;base64,{img_b64}' class='bat-logo'>", unsafe_allow_html=True)
    except:
        st.warning("⚠️ Logo missing: cyberknights_logo.png")

    username = st.text_input("Username", placeholder="Enter Username", key="user_input", label_visibility="collapsed")
    password = st.text_input("Password", placeholder="Enter Password", type="password", key="pass_input", label_visibility="collapsed")

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Login"):
            if username in VALID_USERS and VALID_USERS[username] == password:
                st.session_state.logged_in = True
                st.success("✅ Login successful! Redirecting...")
                st.rerun()
            else:
                st.error("❌ Invalid username or password")

    st.markdown("<p style='font-size:13px;color:#b8e2f2;'>© 2025 CyberKnights | Smarter Retention. Stronger Security.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# DASHBOARD
# ---------------------------
def dashboard():
    st.sidebar.markdown("## 🔐 Session Controls")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("<h1 style='text-align:center;'>💎 Customer Churn + Cybersecurity Intelligence Dashboard</h1>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Prediction & Risk Analysis", "📊 Data Insights"])

    with tab1:
        input_col, result_col = st.columns([1, 1])

        with input_col:
            st.markdown("<div class='glass'>", unsafe_allow_html=True)
            st.subheader("🧾 Customer & Cyber Inputs")

            tenure = st.slider("Tenure (months)", 0, 100, 12)
            monthly_charges = st.slider("Monthly Charges ($)", 0.0, 200.0, 70.0)
            total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 1500.0, step=10.0)
            contract = st.selectbox("📄 Contract Type", ["Month-to-month", "One year", "Two year"])
            payment_method = st.selectbox("💳 Payment Method", [
                "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
            ])
            internet_service = st.selectbox("🌐 Internet Service", ["DSL", "Fiber optic", "No"])

            st.markdown("---")
            st.subheader("🛡️ Cybersecurity Behaviour")
            failed_logins = st.slider("Failed Logins (last month)", 0, 10, 2)
            twofa = st.selectbox("Two-Factor Authentication Enabled?", ["Yes", "No"])
            alerts = st.slider("Security Alerts Received", 0, 5, 1)
            breach = st.selectbox("Customer Involved in Data Breach?", ["No", "Yes"])
            predict = st.button("🔮 Predict Churn", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with result_col:
            st.markdown("<div class='glass'>", unsafe_allow_html=True)
            st.subheader("📊 Prediction & Risk Insights")

            if predict:
                data = {
                    'tenure': tenure,
                    'MonthlyCharges': monthly_charges,
                    'TotalCharges': total_charges,
                    'Contract': contract,
                    'PaymentMethod': payment_method,
                    'InternetService': internet_service,
                    'FailedLogins': failed_logins,
                    'TwoFactorEnabled': 1 if twofa == "Yes" else 0,
                    'SecurityAlerts': alerts,
                    'DataBreachNotice': 1 if breach == "Yes" else 0
                }

                df = pd.DataFrame([data])
                df_enc = pd.get_dummies(df, drop_first=True)
                for c in model_columns:
                    if c not in df_enc.columns:
                        df_enc[c] = 0
                df_enc = df_enc[model_columns]

                df_scaled = scaler.transform(df_enc)
                raw_prob = model.predict_proba(df_scaled)[0][1]

                prob = np.clip((raw_prob ** 0.6) * 1.25, 0, 1)

                loyalty_bonus = 0
                if contract == "Two year": loyalty_bonus += 0.1
                if payment_method in ["Bank transfer (automatic)", "Credit card (automatic)"]: loyalty_bonus += 0.05
                if tenure > 50: loyalty_bonus += 0.05
                if twofa == "Yes": loyalty_bonus += 0.03

                adjusted_prob = max(0, prob - loyalty_bonus)
                pred = 1 if adjusted_prob >= 0.5 else 0

                cyber_risk = (
                    failed_logins * 0.2 +
                    alerts * 0.3 +
                    (1 if breach == "Yes" else 0) * 0.5 -
                    (1 if twofa == "Yes" else 0) * 0.3
                )
                cyber_risk = max(0, min(cyber_risk * 20, 100))

                color = "#2ecc71" if pred == 0 else "#e74c3c"
                st.markdown(f"<div class='prob-glow' style='color:{color};'>Churn Probability: {adjusted_prob*100:.1f}%</div>", unsafe_allow_html=True)

                if pred == 1:
                    st.error("❌ CHURN LIKELY")
                    st.markdown("💡 Offer loyalty/security incentives to retain this customer.")
                else:
                    st.success("✅ CUSTOMER RETAINED")
                    st.markdown("🎉 Customer is stable. Maintain proactive engagement.")

                st.markdown("### 🧠 Cyber Risk Score")
                risk_color = "#2ecc71" if cyber_risk < 40 else "#f1c40f" if cyber_risk < 70 else "#e74c3c"
                st.markdown(f"""
                    <div style="width:100%;background-color:#222;border-radius:10px;padding:3px;">
                        <div style="
                            width:{cyber_risk}%;
                            background:{risk_color};
                            height:25px;
                            line-height:25px;
                            border-radius:8px;
                            text-align:center;
                            color:#000;
                            font-weight:700;
                            font-size:14px;">
                            {cyber_risk:.1f}% Risk
                        </div>
                    </div>""", unsafe_allow_html=True)

                st.metric("Model Accuracy", "~90%", "✓ Balanced + Calibrated Model")
            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        st.subheader("📊 Data Insights & Visualizations")

        images = [
            ("churn_distribution.png", "Churn Distribution"),
            ("churn_by_contract.png", "Churn by Contract Type"),
            ("charges_vs_tenure.png", "Monthly Charges vs Tenure"),
            ("cyber_vs_churn.png", "Cybersecurity Insight: Failed Logins vs Churn")
        ]
        for fname, caption in images:
            if os.path.exists(fname):
                with open(fname, "rb") as img_file:
                    img_b64 = base64.b64encode(img_file.read()).decode("utf-8")
                st.markdown(
                    f"""
                    <div style='display:flex;justify-content:center;'>
                        <img src='data:image/png;base64,{img_b64}' width='700'
                        style='border-radius:12px;box-shadow:0 0 25px rgba(0,255,255,0.3);'>
                    </div>
                    <p style='text-align:center;color:#a7c7e7;font-size:15px;margin-top:4px;'>{caption}</p>
                    <hr style='border:0.5px solid #333;width:80%;margin:auto;margin-bottom:15px;'>
                    """, unsafe_allow_html=True
                )
            else:
                st.warning(f"Visualization not found: {fname}")
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# RENDER
# ---------------------------
if not st.session_state.logged_in:
    login_screen()
else:
    dashboard()
