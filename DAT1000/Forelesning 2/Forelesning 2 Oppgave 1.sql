USE `Oppgave1kap2`;

SELECT
	*
FROM
	film
;

-- Oppgave 1g
SELECT
	COUNT(Tittel) AS FilmerIkkeTilSalgs
FROM
	film
WHERE
	Pris IS NULL
;
    
-- Oppgave 1h
SELECT
	COUNT(Tittel) AS Billigfilmer
FROM
	film
WHERE
	Pris<100
;

-- Oppgave 1i
SELECT
	Tittel
FROM
	film
WHERE
	Tittel LIKE "%now"