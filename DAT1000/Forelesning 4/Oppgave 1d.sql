USE `oppgave1kap2`;

SELECT
	Tittel
FROM 
	film
WHERE
	Sjanger="Action" OR Sjanger="Western"