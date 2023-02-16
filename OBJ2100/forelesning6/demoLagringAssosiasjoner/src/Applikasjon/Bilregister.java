package Applikasjon;

import Hjelpeklasser.Filbehandling;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Bilregister {
    List<Person> personer = new ArrayList<Person>();
    List<Bil> biler = new ArrayList<Bil>();
    List<Postadresse> postadresser = new ArrayList<Postadresse>();
    String bilfil = "biler.csv";
    String personfil = "personfil.csv";
    String postadressefil = "postadressefil.csv";

    public void regBil(Bil b){
        biler.add(b);
    }

    public void regPerson(Person p){
        personer.add(p);
    }

    public void regPostadresse(Postadresse p){
        postadresser.add(p);
    }

    //Søkemetoder:
    public Postadresse finnPostadresse(String postnr){
        for (int i = 0;i<postadresser.size();i++){
            Postadresse p = postadresser.get(i);
            if (p.getPostnr().equals(postnr)){
                return p;
            }
        }
        return null;
    }

    public Person finnPerson(String eNavn){
        for (int i=0;i< personer.size();i++){
            Person p = personer.get(i);
            if (p.getEnavn().equals(eNavn)){
                return p;
            }
        }
        return null;
    }

    public Bil finnBil(String regnr){
        for (int i=0;i< biler.size();i++){
            Bil b = biler.get(i);
            if (b.getRegnr().equals(regnr)){
                return b;
            }
        }
        return null;
    }

    //Lagringsmetoder:
    public void skrivPersoner(String filnavn) throws Exception{
        try {
            PrintWriter utfil = Filbehandling.lagSkriveforbindelse(filnavn);
            for (int i=0; i< personer.size();i++){
                utfil.println(personer.get(i).toFile());
            }
            utfil.close();
        }catch (Exception e){
            throw new Exception("Kan ikke lagre personer");
        }
    }

    public void skrivBiler(String filnavn) throws Exception{
        try {
            PrintWriter utfil = Filbehandling.lagSkriveforbindelse(filnavn);
            for (int i=0;i<biler.size();i++){
                utfil.println(biler.get(i));
            }
            utfil.close();
        }catch (Exception e){
            throw new Exception("Kan ikke lagre biler");
        }
    }

    public void skrivPostadresser(String filnavn) throws Exception{
        try {
            PrintWriter utfil = Filbehandling.lagSkriveforbindelse(filnavn);
            for (int i=0;i< postadresser.size();i++){
                utfil.println(postadresser.get(i));
            }
            utfil.close();
        }catch (Exception e){
            throw new Exception("Kan ikke lagre postadresser");
        }
    }

    //Innlesningsmetoder;

    public void lesPostadresser(String filnavn) throws Exception{
        try {
            BufferedReader innfil= Filbehandling.lagLeseforbindelse(filnavn);
            //Leser første linje:
            String linje = innfil.readLine();
            while (linje!=null){
                StringTokenizer innhold = new StringTokenizer(linje,";");
                String postnr = innhold.nextToken();
                String postadresse = innhold.nextToken();
                postadresser.add(new Postadresse(postnr,postadresse));
                linje=innfil.readLine();
            }
            innfil.close();
        }catch (Exception e){
            throw new Exception("Kan ikke lese postadressefil");
        }
    }

    public void lesPersoner(String filnavn) throws Exception{
        try {
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(filnavn);
            String linje = innfil.readLine();
            while (linje!=null){
                StringTokenizer innhold = new StringTokenizer(linje,";");
                String enavn = innhold.nextToken();
                String fnavn = innhold.nextToken();
                String gateadresse = innhold.nextToken();
                //Leser postnr fra fila der den opptrer som fremmednøkkel:
                String postnr = innhold.nextToken();
                //Bruker postnr til å finne referanse til postadressen:
                Postadresse postadresse = finnPostadresse(postnr);
                personer.add(new Person(enavn,fnavn,gateadresse,postadresse));
                linje=innfil.readLine();
            }
        }catch (Exception e){
            throw new Exception("Kan ikke lese personfil");
        }
    }

    public void lesBiler(String filnavn) throws Exception{
        try {
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(filnavn);
            String linje = innfil.readLine();
            while (linje!=null){
                StringTokenizer innhold = new StringTokenizer(linje,";");
                String regnr = innhold.nextToken();
                String merke = innhold.nextToken();
                String modell = innhold.nextToken();
                String enavn = innhold.nextToken();
                Person eier = finnPerson(enavn);
                Bil b = new Bil(regnr,merke,modell,eier);
                biler.add(b);
                eier.regBil(b);
                linje = innfil.readLine();
            }
        }catch (Exception e){
            throw new Exception("Kan ikke lese bilfil");
        }
    }

    public void lesAlleFiler() throws Exception{
        try {
            lesPostadresser(postadressefil);
            lesPersoner(personfil);
            lesBiler(bilfil);
        }catch (Exception e){
            throw e;
        }
    }

    public void skrivAlleFiler() throws Exception{
        try {
            skrivPostadresser(postadressefil);
            skrivPersoner(personfil);
            skrivBiler(bilfil);
        }catch (Exception e){
            throw e;
        }
    }
}
