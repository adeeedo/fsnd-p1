

import psycopg2

DBNAME = "news"

def results():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(" select articles.title , finalview.count from articles , finalview where articles.slug=finalview.cut order by count desc limit 3;")
  posts = c.fetchall()
  print("\n")
  print("first question : ")
  print("\n")
  print( posts)
  print("\n")
  c1= db.cursor()
  c1.execute(" select distinct(authorsids.name) , summedviews.author , summedviews.sum from authorsids , summedviews where authorsids.author=summedviews.author order by sum desc;")
  posts1 = c1.fetchall()
  print("\n")
  print("second question : ")
  print("\n")
  print(posts1)
  c2= db.cursor()
  c2.execute("  select date, percent from percentage where percent > 1;")
  posts2 = c2.fetchall()
  print("\n")
  print("third question : ")
  print("\n")
  print(posts2)
  db.close()

results()

