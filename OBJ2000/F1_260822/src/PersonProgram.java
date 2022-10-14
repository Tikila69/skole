public class PersonProgram {
    //Dette er selve programmet
    public static void main(String[] args) {
        //oppretter personobjekter
        Person p1 = new Person("Ole");
        Person p2 = new Person("Lise");
        System.out.println(p1.toString());
        System.out.println(p2.toString());
    }
}
