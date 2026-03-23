from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    print("🚀 Jump Counter → http://127.0.0.1:55812/")
    app.run(debug=False)
