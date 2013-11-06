"""
Simple HTTP monitoring endpoint for a third party service or another machine to check
"""

from flask import Flask
from process import running
from tradestation import live

app = Flask(__name__)


@app.route("/")
def monitor():
    if running() and live():
        return "pass"
    else:
        return "fail"


if __name__ == "__main__":
    app.run(host='0.0.0.0')