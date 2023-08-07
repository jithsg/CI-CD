from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return Hello, World! on the index route."""
    return "Hello, World!"  # Fixed indentation here


if __name__ == "__main__":
    app.run(host="0.0.0.0")
