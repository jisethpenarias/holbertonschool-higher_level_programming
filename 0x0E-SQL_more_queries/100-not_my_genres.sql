-- Results must be sorted in ascending order by the genre name.
SELECT tv_genres.name
FROM tv_genres
WHERE `name` NOT IN (
    SELECT tv_genres.name
    FROM tv_shows
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_shows.title = "Dexter"
    )
ORDER BY tv_genres.name ASC;
