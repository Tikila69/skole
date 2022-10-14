DROP SCHEMA IF EXISTS oblig2022;

CREATE SCHEMA oblig2022;

USE oblig2022;

-- Student(Studentnr, Fornavn, Etternavn, Epost, Telefon) 
-- Emne(Emnekode, Emnenavn, Studiepoeng) 
-- Rom(Romnr, Antallplasser) 
-- Eksamen(Emnekode*, Dato, Romnr*) 
-- Eksamensresultat(Studentnr*, Emnekode*, Dato*, Karakter)

CREATE TABLE Student (
    Studentnr CHAR(6),
    Fornavn CHAR(30),
    Etternavn CHAR (20),
    Epost CHAR (40),
    Telefon CHAR(8),
    CONSTRAINT StudentPK PRIMARY KEY (Studentnr)
);


CREATE TABLE Emne (
    Emnekode CHAR(8),
    Emnenavn CHAR(40),
    Studiepoeng DECIMAL(3,1),
    CONSTRAINT EmnePK PRIMARY KEY (Emnekode)
);


CREATE TABLE Rom (
    Romnr CHAR(4),
    Antallplasser INTEGER(3),
    CONSTRAINT RomPK PRIMARY KEY (Romnr)
);


CREATE TABLE Eksamen (
    Emnekode CHAR(8),
    Dato DATE,
    Romnr CHAR (4),
    CONSTRAINT EksamenPK PRIMARY KEY (Emnekode, Dato),
    CONSTRAINT EksamenEmnekodeFK FOREIGN KEY (Emnekode) REFERENCES Emne (Emnekode),
    CONSTRAINT EksamenRomnrFK FOREIGN KEY (Romnr) REFERENCES Rom (Romnr)
);

CREATE TABLE Eksamensresultat (
    Studentnr CHAR(6),
    Emnekode CHAR(8),
    Dato DATE,
    Karakter CHAR(1),
    CONSTRAINT EksamensresultatPK PRIMARY KEY (Studentnr, Emnekode, Dato),
    CONSTRAINT EksamensresultatStudentnrFK FOREIGN KEY (Studentnr) REFERENCES Student (Studentnr),
    CONSTRAINT EksamensresultatEmnekodeDatoFK FOREIGN KEY (Emnekode, Dato) REFERENCES Eksamen (Emnekode, Dato)
);


