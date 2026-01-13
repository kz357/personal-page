from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "title": "Banana phone", 
        "description": "This is a little python file that i made in october 2025. Every once in a while, I pretend to lose my phone and have my girlfriend call it before taking a banana out of my back pocket and answering \"yellow?\" It keeps her on her toes. We go to different schools but despite the distance, she can now get hit with this epic prank.",
        "image": "images/bananapjone.jpg",
        "url": "https://github.com/kz357/banana-phone-sensor/tree"
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