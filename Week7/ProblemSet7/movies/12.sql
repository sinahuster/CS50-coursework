-- List the titles of movies that starred both Bradley Cooper and Jennifer Lawrence
SELECT title FROM movies WHERE id IN (SELECT movie_id FROM stars WHERE person_id =
(SELECT id FROM people WHERE name = 'Jennifer Lawrence')) AND id IN (
SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Bradley Cooper'));
