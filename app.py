from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {"title": "Project One", "description": "What it does"},
    {"title": "Project Two", "description": "Another project"},
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)