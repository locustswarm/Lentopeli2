
from flask import Flask, send_from_directory, request, jsonify
app = Flask(__name__, static_folder="../frontend", static_url_path="")
@app.route("/")
def sivusto():
    return send_from_directory("../frontend", "etusivu.html")
@app.route('/viestikanava', methods=['POST'])
def viestimies():
    data = request.get_json()
    match data['lähetysarvo'].split("/")[-1]:
        case "etusivu.html":

            return jsonify(result=f"{data['lähetysarvo']} on sinun nettiosoite.")

        case "imgdump.html":

            return jsonify(result=f"{data['lähetysarvo']} on sinun nettiosoite.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)