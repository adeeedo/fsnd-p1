#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def results():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    print("\n")
    print("What are the most popular three articles of all time? \n")
    c.execute("""SELECT articles.title, cast(finalview.count AS varchar)
    FROM articles, finalview WHERE articles.slug=finalview.cut
    ORDER BY COUNT DESC LIMIT 3;""")
    row = c.fetchall()
    for r in row:
        print("\"%s \" - %s views" % (r))
    c1 = db.cursor()
    print("\n")
    print("Who are the most popular article authors of all time? ")
    print("\n")
    c1.execute("""select distinct(authorsids.name) ,
     cast(summedviews.sum as varchar) from authorsids ,
      summedviews where authorsids.author=summedviews.author
      order by sum desc;""")
    row1 = c1.fetchall()
    for r1 in row1:
        print("\"%s\" - %s views" % (r1))
    c2 = db.cursor()
    print("\n")
    print("On which days did more than 1% of requests lead to errors? ")
    print("\n")
    c2.execute("""select FORMAT('%s  - %s %%', date , cast(percent as varchar))
     from percentage where percent > 1;""")
    row2 = c2.fetchall()
    for r2 in row2:
        print("\"%s\"" % (r2))
    db.close()


results()
