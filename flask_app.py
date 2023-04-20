from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    params = {}
    params["title"] = title
    return render_template('index.html', **params)


@app.route('/training/<prof>')
def training(prof):
    params = {}
    params["profession"] = prof.lower()
    return render_template('training.html', **params)


if __name__ == '__main__':
    app.run(port=8080)
