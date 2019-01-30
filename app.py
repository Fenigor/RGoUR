from flask import Flask, render_template
from flask import request
from engine import rg_of_ur


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # init a game class
    if request.method == 'POST':
        pass
        # blue_player_position = request.form['blue']
        # red_player_position = request.form['red']
        # term = request.form['term']
        # load the game instance with the post data
        # game.init_state(blue_player_position, red_player_position, term)
    else:
        pass # no move, the game just starts
        # delete this part of the logic
    # game.trow_dices()
    # template_params = game.state()
    return render_template('home.html') # add template_params as param to templete renderer

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
