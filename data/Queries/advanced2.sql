--  SHOW ALL INFO FROM THE TABLE GAMES THAT ARE BEING OFFERED BY THE STORE 'Steam'

SELECT g.*, s.*
FROM games g
INNER JOIN units u
ON g.gameID = u.gameID
INNER JOIN shops s
ON u.store_id = s.store_id
WHERE s.store_name LIKE 'GamersGate'