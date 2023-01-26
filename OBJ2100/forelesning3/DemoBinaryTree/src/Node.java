public class Node {
    private int verdi;
    private Node venstre;
    private Node høyre;
    private Node forelder;

    public Node (int verdi){
        this.verdi=verdi;
    }

    public Node(int verdi, Node forelder) {
        this.verdi = verdi;
        this.forelder=forelder;
    }

    //Rekursiv metode for å sette inn nye noder (med verdi):
    public void settInn(int nyVerdi) {
        //Hvis verdien i noden er større enn nyVerdi: Vi går til venstre.
        if(verdi >= nyVerdi){

            //Sjekker først om det er en node til ventre:
            if(venstre!= null) {
                //Det er noe til venstre, og vi gjør et rekursivt tall på settInn:
                venstre.settInn(nyVerdi);
            }
            else {
                //Det er ikke en node til venstre:
                venstre=new Node(nyVerdi,this);
            }
        }
        else {
            if(høyre!=null) {
                høyre.settInn(nyVerdi);
            }
            else{
                høyre=new Node(nyVerdi,this);
            }
        }
    }

    public boolean søkVerdi(int søkeverdi) {
        if (verdi == søkeverdi)
            return true;
        if (verdi>=søkeverdi) {
            if (venstre != null) {
                return venstre.søkVerdi(søkeverdi);
            } else {
                return false;
            }
        }
        else{
            if (høyre!=null) {
                return høyre.søkVerdi(søkeverdi);
            }
            else return false;
        }
    }

    public String toString(){
        String retur = "";
        if (venstre!=null){
            retur =retur+venstre.toString();
        }
        if (høyre!=null){
            retur=retur+høyre.toString();
        }
        return retur;
    }
}
