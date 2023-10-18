-- Lists all shows contained in the database hbtn_0d_tvshows.
SELECT sh.title, g.genre_id
FROM tv_shows AS tsh
LEFT JOIN tv_show_genres AS g
    ON tsh.id = g.show_id
ORDER BY tsh.title, g.genre_id;
