-- List the top 5 highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated
SELECT title FROM movies JOIN ratings ON movie_id = id WHERE id IN
(SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE
name = "Chadwick Boseman")) ORDER BY rating DESC LIMIT 5;
