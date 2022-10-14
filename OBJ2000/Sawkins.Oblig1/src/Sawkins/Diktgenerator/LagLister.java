package Sawkins.Diktgenerator;

import java.util.ArrayList;

public class LagLister {

    ArrayList<String> enkleOrd = new ArrayList<>();
    ArrayList<String> artikkel = new ArrayList<>();
    ArrayList<String> adjektiv = new ArrayList<>();
    ArrayList<String> substantiv = new ArrayList<>();
    ArrayList<String> verb = new ArrayList<>();

    public void fyllLister() {

        enkleOrd.add("Den");
        enkleOrd.add("Fulle");
        enkleOrd.add("Sover");
        enkleOrd.add("Mannen");
        enkleOrd.add("Smale");
        enkleOrd.add("Damen");
        enkleOrd.add("Lekker");

        artikkel.add("Den");

        adjektiv.add("Grønne");
        adjektiv.add("Stygge");
        adjektiv.add("Teite");
        adjektiv.add("Søvnige");

        substantiv.add("Mannen");
        substantiv.add("Damen");
        substantiv.add("Hunden");
        substantiv.add("Båten");

        verb.add("Sover");
        verb.add("Faller");
        verb.add("Trener");
        verb.add("Bjeffer");

    }

    public ArrayList<String> hentEnkelListe(){

        return enkleOrd;
    }

    public ArrayList<String> getArtikkel() {

        return artikkel;
    }

    public ArrayList<String> getAdjektiv() {
        return adjektiv;
    }

    public ArrayList<String> getSubstantiv() {
        return substantiv;
    }

    public ArrayList<String> getVerb() {
        return verb;
    }
}
