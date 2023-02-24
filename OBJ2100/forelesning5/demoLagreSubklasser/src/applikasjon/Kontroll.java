package applikasjon;

import hjelpeklasser.Filbehandling;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Kontroll {
    private ArrayList<Sensur> sensurering = new ArrayList<>();

    public void nySensur(Sensur sensur){
        sensurering.add(sensur);
    }

    public ArrayList<Sensur> getSensur() {
        return sensurering;
    }

    public void lagre(String filnavn) throws Exception{
        try {
            PrintWriter utfil = Filbehandling.lagSkriveforbindelse(filnavn);
            for(Sensur s : sensurering){
                utfil.println(s.toFile());
            }
            utfil.close();
        }
        catch (Exception e){
            throw new Exception("Sucky sucky");
        }
    }

    //Innlesningsmetoden må identifisere hva slags subklasse en linje representerer:
    public void leser(String filnavn) throws Exception{
        sensurering.clear();
        try {
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(filnavn);
            String linje = innfil.readLine();
            while (linje != ""){
                StringTokenizer innhold = new StringTokenizer(linje,";");
                //Leser første tegnet som definerer hvilken subklassen:
                String type = innhold.nextToken();
                if (type.equals("M")){
                    lesMuntlig(innhold);
                }
                else if (type.equals("S")) {
                    lesSkriftlig(innhold);
                }
                else {
                    lesProsjekt(innhold);
                }
                linje= innfil.readLine();
            }
            innfil.close();
        }
        catch (Exception e){
            throw new Exception("Much bad, very code");
        }
    }

    public void lesMuntlig(StringTokenizer innhold){
        String fag = innhold.nextToken();
        String eksamenstype = innhold.nextToken();
        double antallTimer = Double.parseDouble(innhold.nextToken());
        sensurering.add(new MuntligSensur(fag,eksamenstype,antallTimer));
    }

    public void lesSkriftlig(StringTokenizer innhold){
        String fag = innhold.nextToken();
        String eksamenstype = innhold.nextToken();
        double antallTimer = Double.parseDouble(innhold.nextToken());
        sensurering.add(new SkriftligSensur());
    }

    public void lesProsjekt(StringTokenizer innhold){
        String fag = innhold.nextToken();
        String eksamenstype = innhold.nextToken();
        int antallBesvarelser = Integer.parseInt(innhold.nextToken());
        sensurering.add(new Prosjektsensur(fag,eksamenstype,antallBesvarelser));
    }

}
