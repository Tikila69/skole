package Kjøretøy;

import java.util.ArrayList;
import java.util.Collections;

public class Kontroll {
    //En kontrollklasse skal inneholde de nødvendige datastrukturene
    //Objekter av subklassene til kjøretøy er også kjøretøy
    private ArrayList<Kjøretøy> kjøretøyliste = new ArrayList<>();

    //Forutsetter at objekt av riktig subklasse opprettes av grensensittet
    public void nyttKjøretøy(Kjøretøy kjøretøy) {
        kjøretøyliste.add(kjøretøy);
    }

    public Kjøretøy finnKjøretøy (String regnr) {
        //Vi må være sikre på at kjøretøyliste er sortert
        Collections.sort(kjøretøyliste);
        //FOr å kunne bruke binærsøk lager vi et dummyø+-objekt med dt registreringsnummeret vi søker etter
        //Kjøretøy dummy = new Kjøretøy(regnr, null, null, 0);
        //Bruk i steden den ekstra konstruktøren i Kjøretøy:
        Kjøretøy dummy = new Kjøretøy(regnr);
        //Bruker binærsøk:
        //binarySearch returnerer indexen til objektet hvis den finner objektet
        //Dersom den ikke finner noe returnerer den et negativt tall
        int index = Collections.binarySearch(kjøretøyliste,dummy);
        if (index>-1){
            return kjøretøyliste.get(index);
        }
        else return null;
    }

    public ArrayList<Kjøretøy> getListe() {
        return kjøretøyliste;
    }
}
