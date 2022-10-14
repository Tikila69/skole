USE Hobbyhuset;

SELECT *
FROM kunde
WHERE NOT EXISTS (
    SELECT KNr FROM Ordre WHERE KUNDE.KNr=Ordre.KNr
);

SELECT *
FROM kunde
WHERE EXISTS (
    SELECT Knr FROM Ordre Where Kunde.KNr=Ordre.knr
);