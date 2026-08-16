from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Project</h1>
    <h2>Hello karan singh (changesa)🚀</h2>
    <p>Flask Application Running Successfully.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
