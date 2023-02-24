package applikasjon;

import hjelpeklasser.Filbehandling;

import java.io.BufferedReader;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Kontroll {
    private HashMap<Integer,Vare> vareliste = new HashMap<>();
    private String filename = "varer.csv";

    public void nyVare(Integer nøkkel, Vare vare){
        vareliste.put(nøkkel,vare);
    }

    public Vare getVare(Integer nøkkel) {
        return vareliste.get(nøkkel);
    }

    //Metode for å lage en iterator
    public Iterator<Vare> getIterator() {
        return vareliste.values().iterator();
    }

    public void lagreVarer(String filnanv) throws Exception{
        try{
            PrintWriter utfil = Filbehandling.lagSkriveforbindelse(filename);
            Iterator<Vare> oppramser = getIterator();
            while (oppramser.hasNext()){
                Vare vare = oppramser.next();
                utfil.println(vare.toFile());
            }
            utfil.close();
        }
        catch (Exception e){
            throw new Exception("Kan ikke lese filen");
        }
    }

    public void leseVarerer(String filnavn) throws Exception{
        String innlinje;
        StringTokenizer inndata;
        try {
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(filename);
            while (innfil.ready()){
                innlinje = innfil.readLine();
                inndata = new StringTokenizer(innlinje,";");
                int varenr = Integer.parseInt(inndata.nextToken());
                String varenavn = inndata.nextToken();
                int beholdning = Integer.parseInt(inndata.nextToken());
                vareliste.put(varenr, new Vare(varenr,varenavn,beholdning));
            }
            innfil.close();
        }
        catch (Exception e) {
            throw new Exception("Yu Fakked app!");
        }
    }

    public void tøm() {
        vareliste.clear();
    }


}
