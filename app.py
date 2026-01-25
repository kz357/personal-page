from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "title": "Banana phone", 
        "description": "pretend to lose your phone and ask your friend to call it. then pull out a banana and say \"yellow?\" but if you don't have friends you can do this epic prank by yourself with this python file. most important libraries are mediapipe and ultralytics YOLOv8",
        "image": "images/bananapjone.jpg",
        "url": "https://github.com/kz357/banana-phone-sensor"
    },

    {
        "title": "Fraudulent conductor", 
        "description": "A lot of my friends are really good at music but i was chopped at piano and even more chopped at violin. But with js and mediapipe i can now feel better about myself and pretend to be a conductor like I always dreamed of. Spotify api is down but I'll add it when I can.",
        "image": "images/jksimmons.avif",
        "url": "/fraudulent-conductor"
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

@app.route("/fraudulent-conductor")
def fraudulent_conductor():
    return render_template("camera.html")

if __name__ == "__main__":
    app.run(debug=True)