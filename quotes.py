import urllib3
import sqlite3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
url = 'http://quotes.toscrape.com/'
r = http.request("GET", url)
conn = sqlite3.connect("my.sql")
cur = conn.cursor()


tetx = open("crap.txt", "w")
soup = BeautifulSoup(r.data, 'html.parser')
print("Title:")
print(soup.title)
url2 = " "
conn = sqlite3.connect("my.sql")
cur = conn.cursor()
url = 'http://quotes.toscrape.com/'
url1 = 'http://quotes.toscrape.com/'
b = 0
a = 1
c = 1
page = 1
while b == 0:


    print("-" * 5, "Page", page, "-" * 5)
    tetx.write(str("-" * 5) + "Page" + str(page) + str("-" * 5) + "\n")

    http = urllib3.PoolManager()
    r = http.request("GET", url)
    soup = BeautifulSoup(r.data, 'html.parser')

    rez = soup.find_all("div", attrs={"class": "quote"})
    authors = soup.find_all("div", attrs={"class": "quote"})

    for i, quote in enumerate(rez):

        main_text = quote.find("span", attrs={'class': "text"})
        author_text = authors[0].find("small", attrs={'class': "author"})
        print(i + 1, main_text.text[1:-1], "by", author_text.text)
        tetx.write(str(i + 1) + " " + main_text.text[1:-1] + " by " + author_text.text + "\n")




        cur.execute("SELECT id FROM authors WHERE authors = ?", (author_text.text,))
        data = cur.fetchone()

        if data is None:
            cur.execute('insert into authors values (%d,"%s");'
                        % (a, author_text.text))
            cur.execute("select * from authors")
            a += 1
            print(cur.fetchall())



        cur.execute("SELECT id FROM authors WHERE authors = ?", (author_text.text,))
        id_author = cur.fetchone()
        print(id_author[0])



        cur.execute('insert into phrases values(%d, %d, "%s");'
                    %(c, id_author[0], main_text.text[1:-1]))
        cur.execute("select * from phrases")
        c+=1
        print(cur.fetchall())
        conn.commit()


    for next in soup.find_all("li", attrs={"class": "next"}):
        for next1 in next.find_all("a"):
            tt = next.find_all('a', href=True)
            url2 = next1.get('href')
            url = url1 + url2[1::]
            page += 1
    if not next in soup.find_all("li", attrs={"class": "next"}):
        b = 1
        print("All page scraped")
        tetx.close()


