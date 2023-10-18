-- Lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT sh.title, g.genre_id
FROM tv_shows AS tsh
LEFT JOIN tv_show_genres AS g
    ON tsh.id = g.show_id
WHERE g.genre_id IS NULL
ORDER BY tsh.title, g.genre_id;
