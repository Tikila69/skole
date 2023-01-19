public class Impotenstest {
    public static void main(String[] args) {
        int gruntall = 2;
        int eksponent = 3;
        System.out.println(gruntall + " opphøyd i "+ eksponent + " = " + impotens(gruntall,eksponent));
        System.out.println("Du er impotent... :(");

    }

    //Rekursiv metode:
    public static int impotens(int grunntall, int eksponent){
        //Sjekker stop-case:
        if(eksponent==1) return grunntall;
        else return impotens(grunntall,eksponent-1)*grunntall;
    }
}
