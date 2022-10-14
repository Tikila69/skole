USE `??????`;

-- Oppgave 2a
SELECT
	Nr, Beskrivelse
FROM
	Hytte
WHERE
	Ukepris<4500 AND AntallSenger>=4
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
	COUNT(*) AS Antall
FROM
	Hytte
WHERE
	AvstandAlpin<500
;