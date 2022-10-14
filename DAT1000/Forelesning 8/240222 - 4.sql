USE Hobbyhuset;

CREATE VIEW Salg AS
(
    SELECT OL.*,V.Betegnelse,K.Navn AS Kategori,O.OrdreDato,O.Knr
    FROM Ordre AS O, Ordrelinje AS OL, Vare AS V, Kategori As K
    WHERE OL.OrdreNr=O.Ordrenr
        AND OL.VNr=V.VNr
        AND V.KatNR=K.KatNr
);

SELECT *
FROM SALG;

SELECT *
FROM ordrelinje;
