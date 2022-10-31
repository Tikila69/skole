package DemoAssosiasjoner;

import javax.swing.*;

public class Grensesnitt {

    int postnr;
    String poststed;
    String navn;
    String adresse;
    String regnr;
    String modell;

    Kontroll kontroll = new Kontroll();
    Postadresse postadresse = new Postadresse(postnr, poststed);
    Person person = new Person(navn, adresse, postadresse);

    Kjøretøy kjøretøy = new Kjøretøy(regnr, modell, person);


    private final String[] alternativer = {
            "Registrer Person",
            "Registrer Kjøretøy",
            "Finn Person",
            "Finn Kjøretøy",
            "Finn Postadresse",
            "Vis alle registrerte kjøretøy",
            "Avslutt"
    };

    public int lesValg() {
        int valg = JOptionPane.showOptionDialog(
                null,
                "Hva ønsker du å registrere?",
                "Bil og Personregister",
                JOptionPane.DEFAULT_OPTION,
                JOptionPane.PLAIN_MESSAGE,
                null,
                alternativer,
                alternativer[0]
        );
        return valg;
    }

    public void meny (){
        boolean fortsette = true;
        while (fortsette) {
            int valg = lesValg();
            switch (valg){
                case 0: registrerPerson();
                break;
                case 1: registrerKjøretøy();
                break;
                case 2: søkPerson();
                break;
                case 3: søkKjøretøy();
                break;
                case 4: søkPostadresse();
                break;
                case 5: visKjøretøy();
                break;
                default: fortsette = false;
                break;
            }
        }
    }

    public void registrerPerson() {
        navn = JOptionPane.showInputDialog("Navn:");
        adresse = JOptionPane.showInputDialog("Adresse:");
        postnr = Integer.parseInt(JOptionPane.showInputDialog("Postnummer:"));
        poststed = JOptionPane.showInputDialog("Poststed:");

        postadresse = new Postadresse(postnr,poststed);
        person = new Person(navn,adresse,postadresse);

        kontroll.nyPerson(person);
        kontroll.nyPostadresse(postadresse);
        JOptionPane.showMessageDialog(
                null,
                "Kunde Registrert: " +
                        person.toString()+
                        " " +
                        postadresse.toString()
        );

    }

    public void registrerKjøretøy() {
        navn = JOptionPane.showInputDialog("Hvem skal bilen registreres på?");
        regnr = JOptionPane.showInputDialog("Registreringsnummer:");
        modell = JOptionPane.showInputDialog("Modell");

        kjøretøy = new Kjøretøy(regnr,modell,kontroll.getPersoner(navn));

        kontroll.nyttKjøretøy(kjøretøy);

        JOptionPane.showMessageDialog(
                null,
                "Kjøretøy registrert: " +
                        kjøretøy.toString()
        );

    }

    public void søkPerson(){
        navn = JOptionPane.showInputDialog("Navn:");
        JOptionPane.showMessageDialog(
                null,
                kontroll.getPersoner(navn)
        );
    }

    public void søkKjøretøy(){
        regnr = JOptionPane.showInputDialog("Regnr:");
        JOptionPane.showMessageDialog(
                null,
                kontroll.getKjøretøy(regnr)
        );
    }

    public void søkPostadresse(){
        postnr = Integer.parseInt(JOptionPane.showInputDialog("Postnr"));
        JOptionPane.showMessageDialog(
                null,
                kontroll.getPostadresse(postnr)
        );
    }

    public void visKjøretøy(){
        JOptionPane.showMessageDialog(
                null,
                kontroll.getAlleKjøretøy()
        );
    }
}
