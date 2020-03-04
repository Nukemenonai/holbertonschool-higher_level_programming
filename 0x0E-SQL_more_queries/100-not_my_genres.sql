-- script that uses the database to list all genres of a show
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
     SELECT tv_genres.name AS genres
     FROM tv_genres
     JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
     JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
     WHERE tv_shows.title = 'Dexter') AS dexter_related
ON dexter_related.genres = tv_genres.name
WHERE dexter_related.genres IS NULL
ORDER BY tv_genres.name ASC;
