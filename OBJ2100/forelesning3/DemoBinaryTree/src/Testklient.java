import com.sun.source.tree.BinaryTree;

public class Testklient {
    public static void main(String[] args) {
        Binærtre tre = new Binærtre();

        tre.settInn(5);
        tre.settInn(3);
        tre.settInn(1);
        tre.settInn(4);
        tre.settInn(7);

        System.out.println("Skriver ut innholdet i treet");
        System.out.println(tre.toString());

        //Sjekker søkemetoden

        System.out.println("Finnes 2 i treet? " + tre.søkVerdi(2));
        System.out.println("Finnes 5 i treet? " + tre.søkVerdi(5));

    }
}
