package Applikasjon;

import java.io.Serializable;
import java.text.Collator;
import java.util.ArrayList;
import java.util.List;

public class Person implements Serializable, Comparable<Person>{
    private String enavn,fnavn,gateadresse;
    //Referanse til postadresseobjekt:
    private Postadresse postadresse;
    //Liste med refaranser til de bilene vedkommende eier
    List<Bil> biler = new ArrayList<Bil>();
    //Kollator
    private final static Collator KOLLATOR  = Collator.getInstance();

    public Person(String enavn, String fnavn, String gateadresse, Postadresse postadresse) {
        this.enavn = enavn;
        this.fnavn = fnavn;
        this.gateadresse = gateadresse;
        this.postadresse = postadresse;
    }

    public String getEnavn() {
        return enavn;
    }

    public void setEnavn(String enavn) {
        this.enavn = enavn;
    }

    public String getFnavn() {
        return fnavn;
    }

    public void setFnavn(String fnavn) {
        this.fnavn = fnavn;
    }

    public String getGateadresse() {
        return gateadresse;
    }

    public void setGateadresse(String gateadresse) {
        this.gateadresse = gateadresse;
    }

    public Postadresse getPostadresse() {
        return postadresse;
    }

    public void setPostadresse(Postadresse postadresse) {
        this.postadresse = postadresse;
    }

    public List<Bil> getBiler() {
        return biler;
    }

    public void regBil(Bil b){
        biler.add(b);
    }

    @Override
    public String toString() {
        return "Person{" +
                "enavn='" + enavn + '\'' +
                ", fnavn='" + fnavn + '\'' +
                ", gateadresse='" + gateadresse + '\'' +
                ", postadresse=" + postadresse +
                ", biler=" + biler +
                '}';
    }
    public String toFile(){
        return enavn+";"+fnavn+";"+gateadresse+";"+postadresse+";"+postadresse.getPostnr();
    }

    public String alleBiler(){
        String bilut="";
        for (int i=0;i<biler.size();i++){
            bilut+=biler.get(i).toString();
            bilut+="\n";
        }
        return bilut;
    }
    @Override
    public int compareTo(Person o) {
        return KOLLATOR.compare(this.enavn,o.getEnavn());
    }
}
