from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('templates/home.html')

@app.route('/about')
def about():
    return render_template('templates/about.html')

if __name__ == '__name__':
    app.run()
