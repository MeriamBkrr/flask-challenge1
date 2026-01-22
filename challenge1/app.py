from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <html>
        <head>
            <title>NET 4255 - Challenge 1</title>
        </head>
        <body>
            <h1>NET 4255 - High Availability Web Services</h1>
            <p><strong>Name:</strong> Meriam Boukraa</p>
            <p><strong>Project:</strong> Simple Flask Web App</p>
            <p><strong>Version:</strong> V1</p>
            <p><strong>Server hostname:</strong> {hostname}</p>
            <p><strong>Current date:</strong> {current_date}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
