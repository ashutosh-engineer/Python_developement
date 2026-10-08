from flask import Flask, render_template, request

app = Flask(__name__, template_folder=".")


@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def get_data():
    name = request.form.get("name")
    email = request.form.get("email")

    return render_template("form.html", name=name, email=email)


if __name__ == "__main__":
    app.run(debug=True)
