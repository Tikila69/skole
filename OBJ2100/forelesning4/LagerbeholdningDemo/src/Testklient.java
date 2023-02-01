import java.util.Iterator;

public class Testklient {
    public static void main(String[] args) {
        Kontroll kontroll = new Kontroll();
        Vare vare = new Vare(1,"Eske",10);
        kontroll.nyVare(1,vare);
        vare = new Vare(2,"Boks",5);
        kontroll.nyVare(2,vare);

        Iterator<Vare> varene =  kontroll.getVarer();

        while(varene.hasNext()){
            System.out.println(varene.next());
        }
        System.out.println("");

        //Tester getVare
        vare=kontroll.getVare(2);
        System.out.println(vare.toString());
        System.out.println("");

        //Tester endreBeholdning
        kontroll.endreBeholdning(1,-5);
        varene=kontroll.getVarer();

        while (varene.hasNext()){
            System.out.println(varene.next());
        }
        System.out.println("");


        //Tester sletting
        kontroll.removeVare(2);
        varene=kontroll.getVarer();

        while (varene.hasNext()){
            System.out.println(varene.next());
        }
        System.out.println("");

    }


}
