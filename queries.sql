-- 1. SHOW THE NAME AND SCORE OF THE TOP 3 RATED GAMES WHOSE GENRE IS 'ACTION'
SELECT DISTINCT title, scores
FROM games g
INNER JOIN games_genres gr
ON g.gameID = gr.gameID
WHERE genre_name LIKE 'Action'
ORDER BY scores DESC
LIMIT 3


-- 2. SHOW THE AMOUNT OF TITLES OF THE GAMES WHOSE FIRST LETTER STARTS WITH THE FIRST LETTER OF THE GENRE THEY BELONG TO
SELECT genre_name, count(g.title) as 'title_count'
FROM games g
INNER JOIN games_genres gr
ON g.gameID = gr.gameID
WHERE LEFT(g.title, 1) = LEFT(genre_name, 1)
GROUP BY genre_name


-- 3. SHOW THE TITLE OF THE GAME WHOSE TITLE STARTS BY THE SAME LETTER AS ITS GENRE: 'ARCADE' 
SELECT title
FROM games g
INNER JOIN games_genres gr
ON g.gameID = gr.gameID
WHERE LEFT(g.title, 1) = LEFT('Arcade', 1) AND gr.genre_name LIKE 'Arcade'
