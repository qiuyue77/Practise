from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", text="")
    elif request.method == "POST":
        text = request.form.get("text")
        return render_template("show.html", text=text)


if __name__ == "__main__":
    app.run(debug=True)
