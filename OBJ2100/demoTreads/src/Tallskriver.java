public class Tallskriver extends Thread {

    private int tall;

    public Tallskriver(int tall){
        this.tall = tall;
    }

    //overstyrer metoden run:
    public void run() {
        //Starter en evig løkke:
        while (true){
            System.out.print(tall);
            //Legger inn en forsinkelse:
            try {
                Thread.sleep(10);
            }catch (InterruptedException e){
            }
            System.out.print("");
        }
    }
}
