public class Ansatt {
    private String navn;
    private Ansattforhold status;

    public Ansatt(String navn, Ansattforhold status) {
        this.navn = navn;
        this.status = status;
    }

    public String getNavn() {
        return navn;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public Ansattforhold getStatus() {
        return status;
    }

    public void setStatus(Ansattforhold status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "Ansatt{" +
                "navn='" + navn + '\'' +
                ", status=" + status +
                '}';
    }
}
