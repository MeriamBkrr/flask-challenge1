from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("WEBDB_VERSION", "N/A")  # <- Lecture de la variable d'env
    return render_template("index.html", version=version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
