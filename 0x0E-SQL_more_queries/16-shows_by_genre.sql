-- Lists all shows, and all genres linked to that show
SELECT sh.title, gen.name
FROM tv_shows AS tsh
LEFT JOIN tv_show_genres AS relation
    ON tsh.id = relation.show_id
LEFT JOIN tv_genres AS gen
    ON gen.id = relation.genre_id
ORDER BY tsh.title, gen.name;
