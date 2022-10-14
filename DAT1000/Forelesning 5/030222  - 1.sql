USE ansattpersonal2022;

INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES ("1000","IT");
INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES ("2000","Admininstrasjon");
INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES ("3000","Økonomi");
INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES ("4000","Personal");
INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES ("5000","Vedlikehold");

INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES ("1000","Avdelingssjef");
INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES ("2000","Konsulent");
INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES ("3000","Økonomimedarbeider");
INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES ("4000","Sekretær");
INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES ("5000","Trainee");


INSERT INTO Postkatalog(Postnr,Poststed) VALUES ("1000","Storeby");
INSERT INTO Postkatalog(Postnr,Poststed) VALUES ("1500","Lilleby");
INSERT INTO Postkatalog(Postnr,Poststed) VALUES ("2000","Mellomby");
INSERT INTO Postkatalog(Postnr,Poststed) VALUES ("2500","Storebygd");
INSERT INTO Postkatalog(Postnr,Poststed) VALUES ("3000","Mellombygd");
INSERT INTO Postkatalog(Postnr,Poststed) VALUES ("3500","Lillebygd");

INSERT INTO Kurs(Kursnr,Kursnavn) VALUES ("1000","HMS");
INSERT INTO Kurs(Kursnr,Kursnavn) VALUES ("2000","Brannvakt");
INSERT INTO Kurs(Kursnr,Kursnavn) VALUES ("3000","Førstehjelp");
INSERT INTO Kurs(Kursnr,Kursnavn) VALUES ("4000","Sistehjelp");

INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES ("1000","Ole","Olsen","Finnsikkegate 69","69696969","1000","1000","1000");
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES ("2000","Hans","Hansen","Finshellerikke 6","14204201","2000","2000","1500");
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES ("3000","Jens","Jensen","Nordpolen 1","66699901","3000","3000","2000");
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES ("4000","Trine","Trinesen","Sørpolen 2","12345678","4000","4000","2500");
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES ("5000","Kari","Vilikke","Hjemme 666","87654321","5000","5000","3000");

INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES ("1000","1000","2022-02-03","Bestått");
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES ("1000","2000","2022-02-03","Ikke Bestått");
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES ("2000","1000","2022-02-03","Bestått");
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES ("2000","2000","2022-02-03","Ikke Bestått");
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES ("3000","3000","2022-02-03","Bestått");
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES ("4000","2000","2022-02-03","Bestått");
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES ("5000","2000","2022-02-03","Bestått");
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES ("5000","3000","2022-02-03","Bestått");


