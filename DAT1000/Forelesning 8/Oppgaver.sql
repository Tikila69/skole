USE hobbyhuset;

SELECT KNr, COUNT(*) AS AntallBestillinger
FROM Ordre
Group By KNr
Having AntallBestillinger>= 10;

CREATE View Gullklubben AS
(
    SELECT KNr, COUNT(*) AS AntallBestillinger
    FROM Ordre
    Group By KNr
    Having AntallBestillinger>= 10
);

SELECT *
FROM Gullklubben;

-- Gullklubblista
SELECT Gullklubben.KNr, Fornavn, Etternavn, Adresse, Kunde.Postnr, Poststed, AntallBestillinger
FROM Gullklubben, Kunde, Poststed
WHERE Gullklubben.Knr=Kunde.KNr
    AND Kunde.Postnr=Poststed.Postnr;

-- Som VIEW
CREATE VIEW Gullklubblista AS
(
    SELECT Gullklubben.KNr, Fornavn, Etternavn, Adresse, Kunde.Postnr, Poststed, AntallBestillinger
    FROM Gullklubben, Kunde, Poststed
    WHERE Gullklubben.KNr=Kunde.KNr
        AND Kunde.Postnr=Poststed.Postnr
);


SELECT *
FROM gullklubblista;

SELECT *
FROM gullklubblista
ORDER BY AntallBestillinger Desc;



-- Oppgave 1: Gullklubblista som en spørring uten VIEW:

SELECT kunde.KNr, Kunde.fornavn, Kunde.Etternavn, Kunde.Adresse, Kunde.Postnr, Poststed.Poststed, COUNT(Ordre.OrdreNr) AS AntallBestillinger
FROM Kunde, Ordre, Poststed
WHERE kunde.Knr=Ordre.Knr AND Kunde.Postnr=Poststed.Postnr
GROUP BY kunde.KNr, Kunde.fornavn, Kunde.Etternavn, Kunde.Adresse, Kunde.Postnr
HAVING AntallBestillinger>=10;


SELECT KNr, COUNT(*) AS AntallBestillinger
FROM Ordre
Group By KNr
Having AntallBestillinger>= 10;

-- Egenkobling

USE Egenkobling;

SELECT AnsNr, Fornavn, Etternavn, Leder
From Ansatt;

--Alle ansatte med navn på leder
SELECT Ansatte.AnsNr, Ansatte.Etternavn, Ansatte.Fornavn, Lederen.Etternavn AS HarSomLeder
FROM Ansatt AS Ansatte, Ansatt AS Lederen
WHERE Ansatte.leder=Lederen.AnsNr 
ORDER BY harSomLeder, Ansatte.Etternavn, Ansatte.Fornavn;


--Oppgave: Lage Spørring som får med de som ikke har leder

SELECT Ansatte.AnsNr, Ansatte.Etternavn, Ansatte.Fornavn, Lederen.Etternavn AS HarSomLeder
FROM Ansatt AS Ansatte LEFT OUTER JOIN Ansatt AS Lederen ON Ansatte.Leder=Lederen.AnsNr
ORDER BY HarSomLeder, Ansatte.Etternavn, Ansatte.Fornavn;


--View for produksjon av salgsrapporter
--Oppgaver: Bruk view'et sammen med andre tabller for å lage ulike salgsrapporter


USE Hobbyhuset;

CREATE VIEW Salg AS (
    SELECT OL.*,V.Betegnelse,K.Navn AS Kategori,O.OrdreDato,O.Knr
    FROM Ordre AS O, Ordrelinje AS OL, Vare AS V, Kategori As K
    WHERE OL.OrdreNr=O.OrdreNr
        AND OL.VNr=V.VNr
        AND V.KatNr=K.KatNr
);

SELECT *
FROM Salg;

