import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;

public class Kontroll {
    private ArrayList<Kurs> kursliste = new ArrayList<>();
    //private ArrayList<Person> personliste = new ArrayList<>();
    private LinkedList<Person> personliste = new LinkedList<>();

    public void nyPerson(Person person) {
        personliste.add(person);
    }

    public void nyttKurs(Kurs kurs){
        kursliste.add(kurs);
    }

    public void finnPerson(){
    }

    public void regKursPåPerson(Kurs kurset, Long personnummer){
        Student studenten = (Student)finnPerson(personnummer);
        if(studenten!=null) studenten.nyttKurs(kurset);
    }

    public Iterator<Person> getIterator() {
        return (Iterator)personliste.linkedIterator();
    }



}
