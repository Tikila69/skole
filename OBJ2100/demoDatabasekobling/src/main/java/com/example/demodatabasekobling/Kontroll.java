package com.example.demodatabasekobling;

public class Kontroll {
    private String databasenavn = "jdbc:mysql:localhost:3306/hobbyhuset";
    private String databasedriver = "com.mysql.jbdc.Driver";
    private Connection forbindelse;
    private ResultSet resultat;
    private Statement utsagn;

    //metode for tilkobling:
    public void lagForbindelse() throws Exception {
        try {
            forbindelse = DriverManager.getConnection(databasenavn,"root","Icastforeball20");
        }
        catch (Exception e) {
            throw new Exception("Kan ikke åpne database");
        }
    }

    public void lukk() throws Exception{
        try {
            if(forbindelse!=null)forbindelse.close();
        }
        catch (Exception e){
            throw new Exception("Kan ikke lukke database");
        }
    }

    public ResultSet lesKunder() throws Exception {
        resultat = null;
        String sql = "select * from Kunde";
        try {
            utsagn = forbindelse.createStatement();
            resultat = utsagn.executeQuery(sql);
            return resultat;
        }
        catch (Exception e) {
            throw new Exception("kan ikke åpne databasetabell");
            return null;
        }

    }
}
