from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    title = "Connor Jones's Portfolio"
    return render_template("index.html", title=title)

@app.route('/about')
def about():
    names = ["Connor", "Ian", "Stephen", "John"]
    return render_template("about.html", names=names)


@app.route('/Subscribe')
def subscribe():
    title = "Subscribe to my email newsletter"
    return render_template("subscribe.html", title=title)

@app.route('/form', methods=["post"])
def form():
    First_name = request.form.get("First_name")
    Last_name = request.form.get("Last_name")
    Email = request.form.get("Email")

    

    if not First_name or not Last_name or not Email:
        error_statement = "All form fields required..."
        return render_template("fail.html", error_statement=error_statement)


    title = "Thank You!"
    return render_template("form.html", title=title, First_name=First_name, Last_name=Last_name, Email=Email)