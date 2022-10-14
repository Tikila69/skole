public class Person {
    //Attributter
    String navn;

    //Konstruktør
    public Person(String navn) {
        //Attributtets navn settes til parameterern navn
        this.navn=navn;
    }

    public String toString() {
        return "************+\n" + navn + "\n************";
    }
}
