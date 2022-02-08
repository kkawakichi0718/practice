import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return "こんにちは！川北圭祐です！"


if __name__ == '__main__':
    app.run(debug=True)
