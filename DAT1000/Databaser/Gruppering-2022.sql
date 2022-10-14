DROP SCHEMA IF EXISTS gruppering2022;
CREATE SCHEMA gruppering2022;

USE gruppering2022;

CREATE TABLE Ansatt
(
Ansattnr CHAR(4),
Fornavn CHAR(15) NOT NULL,
Stillingskode CHAR(4),
Lønnstrinn CHAR(2),
Avdelingsnr CHAR(4),
CONSTRAINT AnsattPK PRIMARY KEY (Ansattnr)
);

INSERT INTO Ansatt VALUES ('1','Brit','1008','66','3');
INSERT INTO Ansatt VALUES ("2","Ole","1008","67","1");
INSERT INTO Ansatt VALUES ("3","Robin","1010","1","2");
INSERT INTO Ansatt VALUES ("4","Roman","1012","99","2");
INSERT INTO Ansatt VALUES ("5","Erik","1010","50","1");
INSERT INTO Ansatt VALUES ("666","Didrik","9999","99","9999");
INSERT INTO Ansatt VALUES ("7","Vegard","0","0","3");
INSERT INTO Ansatt VALUES ("8","Dennis","1008","67","1");


