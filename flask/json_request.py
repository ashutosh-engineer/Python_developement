from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def main():
    data = request.get_json()
    if not isinstance(data, dict):
        return {"error": "Request body must be a JSON object"}, 400

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    return f"{name} , {age} , {course}"


if __name__ == "__main__":
    app.run(debug=True)
