-- Returns the average energy of all of Drake's songs
SELECT AVG(energy) FROM songs WHERE artist_id = (SELECT id FROM artists WHERE name = "Drake");
