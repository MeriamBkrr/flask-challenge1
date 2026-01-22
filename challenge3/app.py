from flask import Flask, request
from pymongo import MongoClient
import socket
from datetime import datetime

app = Flask(__name__)

# MongoDB connection (via docker-compose service name)
client = MongoClient("mongodb://admin:admin123@mongodb:27017/")
db = client.net4255
collection = db.logs

@app.route("/")
def home():
    hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client_ip = request.remote_addr

    # Insert record for each request
    collection.insert_one({
        "client_ip": client_ip,
        "date": current_date
    })

    # Get last 10 records
    last_records = collection.find().sort("_id", -1).limit(10)

    records_html = ""
    for record in last_records:
        records_html += f"<li>{record['client_ip']} - {record['date']}</li>"

    return f"""
    <html>
        <head>
            <title>NET 4255 - Challenge 3</title>
        </head>
        <body>
            <h1>NET 4255 - High Availability Web Services</h1>
            <p><strong>Name:</strong> Meriam Boukraa</p>
            <p><strong>Project:</strong> Flask + MongoDB Web Service</p>
            <p><strong>Version:</strong> V2</p>
            <p><strong>Server hostname:</strong> {hostname}</p>
            <p><strong>Current date:</strong> {current_date}</p>

            <h2>Last 10 requests</h2>
            <ul>
                {records_html}
            </ul>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
