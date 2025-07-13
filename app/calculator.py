from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Calculator Backend"

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return jsonify({"error": "Missing input"}), 400

    try:
        result = float(num1) + float(num2)
    except ValueError:
        return jsonify({"error": "Invalid numbers"}), 400

    return jsonify({"result": result}), 200

@app.route("/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Missing input"}), 400

    try:
        result = float(a) - float(b)
    except ValueError:
        return jsonify({"error": "Invalid Input"}), 400
    return jsonify({"result": result}), 200

@app.route("/multiplication", methods=["POST"])
def multiplication():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Missing input"}), 400

    try:
        result = float(a) * float(b)
    except ValueError:
        return jsonify({"error": "Invalid Input"}), 400
    return jsonify({"result": result}), 200

@app.route("/div", methods=["POST"])
def division():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Missing input"}), 400

    try:
        result = float(a) / float(b)
    except ValueError:
        return jsonify({"error": "Invalid Input"}), 400
    return jsonify({"result": result}), 200


if __name__ == "__main__":
    app.run(debug=True)