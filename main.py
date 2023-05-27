# A comment
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello C3 participants! Brought to you by Startfield using Flask.'


app.run(host='0.0.0.0', port=81)
