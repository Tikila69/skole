USE gruppering2022;

SELECT
	*
FROM
	Ansatt;


SELECT
	Stillingskode,Lønnstrinn
FROM
	Ansatt
GROUP BY
	Stillingskode,Lønnstrinn
ORDER BY
	Stillingskode;
    

SELECT
	Stillingskode,Lønnstrinn,COUNT(*) AS Ansatte
FROM
	Ansatt
GROUP BY 
	Stillingskode,Lønnstrinn
ORDER BY
	Stillingskode;
