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
;


-- Oppgave 2a
SELECT
	Nr, Beskrivelse
FROM
	Hytte
WHERE
	Ukepris<450 AND AntallSenger>=4
;

-- Oppgave 2b
SELECT
	*
FROM
	Hytte
WHERE
	Strøm="J" AND Dusj="J"
ORDER BY
	Ukepris ASC
;

-- Oppgave 2c
SELECT
	COUNT(AntallHytter) AS "2Sengeplasser"
FROM
	Hytte
WHERE
	COUNT(AntallSenger)=2
;

-- Oppgave 2d
SELECT
	AVG(Pris)
FROM
	Hytte
WHERE
	AntallSenger=4
;

-- Oppgave 2e
SELECT
	COUNT(Nr) AS Antall
FROM
	Hytte
WHERE
	AvstandAlpin<500
;

