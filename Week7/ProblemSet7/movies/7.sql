-- List all movies released in 2010 and their raitings, in descending order of rating.
-- If the rating is the same, order them alphabetically by title.
SELECT title, rating FROM movies JOIN ratings ON id = movie_id WHERE year = 2010 ORDER BY rating DESC, title; 
