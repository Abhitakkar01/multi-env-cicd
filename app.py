import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("ENV_NAME", "UNKNOWN")
    return f"<h1>Hello from {env}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
