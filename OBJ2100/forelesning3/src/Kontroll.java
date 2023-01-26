import java.util.Collection;
import java.util.Iterator;
import java.util.TreeMap;

public class Kontroll {
    private TreeMap<String, Person> personer = new TreeMap<>();

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
