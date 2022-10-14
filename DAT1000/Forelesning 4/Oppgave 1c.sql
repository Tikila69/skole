USE `oppgave1kap2`;

SELECT
	*
FROM 
	film
WHERE
	Sjanger="Komedie" 
    AND Alder < 10 
    AND Tid < 130