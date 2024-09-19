-- 2 G.  SHOW THE NUMBER OF GAME TITLES WHOSE FIRST LETTER MATCHES THE FIRST LETTER OF THEIR RESPECTIVE GENRE"

SELECT genre_name, count(g.title) as 'title_count'
FROM games g
INNER JOIN games_genres gr
ON g.gameID = gr.gameID
WHERE LEFT(g.title, 1) = LEFT(genre_name, 1)
GROUP BY genre_name




-- 4 G. SHOW ALL INFO FROM THE TABLE GAMES THAT ARE BEING OFFERED BY THE STORE 'Steam'

SELECT g.*, s.*
FROM games g
INNER JOIN units u
ON g.gameID = u.gameID
INNER JOIN shops s
ON u.store_id = s.store_id
WHERE s.store_name LIKE 'GamersGate'

--5 SHOW TITLE, gameID, store_name and original price OF THE GAMES WHERE THEIR ORIGINAL PRICE IS LOWER THAN THE AVERAGE.

SELECT g.title, u.gameID, s.store_name, u.original_price
FROM games g
INNER JOIN units u
ON g.gameID = u.gameID
INNER JOIN shops s
ON u.store_id = s.store_id
WHERE original_price < (
	SELECT avg(original_price)
    FROM units
) 


-- 7 G SELECT ALL GAMES OF THE SAME GENRE/S AS THE GAME WITH THE HIGHER SCORE AND LOWEST DISCOUNT

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
