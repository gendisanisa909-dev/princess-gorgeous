from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my website!"

@app.route("/rahasia")
def rahasia():
    riddles = [
        "punya jarum tapi tidak bisa menjahit? pasti Jam dong.",
        "semakin diisi semakin ringan? tentu Balon.",
        "punya kaki tetapi tidak bisa berjalan? ya! Meja."
    ]

    return f"""
    <html>
    <head>
        <title>Halaman Rahasia</title>
    </head>
    <body>
        <h1>🔐 Welcome to Secret Page!</h1>
        <h2>{random.choice(riddles)}</h2>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)