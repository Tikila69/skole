public class Binærtre {
    private Node root; //roten i treet

    public void settInn(int verdi){
        //Sjekker om det er noe i treet:
        if (root!=null){
            root.settInn(verdi);
        }
        else{
            root= new Node(verdi);
        }
    }

    public boolean søkVerdi(int verdi) {
        //Sjekker om treet er tomt:
        if (root==null) return false;
        else return root.søkVerdi(verdi);
    }

    public String toString(){
        if (root!=null) return root.toString();
        else return null;
    }
}
