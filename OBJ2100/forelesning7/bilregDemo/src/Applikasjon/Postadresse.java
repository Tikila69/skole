package Applikasjon;

import java.io.Serializable;
import java.text.Collator;

public class Postadresse implements Serializable, Comparable<Postadresse>{
    private String postnr, poststed;
    private final static Collator KOLLATOR = Collator.getInstance();

    public Postadresse(String postnr, String poststed) {
        this.postnr = postnr;
        this.poststed = poststed;
    }

    public String getPostnr() {
        return postnr;
    }

    public void setPostnr(String postnr) {
        this.postnr = postnr;
    }

    public String getPoststed() {
        return poststed;
    }

    public void setPoststed(String poststed) {
        this.poststed = poststed;
    }

    @Override
    public String toString() {
        return "Postadresse{" +
                "postnr='" + postnr + '\'' +
                ", poststed='" + poststed + '\'' +
                '}';
    }

    public String toFile(){
        return postnr+";"+poststed;
    }

    public boolean equals(Postadresse p){
        return KOLLATOR.equals(this.postnr,p.getPostnr());
    }

    @Override
    public int compareTo(Postadresse o) {
        return KOLLATOR.compare(this.postnr,o.getPostnr());
    }
}
