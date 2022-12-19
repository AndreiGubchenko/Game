from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)

@app.route('/')
def index():
    GameOfLife(25, 25)
    return render_template('index.html')

@app.route('/live')
def live():
    game = GameOfLife()
    k = 0
    flag = True
    for i in range(len(game.world)):
        if any(game.world[i]):
            k += 1
    if game.counter > 0:
        if k > 0:
            game.form_new_generation()
        else:
            flag = False
    if flag:
        game.counter += 1
    return render_template('live.html', game=game)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)