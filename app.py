from flask import Flask, render_template
from flask import request
import requests
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/complete", methods=["POST"])
def move_complete():
    name = request.form.get("name")
    email = request.form.get("email")
    datetime = request.form.get("datetime")

    url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScNkBYMgWRGm6cKjA3YVp10SpiqyMlqAilKOqBifaBDo1DMmw/formResponse"
    params = {
        "entry.1498135098": name,
        "entry.567211892": email,
        "entry.1238054153": datetime
    }
    r = requests.get(url, params=params)

    return render_template("complete.html", name=name, email=email, datetime=datetime, r=r)
    # return render_template("complete.html", name=name, email=email, datetime=datetime)


if __name__ == '__main__':
    app.run()
