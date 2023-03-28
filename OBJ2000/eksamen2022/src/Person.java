public class Person implements Comparable<Person>{

    private long personnummer;
    private String navn;
    private String adresse;

    public Person(long personnummer, String navn, String adresse) {
        this.personnummer = personnummer;
        this.navn = navn;
        this.adresse = adresse;
    }

    public long getPersonnummer() {
        return personnummer;
    }

    public void setPersonnummer(long personnummer) {
        this.personnummer = personnummer;
    }

    public String getNavn() {
        return navn;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public int compareTo(Person denandre){
        if (this.personnummer>denandre.getPersonnummer()) return 1;
        else if (this.personnummer<denandre.getPersonnummer()) return -1;
        else return 0;
    }

    public boolean equals(Person denadre) {
        if(this.personnummer==denadre.getPersonnummer()) return true;
        else return false;
    }

    @Override
    public String toString() {
        return "Person{" +
                "personnummer=" + personnummer +
                ", navn='" + navn + '\'' +
                ", adresse='" + adresse + '\'' +
                '}';
    }
}





