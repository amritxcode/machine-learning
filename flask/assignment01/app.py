from flask import (
    Flask,
    render_template
)

app = Flask(
    __name__
)

@app.route(
    "/"
)

def home():
    return(
        "Welcome to my website"
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/profile/<username>")
def profile(username):
    skills = ["Python", "Flask", "HTML", "Git"]

    return render_template("/profile.html", name=username, my_skills = skills)


if __name__ == "__main__":
    app.run(
        debug = True
    )