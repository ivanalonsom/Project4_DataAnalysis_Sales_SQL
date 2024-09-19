-- SHOW THE NUMBER OF GAME TITLES WHOSE FIRST LETTER MATCHES THE FIRST LETTER OF THEIR RESPECTIVE GENRE"

SELECT genre_name, count(g.title) as 'title_count'
FROM games g
INNER JOIN games_genres gr
ON g.gameID = gr.gameID
WHERE LEFT(g.title, 1) = LEFT(genre_name, 1)
GROUP BY genre_name
