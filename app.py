from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# -----------------------------
# MySQL Configuration
# -----------------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shayswife@1258547",   # <-- Replace with your MySQL password
    database="shaysagt"
)

cursor = db.cursor(dictionary=True)

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Admin Page
# -----------------------------
@app.route("/admin")
def admin():
    return render_template("admin.html")


# -----------------------------
# Test Database Connection
# -----------------------------
@app.route("/test")
def test():
    try:
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        return {
            "status": "Connected Successfully",
            "server_time": str(result["NOW()"])
        }
    except Exception as e:
        return {
            "status": "Database Connection Failed",
            "error": str(e)
        }


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)