package com.example.demosingleton;
import java.sql.*;
public class Kontroll {
    private String databasenavn = "jdbc:mysql://localhost:3306/hobbyhuset";
    private  String databasedriver = "com.mysql.jdbc.Driver";
    public String sqlSpørring =
            "SELECT kunde.Etternavn, ordre.Ordredato, vare.betegnelse, ordrelinje.Antall " +
            "FROM kunde, ordre, vare, ordrelinje " +
            "WHERE kunde.KNr=Ordre.KNr " +
            "AND vare.VNr = ordrelinje.VNr " +
            "AND ordrelinje.OrdreNr = ordre.Ordrenr";

    private Connection forbindelse;
    private ResultSet resultat;
    private Statement utsagn;

    public void lagForbindelse() throws Exception{
        try {
            forbindelse = DriverManager.getConnection(databasenavn,"root","PASSORD");
        }
        catch (Exception e) {
            throw new Exception("Kan ikke opprette forbindelse med databasen");
        }
    }

    public void lukkForbindelse() throws Exception{
        try {
            if (forbindelse!= null){
                forbindelse.close();
            }
        } catch (Exception e){
            throw new Exception("Kan ikke lukke forbeindelse med databasen");
        }
    }


    //Kontroll lages som en singleton. Dette gjøres ved at vi lager en indre klasse som inneholder et final
    //objekt av kontroll:

    private static class kontrollHolder {
        private static final Kontroll INSTANCE = new Kontroll();
    }

    public Kontroll(){

    }

    public static Kontroll getInstance(){
        return kontrollHolder.INSTANCE;
    }

    public Resultset lesOrdre() throws Exception {
        resultat = null;
        try {
            utsagn = forbindelse.createStatement();
            resultat = utsagn.executeQuery(sqlSpørring);
        } catch (Exception e){
            throw new Exception("Kan ikke utføre spørring");
        }
    }
}
