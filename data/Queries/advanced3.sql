-- SHOW TITLE, gameID, store_name and original price OF THE GAMES WHERE THEIR ORIGINAL PRICE IS LOWER THAN THE AVERAGE.

SELECT g.title, u.gameID, s.store_name, u.original_price
FROM games g
INNER JOIN units u
ON g.gameID = u.gameID
INNER JOIN shops s
ON u.store_id = s.store_id
WHERE original_price < (
	SELECT avg(original_price)
    FROM units
	);