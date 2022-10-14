SELECT Regnr, Merke, Modell 
FROM Bil WHERE NOT EXISTS (
    SELECT * FROM Utleie WHERE Utlevert IS NULL AND Bil.Regnr=Utleie.Regnr)