from flask import Flask
from flask import render_template
from flask import request

from graph import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    player1 = request.form['player1']
    player2 = request.form['player2']

    return render_template('result.html', player1=player1, player2=player2, deg=shortest_path(player1, player2))

if __name__ == "__main__":
    app.run(debug=True)
