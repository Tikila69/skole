package Stjerner;

public class Tengekontroll {
    public String tegnTrekant(int antall) {
        //lager en tom string
        String tegning = "";
        int antallStjerner = 1;
        System.out.println("Du er inne i tegnTrekant()");

        for (int i=0;i<antall+1;i++){
            System.out.println("Du er inne i første løkke i tegnTrekant()");
            for (int n=1;n<antallStjerner+1;n++){
                System.out.println("Du er inne i andre løkke i tegnTrekant()");
                tegning+="*";
            }
            antallStjerner++;
            //Legger til linjeskift:
            tegning+="\n";
        }
        //Returnerer tegningen
        return tegning;
    }

    public String tegnPyramide(int antall) {
        String tegning = "";


        for (int i = 1; i<antall*2;i+=2){

            for (int j=0;j<(antall-i/2);j++){
                tegning+=" ";
            }

            for (int k = 0;k<i;k++){
                tegning+="*";
            }
            tegning+="\n";
        }

        return tegning;
    }
}
