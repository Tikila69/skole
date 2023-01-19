import java.util.Iterator;

public class Grensesniitt {
    Long personnummer;
    String kursid;
    String kursnavn;

    Kontroll kontroll = new Kontroll();
    Kurs kurs = new Kurs(kursid,kursnavn);

    public void skrivPersoner() {
        Iterator<Person> oppramser = kontroll.getIterator();
        while (oppramser.hasNext()) {
            System.out.println(oppramser.next().toString());
        }
    }

    public void registrerKurs() {
        kontroll.regKursPåPerson(kurs,personnummer);
    }
}
