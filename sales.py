import sqlite3 as lite
import sys

sales = (
    ('John', 2000),
    ('Ron', 23000),
    ('Jessica', 3000),
    ('Snow', 2400),
    ('Bunny', 20500),
    ('Penny', 25000),
    ('Tyrel', 20600),
    ('William', 27000),
    ('Allena', 20050)
    )
con = lite.connect('sales.db')

with con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS reps')
    cur.execute('CREATE TABLE reps(rep_name TEXT, amount INT)')
    cur.executemany('INSERT INTO reps VALUES(?, ?)', sales)