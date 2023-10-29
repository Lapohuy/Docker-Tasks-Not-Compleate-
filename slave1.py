from flask import Flask, request
from textblob import TextBlob

app = Flask(__name__)


@app.route('/slave1')
def words_counter():
    words: dict[str, int] = dict()
    texts: list[str] = request.json['texts']
    for text in texts:
        for word in TextBlob(text).words:
            if words.get(word) is None:
                words.setdefault(word, 1)
            else:
                words[word] = words[word] + 1
    return words


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