INSERT INTO Student (Studentnr, Fornavn, Etternavn, Epost, Telefon) VALUES 
("100","Didrik","Sawkins","didrik.ruud.sawkins@gmail.com","95767711"),
("101","Vegard","Sveinsvoll","Vegard.Sveinsvoll@epost.no","12345678"),
("102","Robin","Tangen","Robin.Tangen@epost.no","23456781"),
("103","Erik","Bøhle","Erik.bøhle@epost.no","34567812"),
("104","Roman","Kollar","Roman.kollar@epost.no","45678123"),
("105","Jordan","Wong","elit.a@protonmail.couk","31368113"),
("106","Tucker","Rutledge","imperdiet@aol.org","86379404"),
("107","Joshua","Beard","praesent.eu@icloud.ca","88859684"),
("108","Owen","Blackburn","at@google.couk","32125588"),
("109","Ivan","Cole","auctor.velit@icloud.net","83596593"),
("110","Rowan","Ashley","mus.donec@hotmail.net","39661022"),
("111","Chancellor","Wilson","hendrerit.consectetuer@outlook.org","25722412"),
("112","Bree","Mckee","lectus.rutrum@aol.org","34127351"),
("113","Evan","Stephenson","neque.nullam@hotmail.couk","54411746"),
("114","Malcolm","Byers","duis.cursus@hotmail.org","23918727"),
("115","Martin","Larson","sagittis@protonmail.ca","81854756"),
("116","Connor","Fernandez","vivamus@aol.net","52033776"),
("117","Kiayada","Carroll","est.ac@protonmail.edu","81671561"),
("118","Barrett","Flowers","mauris.sit@icloud.org","23673013"),
("119","Olympia","Bruce","porttitor@protonmail.couk","23756667"),
("120","Ross","Hendrix","mauris.blandit.enim@protonmail.edu","70397475"),
("121","Damon","Lloyd","nec@icloud.net","67640052"),
("122","Regan","Whitfield","risus@protonmail.couk","64878517"),
("123","Aline","Sandoval","rhoncus@aol.com","65605568"),
("124","Flavia","Jennings","metus@outlook.edu","46461485"),
("125","Kylie","Gentry","a.facilisis@outlook.com","76446065"),
("126","Zeus","Franks","lorem@icloud.com","46564494"),
("127","Dustin","Wood","adipiscing@yahoo.org","69485311"),
("128","Odessa","Lindsey","nisi@yahoo.ca","13574563"),
("129","Iliana","Levine","egestas.fusce@hotmail.org","85532198"),
("130","Michelle","Glenn","eros.proin@google.net","87848316"),
("131","Shelley","Willis","lacus.etiam@yahoo.org","27364300"),
("132","Britanney","Barrett","orci.luctus@outlook.edu","69625859"),
("133","Carly","Myers","aliquet@hotmail.org","88156813"),
("134","Claire","Lloyd","convallis.est@icloud.edu","79376246"),
("135","Savannah","Oliver","neque.vitae@hotmail.couk","92544568"),
("136","Pearl","Maxwell","dolor.fusce@google.org","89444126"),
("137","Arden","Butler","blandit@google.ca","20157823"),
("138","Riley","Peck","dolor.fusce@protonmail.org","58065626"),
("139","Barry","Shelton","imperdiet.dictum@aol.edu","35658768"),
("140","Nora","Knight","aliquam.erat@google.org","66837353"),
("141","Sydnee","Trujillo","enim@hotmail.ca","35884625"),
("142","Gloria","Wheeler","justo@hotmail.org","28624755"),
("143","Ian","Delgado","vestibulum@outlook.org","83766705"),
("144","Lee","Shannon","rutrum.fusce@google.couk","64925191"),
("145","Axel","Schroeder","cras.sed@yahoo.edu","43751387"),
("146","Katelyn","Mcmillan","consequat.enim.diam@aol.ca","47329816"),
("147","Mollie","Guzman","lorem@hotmail.ca","38831354"),
("148","Clarke","Franklin","mauris@outlook.ca","76078976"),
("149","Camden","Norman","risus.a@protonmail.edu","62537349");



INSERT INTO Emne (Emnekode, Emnenavn, Studiepoeng) VALUES 
("PRG1000","Grunnleggende Programmering 1",7.5),
("WEB1100","Webutvikling og HCI",7.5),
("SYS1000","Systemutvikling",7.5),
("INF1000","Informasjonssystemer",7.5),
("DAT1000","Database 1",7.5),
("ORL1000","Organisasjon og Ledelse",7.5), 
("PRG1100","Grunnleggende Programmering 2",7.5),
("PRO1000","Praktisk Prosjekt",7.5);


INSERT INTO Rom (Romnr, Antallplasser) VALUES 
("A101",80),
("A102",50),
("A201",80),
("A202",50),
("B101",50),
("B102",30),
("B201",50),
("B202",30),
("C101",150),
("C102",150),
("C201",150),
("C202",150),
("D101",200),
("D102",100),
("D201",200),
("D202",100);


INSERT INTO Eksamen (Emnekode, Dato, Romnr) VALUES 
("WEB1100","20211201","A101"),
("INF1000","20211201","A102"),
("SYS1000","20211201","B201"),
("PRG1000","20211201","B202"),
("PRG1100","20220501","C101"),
("DAT1000","20220501","C202"),
("PRO1000","20220501","D201"),
("ORL1000","20220501","D102"),
("WEB1100","20201201","A101");

