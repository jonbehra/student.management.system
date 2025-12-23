from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# DATABASE (e njëjta logjikë)
listStd = ["yugesh", "kishor", "gajen", "Gopi"]

@app.route("/")
def index():
    return render_template("index.html", students=listStd)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    if name and name not in listStd:
        listStd.append(name)
    return redirect(url_for("index"))

@app.route("/delete/<name>")
def delete_student(name):
    if name in listStd:
        listStd.remove(name)
    return redirect(url_for("index"))

@app.route("/search", methods=["POST"])
def search_student():
    name = request.form["name"]
    found = name in listStd
    return render_template("index.html", students=listStd, result=found, search=name)

if __name__ == "__main__":
    app.run(debug=True)
