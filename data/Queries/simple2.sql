-- 2. SHOW THE TITLE OF THE GAMES WHOSE TITLE STARTS BY THE SAME LETTER AS ITS GENRE: 'ARCADE' 

SELECT title
FROM games g
INNER JOIN games_genres gr
ON g.gameID = gr.gameID
WHERE LEFT(g.title, 1) = LEFT('Arcade', 1) AND gr.genre_name LIKE 'Arcade'