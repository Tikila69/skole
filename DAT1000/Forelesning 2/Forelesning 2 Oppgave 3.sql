USE `hobbyhusetkap2`;

SELECT
	*
FROM
	vare
WHERE
	Betegnelse LIKE "%,%" AND Betegnelse LIKE "%g" 
    OR Betegnelse LIKE "%stk" AND NOT Betegnelse LIKE "% stk" 
    OR Betegnelse LIKE "%gr"
;