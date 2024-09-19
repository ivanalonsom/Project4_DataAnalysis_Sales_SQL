-- SELECT ALL GAMES OF THE SAME GENRE/S AS THE GAME WITH THE HIGHER SCORE AND LOWEST DISCOUNT

SELECT g.title, g.scores, gr.genre_name, store_name, CASE
	WHEN ROUND(( 100 *  u.discount_price /u.original_price), 2) = 0 THEN 100
    ELSE ROUND(( 100 *  u.discount_price /u.original_price), 2)
END AS 'Discount'
FROM units u
INNER JOIN games g
ON g.gameID = u.gameID
INNER JOIN games_genres gr
ON g.gameID = gr.gameID
INNER JOIN shops s
ON u.store_id = s.store_id
WHERE genre_name IN
(
SELECT gr.genre_name
FROM games_genres gr
WHERE gr.gameID IN (
    SELECT subquery.gameID
    FROM (
        SELECT g.gameID
        FROM games g
        INNER JOIN units u ON g.gameID = u.gameID
        ORDER BY g.scores DESC, (u.discount_price /u.original_price) ASC
        LIMIT 1
    ) AS subquery
))
ORDER BY title ASC