from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def score_server():
    try:
        with open("score.txt", 'r') as file:
            score = file.read()
    except Exception:
        score = "Error: 678"
    return (f"""
    <html>
        <head>
            <title>Score Game</title>
            <link rel="icon" type="image/x-icon" href="{url_for('static', filename='favicon.ico')}">
        </head>
        <body>
            <h1>The score is:</h1>
            <div id="score"> {score} </div>
        </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5254)
