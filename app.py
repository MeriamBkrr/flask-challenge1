from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime
import socket

app = Flask(__name__)


client = MongoClient("mongodb://mongodb:27017/")  
db = client['flask_db']
collection = db['visits']

@app.route("/")
def home():
    name = "Meriam Boukraa"
    project = "NET4255_WebService"
    version = "V2"
    hostname = socket.gethostname()
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    client_ip = request.remote_addr

    collection.insert_one({"ip": client_ip, "date": date_now})

    last_10 = list(collection.find().sort("_id", -1).limit(10))

    html = f"<h1>{project} - {version}</h1>"
    html += f"<p>Nom: {name}</p>"
    html += f"<p>Hostname: {hostname}</p>"
    html += f"<p>Date: {date_now}</p>"
    html += "<h2>Dernières visites :</h2><ul>"
    for record in last_10:
        html += f"<li>{record['date']} - {record['ip']}</li>"
    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

