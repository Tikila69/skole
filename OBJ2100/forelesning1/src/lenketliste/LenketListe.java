package lenketliste;

public class LenketListe<Type> {

    //DEKLARERER STARTEN PÅ EN LISTE SOM BESTÅR AV NODER

    private Node<Type> hode;

    //Metode for å sette inn en ny node:
    public void settInn(Type objekt){
        //Vi må alltid sjekke om det er noe i listen:
        if(hode == null) hode=new Node(objekt);
        //Ellers settes inn først:
        {
            //Definerer Node for å "huske" hodet:
            Node<Type> husk = hode;
            //Lager en ny node:
            hode = new Node<>(objekt);
            hode.setNeste(husk);
        }
    }

    //Metode for å slette neste node:
    public void sletteFørste(){
        if (hode!=null) hode=hode.getNeste();
    }


}
