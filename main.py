from flask import Flask, request
from api import get_posts
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    info = {
        'Home': 'https://scratch-forum.sid72020123.repl.co/',
        'Docs': 'https://github.com/Sid72020123/Scratch-Forums',
        'API': 'https://scratch-forum.sid72020123.repl.co/forum/?topic=:topic&page=:page'
    }
    return json.dumps(info)


@app.route('/forum/', methods=['GET'])
def return_data():
    topic = request.args.get('topic', type=str)
    page = int(request.args.get('page', default=1, type=int))
    return json.dumps(get_posts(topic, page))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)
