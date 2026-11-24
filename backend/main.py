
from flask import Flask, send_from_directory, request, jsonify
import controller.imgdump as imgdump
app = Flask(__name__, static_folder="../frontend", static_url_path="")
@app.route("/")
def sivusto():
    return send_from_directory("../frontend", "etusivu.html")
@app.route('/viestikanava', methods=['POST'])
def viestimies():
    data = request.get_json()
    match data['lähetysarvo'].split("/")[-1]:
        case "etusivu.html":

            return jsonify(result="<img src= Image_dump/hylics_wayne.gif>")

        case "imgdump.html":

            return jsonify(result=f"{imgdump.imglista()}")
        case "paavalikko.html":
            pass
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)