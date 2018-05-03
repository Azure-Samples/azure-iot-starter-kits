import argparse
import os.path
from flask import Flask, request, redirect, url_for, jsonify
from classification import Classification


FLAGS = None
BOT = None


# Start web server
application = Flask(__name__)

@application.route('/chat', methods=['POST'])
def chat():
    text = request.get_data(as_text=True)
    result = BOT.handle(text)
    return jsonify(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--port',
        type=int,
        default=8080,
        help='Port for http server to listen on.'
    )
    FLAGS, unparsed = parser.parse_known_args()

    # Creates NLP chat bot.
    BOT = Classification()

    application.run(host='0.0.0.0', port=FLAGS.port)
