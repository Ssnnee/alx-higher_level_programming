-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT sh.title, g.genre_id
FROM tv_shows AS tsh
JOIN tv_show_genres AS g
    ON tsh.id = g.show_id
ORDER BY tsh.title, g.genre_id;
