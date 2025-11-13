
from flask import Flask, render_template, request, redirect, jsonify
import os
import traceback
import signal

app = Flask(__name__)

VALID_USERS = {"suraj": "dias10", "admin": "1234"}

# -------------------------------
# HOME (Login Page)
# -------------------------------
@app.route('/')
def home():
    try:
        return render_template('login.html')
    except Exception as e:
        return f"<pre style='color:red;'>Error rendering login.html: {e}</pre>"

# -------------------------------
# LOGIN HANDLER
# -------------------------------
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']

        if username in VALID_USERS and VALID_USERS[username] == password:
            # ✅ Kill any old Streamlit instances
            os.system("pkill -f 'streamlit run cyber_app.py'")

            # ✅ Launch Streamlit silently
            os.system("nohup streamlit run cyber_app.py --server.port 8502 >/dev/null 2>&1 &")

            # ✅ Same-tab redirection (JS trick)
            return """
            <script>
            window.location.replace("http://127.0.0.1:8502");
            </script>
            """
        else:
            return """
            <div style='text-align:center;'>
                <h3 style='color:red;'>❌ Invalid credentials. Try again.</h3>
                <a href='/' style='color:#00e6ff;'>Go Back</a>
            </div>
            """
    except Exception as e:
        return f"<pre style='color:red;'>Error during login: {traceback.format_exc()}</pre>"

# -------------------------------
# LOGOUT HANDLER (called by Streamlit)
# -------------------------------
@app.route('/logout', methods=['POST'])
def logout():
    try:
        os.system("pkill -f 'streamlit run cyber_app.py'")
        return jsonify({"status": "success", "message": "Streamlit server stopped"}),200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}),500

# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8600, debug=True)
