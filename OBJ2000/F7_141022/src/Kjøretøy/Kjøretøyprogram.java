package Kjøretøy;

import javax.swing.*;

public class Kjøretøyprogram {
    public static void main(String[] args) {
        Kontroll kontroll = new Kontroll();
        String regnr="";
        String produsent="";
        String modell="";
        int regår=0;
        int antallPlasser=1;
        Personbil personbil1 = new Personbil(regnr, produsent, modell, regår, antallPlasser);
        Personbil personbil2 = new Personbil(regnr, produsent, modell, regår, antallPlasser);

        for (int i = 1; i<11; i++) {

            regnr = i+"a";
            produsent = i+"a";
            modell = i+"a";
            regår = i;
            antallPlasser = i;
            personbil1 = new Personbil(regnr, produsent, modell, regår, antallPlasser);

            System.out.println(personbil1.toString());
            kontroll.nyttKjøretøy(personbil1);
        }

        for (int i = 1; i<11; i++) {

            regnr = i+"b";
            produsent = i+"b";
            modell = i+"b";
            regår = i;
            antallPlasser = i;
            personbil2 = new Personbil(regnr, produsent, modell, regår, antallPlasser);

            System.out.println(personbil2.toString());
            kontroll.nyttKjøretøy(personbil2);
        }


        System.out.println(" ");
        System.out.println("Liste over kjøretøy: "+kontroll.getListe());




        regnr = JOptionPane.showInputDialog("Hvilket regnr ønsker du å søke etter?");
        System.out.println(kontroll.finnKjøretøy(regnr));
        System.out.println(" ");

        System.out.println(personbil2.compareTo(personbil1)); //1b er større enn 1a så skal returnere 1
        System.out.println(personbil1.compareTo(personbil2)); //1a er mindre enn 1b så skal returnere -1
        System.out.println(personbil1.compareTo(personbil1));//1a og 1a er like så skal returnere 0
        System.out.println(" ");

        System.out.println(personbil1.equals(personbil1)); //1a og 1a er like så skal returnere true
        System.out.println(personbil1.equals(personbil2));//1a og 1b er ikke like så skal returnere false

    }
}
