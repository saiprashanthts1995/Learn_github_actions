from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This Sai Prashanth T S. Alright, Starting from the scratch"


if __name__ == "__main__":
    app.run()
