from flask import Flask, render_template
import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
url = 'http://quotes.toscrape.com/'

text_author = []

app = Flask("My first Flask application")


def scrap(url, text_author):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    soup = BeautifulSoup(r.data, 'html.parser')
    rez = soup.find_all("div", attrs={"class": "quote"})
    authors = soup.find_all("div", attrs={"class": "quote"})
    for i, quote in enumerate(rez):
        main_text = quote.find("span", attrs={'class': "text"})
        author_text = authors[i].find("small", attrs={'class': "author"})
        text_author.append({"text": main_text.text[1:-1], "author": author_text.text})
    return text_author


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<string:username>")
def user(username):

    return render_template("index_content.html", name=username)


@app.route("/users/<int:page>")
def users(page):
    text = []
    urls = f"http://quotes.toscrape.com/page/{page}"
    author = scrap(urls, text)
    if 1 <= page <= 10:
        ppage = page - 1
        npage = page + 1

    return render_template("index_for.html", items=author, page=page, nextp=npage, previous=ppage)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
