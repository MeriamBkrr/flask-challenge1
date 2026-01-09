from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <h1>Challenge 4 - Flask WITHOUT DB</h1>
    <p><b>Name:</b> Meriam Boukraa</p>
    <p><b>Project:</b> NET4255</p>
    <p><b>Version:</b> V3-NODB</p>
    <p><b>Hostname:</b> {hostname}</p>
    <p><b>Date:</b> {now}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
