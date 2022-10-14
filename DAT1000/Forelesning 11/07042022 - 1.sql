USE Storenewton;

SELECT *
FROM bestilling;

SELECT Rom.Romnr, Rom.Romtype
FROM Rom JOIN Bestilling ON Rom.Romnr=Bestilling.Romnr
WHERE bestilling.Fradato<="20220505" AND bestilling.Tildato<="20220505" OR bestilling.Fradato>="20220510" AND bestilling.Tildato>="20220510"
GROUP BY Rom.Romnr, Rom.Romtype;

CREATE VIEW Ledigerom AS(
    SELECT Rom.Romnr, Rom.Romtype
    FROM Rom JOIN Bestilling ON Rom.Romnr=Bestilling.Romnr
    WHERE bestilling.Fradato<="20220505" AND bestilling.Tildato<="20220505" OR bestilling.Fradato>="20220510" AND bestilling.Tildato>="20220510"
    GROUP BY Rom.Romnr, Rom.Romtype
);
SELECT *
FROM Ledigerom;

SELECT *
FROM rom
WHERE NOT EXISTS(
    SELECT *
    FROM bestilling
    WHERE Bestilling.Romnr=rom.Romnr
    );


