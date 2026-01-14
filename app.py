from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "title": "Banana phone", 
        "description": "pretend to lose your phone and ask your friend to call it. then pull out a banana and say \"yellow?\" but if you don't have friends you can do this epic prank by yourself with this python file. most important libraries are mediapipe and ultralytics YOLOv8",
        "image": "images/bananapjone.jpg",
        "url": "https://github.com/kz357/banana-phone-sensor"
    },
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