INSERT INTO eksamensresultat (Studentnr, Emnekode, Dato, karakter) VALUES 
("100","WEB1100","20201201","A"),
("100","WEB1100","20211201","C"),
("100","INF1000","20211201","E"),
("100","SYS1000","20211201","A"),
("100","PRG1000","20211201","B"),
("101","WEB1100","20211201","C"),
("101","INF1000","20211201","E"),
("101","SYS1000","20211201","A"),
("101","PRG1000","20211201","C"),
("102","WEB1100","20211201","C"),
("102","INF1000","20211201","C"),
("102","SYS1000","20211201","A"),
("102","PRG1000","20211201","A"),
("103","WEB1100","20211201","A"),
("103","INF1000","20211201","C"),
("103","SYS1000","20211201","A"),
("103","PRG1000","20211201","A"),
("104","WEB1100","20211201","C"),
("104","INF1000","20211201","A"),
("104","SYS1000","20211201","A"),
("104","PRG1000","20211201","A"),
("100","PRG1100","20220501","A"),
("100","DAT1000","20220501","A"),
("100","PRO1000","20220501","A"),
("100","ORL1000","20220501","F"),
("101","PRG1100","20220501",NULL),
("101","DAT1000","20220501",NULL),
("101","PRO1000","20220501",NULL),
("101","ORL1000","20220501",NULL),
("102","PRG1100","20220501",NULL),
("102","DAT1000","20220501",NULL),
("102","PRO1000","20220501",NULL),
("102","ORL1000","20220501",NULL),
("103","PRG1100","20220501",NULL),
("103","DAT1000","20220501",NULL),
("103","PRO1000","20220501",NULL),
("103","ORL1000","20220501",NULL),
("104","PRG1100","20220501",NULL),
("104","DAT1000","20220501",NULL),
("104","PRO1000","20220501",NULL),
("104","ORL1000","20220501",NULL),
("105","DAT1000","20220501",NULL),
("106","PRO1000","20220501",NULL),
("107","PRO1000","20220501",NULL),
("108","ORL1000","20220501",NULL),
("109","ORL1000","20220501",NULL),
("110","PRO1000","20220501",NULL),
("111","PRG1100","20220501",NULL),
("112","PRG1100","20220501",NULL),
("113","ORL1000","20220501",NULL),
("114","ORL1000","20220501",NULL),
("115","PRG1100","20220501",NULL),
("116","ORL1000","20220501",NULL),
("117","DAT1000","20220501",NULL),
("118","DAT1000","20220501",NULL),
("119","ORL1000","20220501",NULL),
("120","PRO1000","20220501",NULL),
("121","PRG1100","20220501",NULL),
("122","ORL1000","20220501",NULL),
("123","DAT1000","20220501",NULL),
("124","PRO1000","20220501",NULL),
("125","DAT1000","20220501",NULL),
("126","DAT1000","20220501",NULL),
("127","PRO1000","20220501",NULL),
("128","PRG1100","20220501",NULL),
("129","PRO1000","20220501",NULL),
("130","DAT1000","20220501",NULL),
("131","ORL1000","20220501",NULL),
("132","PRG1100","20220501",NULL),
("133","DAT1000","20220501",NULL),
("134","DAT1000","20220501",NULL),
("135","PRG1100","20220501",NULL),
("136","DAT1000","20220501",NULL),
("137","PRO1000","20220501",NULL),
("138","PRO1000","20220501",NULL),
("139","DAT1000","20220501",NULL),
("140","PRG1100","20220501",NULL),
("141","PRG1100","20220501",NULL),
("142","PRO1000","20220501",NULL),
("143","DAT1000","20220501",NULL),
("144","PRO1000","20220501",NULL),
("145","PRG1100","20220501",NULL),
("146","DAT1000","20220501",NULL),
("147","PRG1100","20220501",NULL),
("148","PRG1100","20220501",NULL),
("149","PRO1000","20220501",NULL);