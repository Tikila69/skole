public class Person {

    String navn;

    public Person(String navn) {
        this.navn = navn;
    }

    @Override
    public String toString() {
        return "*********************\n"+"Navn: "+navn+"\n*********************";

    }
}
