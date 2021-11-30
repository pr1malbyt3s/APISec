from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('settings.py')

@app.route('/')
def hello():
    return {'hello':'world'}

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9000)