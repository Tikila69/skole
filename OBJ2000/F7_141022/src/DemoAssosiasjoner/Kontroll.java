 package DemoAssosiasjoner;

import java.util.ArrayList;
import java.util.Collections;

public class Kontroll {
    //Vi trenger en arraylist for hver type objekt:
    private ArrayList<Person> personArrayList = new ArrayList<>();
    private ArrayList<Kjøretøy> kjøretøyArrayList = new ArrayList<>();
    private ArrayList<Postadresse> postadresseArrayList = new ArrayList<>();

    //Metoder for å operere på datastrukturene:
    public void nyPerson (Person person) {
        personArrayList.add(person);

    }

    public void nyttKjøretøy (Kjøretøy kjøretøy) {
        kjøretøyArrayList.add(kjøretøy);
    }

    public void nyPostadresse (Postadresse postadresse){
        postadresseArrayList.add(postadresse);
    }

    public ArrayList<Kjøretøy> getAlleKjøretøy(){

        return kjøretøyArrayList;
    }

    public Person getPersoner (String navn) {
        Collections.sort(personArrayList);
        Person dummy = new Person(navn);
        int index = Collections.binarySearch(personArrayList, dummy);
        if (index>-1) return personArrayList.get(index);
        else return null;
    }

    public Kjøretøy getKjøretøy (String regnr) {
        Collections.sort(kjøretøyArrayList);
        Kjøretøy dummy = new Kjøretøy(regnr);
        int index = Collections.binarySearch(kjøretøyArrayList,dummy);
        if (index>-1) return kjøretøyArrayList.get(index);
        else return null;

    }

    public Postadresse getPostadresse (int postnr){
        Collections.sort(postadresseArrayList);
        Postadresse dummy = new Postadresse(postnr);
        int index = Collections.binarySearch(postadresseArrayList,dummy);
        if (index > -1) return postadresseArrayList.get(index);
        else return null;


    }
}
