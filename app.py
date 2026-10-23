from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>My Portfolio Website</h1><p>It works!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)