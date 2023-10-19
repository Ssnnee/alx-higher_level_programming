-- Lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT sh.title
FROM tv_ttshows AS tsh
JOIN tv_show_genres AS relation
    ON tsh.id = relation.show_id
JOIN tv_genres AS gen
    ON gen.id = relation.genre_id
WHERE gen.name = "Comedy"
ORDER BY tsh.title;
