from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime
import socket

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/")
db = client["challenge4_db"]
collection = db["visits"]

@app.route("/")
def home():
    hostname = socket.gethostname()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client_ip = request.remote_addr

    collection.insert_one({
        "ip": client_ip,
        "date": now,
        "server": hostname
    })

    visits = list(collection.find().sort("_id", -1).limit(10))

    html = f"""
    <h1>Challenge 4 - Flask WITH DB</h1>
    <p><b>Name:</b> Meriam Boukraa</p>
    <p><b>Project:</b> NET4255</p>
    <p><b>Version:</b> V3-DB</p>
    <p><b>Hostname:</b> {hostname}</p>
    <p><b>Date:</b> {now}</p>
    <h2>Last 10 visits</h2>
    <ul>
    """

    for v in visits:
        html += f"<li>{v['date']} - {v['ip']} - {v['server']}</li>"

    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
