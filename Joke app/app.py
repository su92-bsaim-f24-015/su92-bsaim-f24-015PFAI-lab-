from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    # Fetch random joke from Official Joke API
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        joke = response.json()
        setup = joke.get("setup", "No joke available")
        punchline = joke.get("punchline", "")
    except Exception:
        setup = "Oops! Could not fetch joke."
        punchline = ""

    return render_template("index.html", setup=setup, punchline=punchline)

if __name__ == "__main__":
    app.run(debug=True)