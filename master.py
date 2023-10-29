import threading
import requests
from bs4 import BeautifulSoup
from flask import Flask, request

app = Flask(__name__)


def parse_texts(links: list[str]):
    texts: list[str] = []
    for link in links:
        result = requests.get(link)
        if result.status_code == 200:
            page = BeautifulSoup(result.text, 'html.parser')
            content = page.find('div', class_="post-body entry-content")
            temp_text = ""
            for p in content.findAll('p'):
                temp_text += p.get_text().lower()
            texts.append(temp_text)
    return texts


def words_counter(texts: list[str], slave_link: str, words: dict[str, int]):
    slave_words = requests.get(slave_link, json={'texts': texts})
    if slave_words.status_code == 200:
        for key, value in slave_words.json().items():
            if words.get(key) is None:
                words.setdefault(key, value)
            else:
                words[key] = words[key] + value


@app.route('/master', methods=['POST'])
def master():
    if request.get_json() is None or request.get_json()["links"] is None:
        return 'Error, incorrect links'

    texts = parse_texts(request.get_json()['links'])
    words: dict[str, int] = dict()

    t1 = threading.Thread(target=words_counter,
                          args=[texts[:int(len(texts) / 2)], "http://127.0.0.1:5001/slave1", words])
    t2 = threading.Thread(target=words_counter,
                          args=[texts[int(len(texts) / 2):], "http://127.0.0.1:5002/slave2", words])
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    top_words = []
    for word in reversed(sorted(words.items(), key=lambda item: item[1])):
        if len(top_words) >= 10:
            break
        top_words.append(word)

    return top_words


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
