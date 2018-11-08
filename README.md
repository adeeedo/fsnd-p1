The project analyzes a log from an articles website, running this program will answer three question:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 

to tun the code, you must install virtual box, vagrant 
my test versions are : 
virtual box 5.2.20
vagrant 2.2.0

donwload https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
and move the file into vagrant directory 
start virtual machine, cd into vagrant folder and in bash comman line run
vagrant up 
it'll take some time if this is the first time to run it.
and then :

vagrant ssh 
cd /vagrant 
psql -d news -f newsdata.sql


These are the views I created to query the database, run those lines to create them, 



CREATE VIEW cutpath AS
SELECT substring(path,10) AS cut,
       status
FROM log 
WHERE (status = '200 OK'::text);






CREATE VIEW finalview AS
SELECT cut,
       status,
       count(cut)
FROM cutpath
WHERE cut!=''
GROUP BY cut,
         status;





CREATE VIEW authorsids AS
SELECT articles.author,
       authors.name
FROM articles,
     authors
WHERE authors.id = articles.author;



CREATE VIEW summedviews AS
SELECT articles.author,
       sum(finalview.count) AS SUM
FROM public.articles,
     public.finalview
WHERE (articles.slug = finalview.cut)
GROUP BY articles.author;



CREATE VIEW failedrequests AS
SELECT date(TIME),
       count(status)
FROM log
WHERE status !='200 OK'
GROUP BY date(TIME)
ORDER BY date(TIME);




CREATE VIEW totalrequests AS
SELECT date(TIME),
       count(status)
FROM log
GROUP BY date(TIME);





CREATE VIEW percentage AS
SELECT TO_CHAR(totalrequests.date, 'Mon DD, YYYY') AS date,
       totalrequests.count AS total,
       failedrequests.count AS failed,
       round(failedrequests.count*100.0/totalrequests.count,2) AS percent
FROM totalrequests,
     failedrequests
WHERE totalrequests.date=failedrequests.date ;





\q if you're done with exploring the database.

download project1.py from my github https://github.com/adeeedo/fsnd-p1 to run the python file type:
python project1.py 

* note you have to be running vagrant and inside /vagrant 
