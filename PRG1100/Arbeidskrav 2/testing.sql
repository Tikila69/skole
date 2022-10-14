USE oblig2022;

-- Kode for å finne karakterstatestikk


SELECT eksamensresultat.emnekode, emne.emnenavn, emne.Studiepoeng, eksamensresultat.karakter, COUNT(eksamensresultat.studentnr) AS Antall 
FROM emne JOIN eksamensresultat ON eksamensresultat.emnekode=emne.emnekode 
WHERE eksamensresultat.emnekode="PRG1000" AND eksamensresultat.dato="20211201" AND karakter IS NOT NULL 
GROUP BY eksamensresultat.emnekode, emne.emnenavn, emne.Studiepoeng, eksamensresultat.karakter 
ORDER BY eksamensresultat.karakter