package Studentoversikt;

public class Testklient {
    //En testklient skal teste ut alle valgene
    //Som skal kunne foretas i et fremtidig grensesnitt

    public static void main(String[] args) {
        Oppgaveoversikt oversikt = new Oppgaveoversikt();

        //Oppretter to studenter:
        Student student = new Student("Lise",2);
        boolean ok =oversikt.nyStudent(student);
        if (!ok) System.out.println("Just no mate");

        student = new Student("Ole",0);
        oversikt.nyStudent(student);

        //Sorterer
        oversikt.sorter();

        //Søker:
        Student stud = oversikt.finnStudent("Ole");
        if(stud !=null) System.out.println(stud.toString());
        else System.out.println("Student ikke funnet");

        //Søke på en student som ikke finnes
        stud = oversikt.finnStudent("Petter");
        if(stud !=null) System.out.println(stud.toString());
        else System.out.println("Student ikke funnet");

    }
}
