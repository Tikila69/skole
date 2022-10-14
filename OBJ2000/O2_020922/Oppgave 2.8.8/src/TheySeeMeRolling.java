public class TheySeeMeRolling {

    public static void main(String[] args) {
        String x = "Gi";
        String y = "Nå";
        String z = "Faen";
        String rest = "";


        for (int i = 0;i<4 ;i++) {
            System.out.println("x = "+x);
            System.out.println("y= "+y);
            System.out.println("z= "+z);
            System.out.println("----------");

            rest = x;
            x = y;
            y = z;
            z = rest;

        }
    }
}
