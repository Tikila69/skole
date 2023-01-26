import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;

public class Kontorll {
    private HashMap<String, Person> personer = new HashMap<>();

    public void settInn(Person person) {
        //Henter ut navn fra objektet:
        String navn = person.getNavn();
        //Legger til navnet i hasmappet
        personer.put(navn,person);
    }


    public Person finnPerson(String nøkkel) {
        //Burde egentlig legge inn kontroll på om den finner noe før noe returneres.
        return personer.get(nøkkel);
    }

    public Iterator<Person> getPersoner() {
        Collection<Person> verdier = personer.values();
        return verdier.iterator();
    }
}
