USE `hobbyhusetkap2`;



-- Oppgave 1
SELECT 
	*
FROM
	vare
WHERE
	Kategori=UPPER("BØKER") AND "Pris">100
    OR kategori=Upper("KERAMIKK") AND "Pris">100
; 

-- Oppgave 2
SELECT
	VNr, Betegnelse, Pris, ROUND(Pris*1.25,2) AS PrisIncMva
FROM
	vare
;

-- Oppgave 3
SELECT
	VNr, Betegnelse, LEFT(Hylle,1)
FROM
	vare
WHERE 
	Hylle IS NOT NULL
;


-- Oppgave 4
SELECT
	*
FROM
	vare
WHERE
	Pris>=57 AND Pris<=75.50
;

-- Oppgave 5
SELECT
	*
FROM
	vare
WHERE
	Pris BETWEEN 57 AND 75.50
;

-- Oppgave 6
SELECT
	*
FROM
	vare
WHERE
	Betegnelse LIKE "M%"
;

-- Oppgave 7
SELECT
	*
FROM
	vare
WHERE
	Betegnelse LIKE "M_%"
;

-- Oppgave 8
SELECT
	*
FROM
	vare
WHERE
	Betegnelse LIKE "%marsipan%"
;

-- Oppgave 9
SELECT
	*
FROM
	vare
ORDER BY
	Kategori ASC, Pris DESC
;

-- Oppgave 10
SELECT
	ROUND(AVG(Pris),2) AS GjennomsnittPris
FROM
	vare
WHERE
	Kategori = "Fiske"
;

-- Oppgave 11
SELECT
	COUNT("Blomsterfrø"), COUNT("Blomsterløker")
FROM
	vare
WHERE
	Kategori= "Blomsterfrø" OR Kategori= "Blomsterløker"
;

-- Oppgave 12
SELECT
	Kategori
FROM
	vare
GROUP BY
	Kategori
HAVING
	COUNT(Antall)>1
;
