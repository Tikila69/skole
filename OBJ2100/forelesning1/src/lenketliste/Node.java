package lenketliste;

//Klassen Node er genersik
public class Node<Type> {
    //Definerer objektet:
    private Type objekt;
    //Referanse til neste node:
    private Node<Type> neste;

    //Konstruktør:
    public Node(Type objekt){
        this.objekt = objekt;
        neste = null; //Greit å lære å gjøre da ikke alle språk har null som default
    }

    //Metode for å returnere objekt
    public Type getInnhold(){
        return objekt;
    }


    //Metode for å hente referanse til neste node:
    public Node<Type> getNeste(){
        return neste;
    }

    //Metode for å sette referanse for neste node:
    public void setNeste(Node<Type> neste) {
        this.neste=neste;
    }
}
