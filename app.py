from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "title": "Banana phone", 
        "description": "This is a little python file that i made in october 2025. I like to pretend to lose my phone and have my girlfriend call it before pulling out a and saying \"yellow?\" I like to keep her on her toes. We go to different schools now but despite the distance, she can still stimulate this epic prank. Most important parts are mediapipe and ultralytics YOLOv8",
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