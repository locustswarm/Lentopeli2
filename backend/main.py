from flask import Flask, send_from_directory
app = Flask(__name__, static_folder="../frontend", static_url_path="")
@app.route("/")
def hello_world():
    return send_from_directory("../frontend", "etusivu.html")
if __name__ == "__main__":
    app.run(debug=True)