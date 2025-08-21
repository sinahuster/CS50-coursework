-- List all the names of people who have starred in movies also starred in by Kevin Bacon
SELECT name FROM people WHERE id IN (SELECT person_id FROM stars WHERE movie_id IN
(SELECT id FROM movies WHERE id IN (SELECT movie_id FROM stars WHERE person_id =
(SELECT id FROM people WHERE name = "Kevin Bacon")))) AND name <> "Kevin Bacon";
