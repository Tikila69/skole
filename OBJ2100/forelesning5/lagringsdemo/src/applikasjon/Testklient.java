package applikasjon;

import java.util.Iterator;

public class Testklient {
    public static void main(String[] args) throws Exception {
        String filnavn = "varefil.csv";
        Kontroll kontroll = new Kontroll();
        Vare vare = new Vare(1,"Eske",5);
        kontroll.nyVare(1,vare);


        vare = new Vare(2,"Box",10);
        kontroll.nyVare(2,vare);


        vare = new Vare(3,"Kasse",15);
        kontroll.nyVare(3,vare);


        vare = new Vare(4,"Robins Virginity",0);
        kontroll.nyVare(4,vare);

        Iterator<Vare> varer = kontroll.getIterator();
        while (varer.hasNext()){
            vare = varer.next();
            System.out.println(vare.toString());
        }

        kontroll.lagreVarer(filnavn);
        kontroll.tøm();
        System.out.println("Nå skal varelisten være tømt");
        varer = kontroll.getIterator();
        while (varer.hasNext()){
            vare  = varer.next();
            System.out.println(vare.toString());
        }

        kontroll.leseVarerer(filnavn);
        System.out.println("Nå skal varelisten være full");
        varer = kontroll.getIterator();
        while (varer.hasNext()) {
            vare = varer.next();
            System.out.println(vare.toString());
        }

    }
}
