-- Lists all genres of the show Dexter.
SELECT gen.name
FROM tv_genres AS gen
JOIN tv_show_genres AS relation
    ON gen.id = relation.genre_id
JOIN tv_shows AS tsh
    ON tsh.id = relation.show_id
WHERE tsh.title = "Dexter"
ORDER BY gen.name;
