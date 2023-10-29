# Docker Task (not completed yet)
На данный момент проект собран на `Flask` в виде трех веб-приложений.

Парсер текста в `master` работает в  для страниц блога `wod-translator.blogspot.com`

Запросы к `master` отпраляются с помощью утилиты `Postman` и содержат JSON'ы со списоком ссылок на статьи:
```
{"links": [
        "https://wod-translator.blogspot.com/2023/08/blog-post.html",
        "https://wod-translator.blogspot.com/2023/08/blog-post_30.html",
        "https://wod-translator.blogspot.com/2023/01/faq.html"
]}
```
Пример обработанного запроса:


![Пример обработанного запроса:](https://github.com/Lapohuy/Docker-Tasks-Not-Compleate-/assets/61329224/2b8a25b5-15ad-41f1-8ae5-d407f616d809)
