views:
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
SELECT totalrequests.date,
       totalrequests.count AS total,
       failedrequests.count AS failed,
       failedrequests.count*100/totalrequests.count AS percent
FROM totalrequests,
     failedrequests
WHERE totalrequests.date=failedrequests.date ;