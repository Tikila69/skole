package Lagredemo;

import Hjelpeklasser.Filbehandling;

import java.io.BufferedReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Kontroll {
    private ArrayList<Person> personer = new ArrayList<>();

    public void nyPerson(Person person){
        personer.add(person);
    }

    public ArrayList<Person> getPersoner(){
        return personer;
    }

    public void tøm(){
        personer.clear();
    }

    //Metode for å lagre objektene:
    public void skrivData(String filnavn){
        try {
            PrintWriter utfil = Filbehandling.lagSkriveforbindelse(filnavn);
            //Går gjennom datastrikturen:
            for (Person p : personer){
                utfil.println(p.toFile());
            }
            utfil.close();
        } catch (Exception e){
            System.out.println("Feil i skrivData");
        }
    }

    //Metode for å lese filen og gjennopprette objektene:
    public void lesData(String filnavn){
        //Tømmer datastrukturen
        personer.clear();
        try {
            BufferedReader innfil = Filbehandling.lagLeseforbindelse(filnavn);
            String linje = innfil.readLine();
            while (linje!=null){
                StringTokenizer innhold = new StringTokenizer(linje,",");
                String fornavn = innhold.nextToken();
                String etternavn = innhold.nextToken();
                int fødselsår = Integer.parseInt(innhold.nextToken());
                personer.add(new Person(fornavn,etternavn,fødselsår));
                linje=innfil.readLine();
            }
            innfil.close();
        }catch (Exception e){
            System.out.println("Feil i lesData");
        }
    }
}
