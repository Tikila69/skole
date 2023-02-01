package Lagredemo;

import java.util.ArrayList;

public class Testklient {
    public static void main(String[] args) {

        //Tester skriving til fil
        String filnavn = "personer.csv";
        Kontroll kontroll = new Kontroll();

        kontroll.nyPerson(new Person("Didrik", "Sawkins", 1991));
        kontroll.nyPerson(new Person("Robin", "Tangen", 2020));
        kontroll.nyPerson(new Person("Roman", "Emperor", 2000));


        //Tester innlesning fra fil:
        ArrayList<Person> personer = kontroll.getPersoner();
        for (Person p : personer) {
            if (p != null) System.out.println(p.toString());
        }
        System.out.println();

        //Lagrer:
        kontroll.skrivData(filnavn);

        //Tømmer ArrayListen i kontroll
        kontroll.tøm();
        System.out.println("Sjekker at objektet er tømt");
        System.out.println(personer);
        //Sjekker at den er tom:
        personer = kontroll.getPersoner();
        for (Person p : personer) {
            if (p != null) System.out.println(p.toString());
        }

        kontroll.lesData(filnavn);
        System.out.println();
        System.out.println("Sjekker at objekt er opprettet");
        personer = kontroll.getPersoner();
        for (Person p : personer) {
            if (p != null) System.out.println(p.toString());
        }
    }
}
