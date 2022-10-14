public class Testklient {
    public static void main(String[] args) {

        //Ved å sette <String> vil alle steder det står Type i koden bli byttet ut med String
        GeneriskStack <String> stack = new GeneriskStack<>();

        //Legger inn navn i objektene
        stack.push("Kongsberg");
        stack.push("Drammen");
        stack.push("Hønefoss");

        //Tester på hva som ligger øverst is stacken
        System.out.println("Øverst i stacken: "+stack.peep());
        System.out.println("");

        //Skriver ut hele stacken
        System.out.println("Hele stacken før pop:");
        Object[] byliste = stack.getInnhold();
        for (int i= byliste.length-1;i>-1;i--) {
            System.out.println(byliste[i]);
        }
        System.out.println("");

        //Fjerner siste/øveste objekt i stacken
        System.out.println("Fjerner øveste by: "+stack.pop());
        System.out.println("");

        //Skriver ut stacken på nytt:
        byliste=stack.getInnhold();
        System.out.println("Dette er stacken etter pop:");
        for (int i= byliste.length-1;i>-1;i--) {
            System.out.println(byliste[i]);
        }
    }
}
