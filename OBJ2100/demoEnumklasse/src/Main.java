public class Main {
    public static void main(String[] args) {
        Ansatt a1 = new Ansatt("Didrik",Ansattforhold.FAST);
        Ansatt a2 = new Ansatt("Robin",Ansattforhold.MIDLERTIDIG);
        Ansatt a3 = new Ansatt("Roman",Ansattforhold.PROSJEKT);
        System.out.println(a1.getNavn());
        System.out.println(a1.getStatus());
        System.out.println(a1.toString());
        System.out.println();
        System.out.println(a2.getNavn());
        System.out.println(a2.getStatus());
        System.out.println(a2.toString());
        System.out.println();
        System.out.println(a3.getNavn());
        System.out.println(a3.getStatus());
        System.out.println(a3.toString());
    }
}