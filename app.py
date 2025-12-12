from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>Name: Meriam Boukraa</h1>
    <p>Project: My Flask Website</p>
    <p>Version: V1</p>
    <p>Server Hostname: {socket.gethostname()}</p>
    <p>Current Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
