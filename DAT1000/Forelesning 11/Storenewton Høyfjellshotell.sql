DROP SCHEMA IF EXISTS Storenewton;

CREATE SCHEMA Storenewton;

USE Storenewton;

CREATE TABLE Kunde (
    Mobilnr CHAR(10),
    Fornavn CHAR(20) NOT NULL,
    Etternavn CHAR(20) NOT NULL,
    CONSTRAINT KundePK PRIMARY KEY(Mobilnr)
);

CREATE TABLE Rom (
    Romnr CHAR(4),
    Romtype CHAR(20),
    CONSTRAINT RomPK PRIMARY KEY(Romnr)
);

CREATE TABLE Bestilling (
    ROMNR CHAR(4),
    Fradato DATE,
    Tildato DATE,
    Mobilnr CHAR(10),
    CONSTRAINT BestillingPK PRIMARY KEY (Romnr,Fradato),
    CONSTRAINT BestillingRomFK FOREIGN KEY (Romnr) REFERENCES Rom(Romnr),
    CONSTRAINT BestillingKundeFK FOREIGN KEY (Mobilnr) REFERENCES Kunde(Mobilnr)
);


INSERT INTO Kunde (Mobilnr, Fornavn, Etternavn) VALUES 
("4705373724","Alden","Rojas"),
("4791201181","Lillian","Munoz"),
("4748786828","Chanda","Dickson"),
("4741417436","Miranda","Acosta"),
("4786210287","Keith","Terrell"),
("4782476276","Rajah","Reyes"),
("4775764363","Inga","Chase"),
("4727181457","Rajah","Fernandez"),
("4775385343","Brent","Joseph"),
("4724715976","Ivana","Wallace"),
("4700122250","Sharon","Galloway"),
("4783393525","Gay","Holmes"),
("4797351753","Vernon","Kramer"),
("4754565606","Magee","Stewart"),
("4742868538","Quinlan","Buck"),
("4727853442","Theodore","Gates"),
("4723254517","Leslie","Blair"),
("4782115139","Hammett","Cannon"),
("4732311689","Kelsey","Riggs"),
("4766316140","Rhona","Warner");



INSERT INTO Rom (Romnr, Romtype) VALUES
("100","Dobbeltrom"),
("101","Dobbeltrom"),
("102","Familierom"),
("103","Familierom"),
("104","Dobbeltrom"),
("105","Dobbeltrom"),
("106","Familierom"),
("107","Familierom"),
("108","Dobbeltrom"),
("109","Dobbeltrom"),
("110","Familierom"),
("111","Familierom"),
("112","Dobbeltrom"),
("113","Dobbeltrom"),
("114","Familierom"),
("115","Familierom"),
("116","Dobbeltrom"),
("117","Dobbeltrom"),
("118","Familierom"),
("119","Familierom"),
("120","Dobbeltrom"),
("121","Dobbeltrom"),
("122","Familierom"),
("123","Familierom"),
("124","Dobbeltrom"),
("125","Dobbeltrom"),
("126","Familierom"),
("127","Familierom"),
("128","Dobbeltrom"),
("129","Dobbeltrom"),
("130","Familierom"),
("131","Familierom"),
("132","Dobbeltrom"),
("133","Dobbeltrom"),
("134","Familierom"),
("135","Familierom"),
("136","Dobbeltrom"),
("137","Dobbeltrom"),
("138","Familierom"),
("139","Familierom"),
("140","Dobbeltrom"),
("141","Dobbeltrom"),
("142","Familierom"),
("143","Familierom"),
("144","Dobbeltrom"),
("145","Dobbeltrom"),
("146","Familierom"),
("147","Familierom"),
("148","Dobbeltrom"),
("149","Dobbeltrom");


INSERT INTO Bestilling (Romnr, Fradato, Tildato, Mobilnr) VALUES
("100","20220501","20220504","4705373724"),
("100","20220511","20220515","4791201181"),
("101","20220501","20220505","4748786828"),
("101","20220510","20220515","4741417436"),
("102","20220504","20220511","4786210287"),
("103","20220504","20220510","4782476276"),
("104","20220504","20220507","4775764363"),
("105","20220505","20220507","4727181457"),
("106","20220505","20220511","4775385343"),
("107","20220507","20220511","4705373724"),
("108","20220507","20220510","4791201181"),
("109","20220505","20220510","4748786828"),
("110","20220506","20220509","4741417436");