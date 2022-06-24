import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("./db/wta.db")
        self.conn.row_factory = dict_factory
        self.cursor = self.conn.cursor()
