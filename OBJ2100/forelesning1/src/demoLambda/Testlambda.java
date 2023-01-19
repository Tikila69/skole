package demoLambda;

public class Testlambda {
    public static void main(String[] args) {
        //Lager et kalkulatorobjekt for addisjon:
        Kalkulator addisjon = (a,b) -> a + b;
        //Subtrasjon:
        Kalkulator subtraksjon = (a,b) -> a - b;
        //Multiplikasjon:
        Kalkulator multiplikasjon = (a,b) -> a * b;
        //Divisjon:
        Kalkulator divisjon = (a,b) -> a / b;

        //Det vi har gjort er å definere innnholde i metoden operasjon for fire kalkulatorer.

        //Vi kan nå bruke kalkulatorene:
        System.out.println("Addisjon: " + addisjon.operasjon(7,2));
        System.out.println("Subtraksjon: " + subtraksjon.operasjon(7,2));
        System.out.println("Multiplikasjon: " + multiplikasjon.operasjon(7,2));
        System.out.println("Divisjon: " + divisjon.operasjon(7,2));
    }
}
