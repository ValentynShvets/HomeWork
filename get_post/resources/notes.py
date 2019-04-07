from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import use_args, use_kwargs
import urllib3
import sqlite3
from bs4 import BeautifulSoup




class Notes(Resource):
    author_id = {'id': fields.Int(required=True, validate=lambda val: val <= 50), "text": fields.Str(required=True)}



    def get(self):
        base_str = ""
        conn = sqlite3.connect("/Users/valentin/PycharmProjects/MyProject/HomeWork/my.sql")
        cur = conn.cursor()
        cur.execute("select phrases from phrases")
        base = cur.fetchall()
        for phrase in base:
            cur.execute("select id_authors from phrases where phrases = ?", (phrase[0],))
            id_authors = cur.fetchone()
            cur.execute("select authors from authors where id = ?", (id_authors[0],))
            authors = cur.fetchall()
            base_str += f"{phrase[0]} by {authors[0][0]} "
            base_str.split()
        return base_str

    @use_args(author_id)
    def post(self, id_author):
        conn = sqlite3.connect("/Users/valentin/PycharmProjects/MyProject/HomeWork/my.sql")
        cur = conn.cursor()
        for key, value in id_author.items():
            if key == "id":
                ids = value
            if key == "text":
                text = value
        cur.execute("select id from phrases")
        k = len(cur.fetchall()) + 1
        cur.execute('insert into phrases values(%d, %d, "%s");'
                    % (k, ids, text))
        conn.commit()


    #
    # @use_kwargs(another_data)
    # def put(self, val):
    #     return val + 10*10
