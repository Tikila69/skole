package com.example.demodatabasekobling;


public class Main{
    Kontroll kontroll = new Kontroll();
    private TableView tabell = new TableView();
    private ObservableList<Kunde> data = FXCollections.observableArrayList();
    TextField nyttFnavn;
    TextField nyttEnavn;
    TextField nyadresse;
    TextField nyttPnr;
    TextField nyttKjønn;

    public Main() {
    }

    public void start(Stage vindu) {
        try {
            this.kontroll.lagForbindelse();
            BorderPane rotpanel = new BorderPane();
            Scene scene = new Scene(rotpanel, 900.0, 600.0);
            vindu.setTitle("Ansattabell");
            vindu.setWidth(900.0);
            vindu.setHeight(600.0);
            TableColumn kundenr = new TableColumn("Kundenr:");
            kundenr.setMinWidth(10.0);
            kundenr.setCellValueFactory(new PropertyValueFactory("kundenr"));
            TableColumn fornavn = new TableColumn("Fornavn:");
            fornavn.setMinWidth(150.0);
            fornavn.setCellValueFactory(new PropertyValueFactory("fornavn"));
            TableColumn etternavn = new TableColumn("Etternavn");
            etternavn.setMinWidth(150.0);
            etternavn.setCellValueFactory(new PropertyValueFactory("etternavn"));
            TableColumn adresse = new TableColumn("Adresse:");
            adresse.setMinWidth(150.0);
            adresse.setCellValueFactory(new PropertyValueFactory("adresse"));
            TableColumn postnr = new TableColumn("Postnr:");
            postnr.setMinWidth(150.0);
            postnr.setCellValueFactory(new PropertyValueFactory("postnr"));
            TableColumn kjønn = new TableColumn("Kjønn:");
            kjønn.setMinWidth(10.0);
            kjønn.setCellValueFactory(new PropertyValueFactory("kjønn"));
            this.tabell.getColumns().addAll(new Object[]{kundenr, fornavn, etternavn, adresse, postnr, kjønn});
            this.tabell.setItems(this.data);
            Label overskrift = new Label("Kundeliste");
            FlowPane registreringspanel = new FlowPane();
            this.nyttKnr.set(new TextField());
            this.nyttKnr.get().setPromptText("Kundenr:");
            this.nyttKnr.get().setMaxWidth(kundenr.getPrefWidth());
            this.nyttFnavn = new TextField();
            this.nyttFnavn.setPromptText("Navn: ");
            this.nyttFnavn.setMaxWidth(fornavn.getPrefWidth());
            this.nyttEnavn = new TextField();
            this.nyttEnavn.setPromptText("Etternavn: ");
            this.nyttEnavn.setMaxWidth(etternavn.getPrefWidth());
            this.nyadresse = new TextField();
            this.nyadresse.setPromptText("Adresse: ");
            this.nyadresse.setMaxWidth(adresse.getPrefWidth());
            this.nyttPnr = new TextField();
            this.nyttPnr.setPromptText("Postnr:");
            this.nyttPnr.setMaxWidth(postnr.getPrefWidth());
            this.nyttKjønn = new TextField();
            this.nyttKjønn.setPromptText("Kjønn");
            this.nyttKjønn.setMaxWidth(kjønn.getPrefWidth());
            Button nyknapp = new Button("Legg til");
            nyknapp.setOnAction((e) -> {
                this.behandleNy();
            });
            rotpanel.setTop(overskrift);
            rotpanel.setCenter(this.tabell);
            rotpanel.setBottom(registreringspanel);
            registreringspanel.getChildren().addAll(new Node[]{this.nyttKnr.get(), this.nyttFnavn, this.nyttEnavn, this.nyadresse, this.nyttPnr, this.nyttKjønn, nyknapp});
            this.hentKunder();
            vindu.setScene(scene);
            vindu.show();
        } catch (Exception var13) {
            var13.printStackTrace();
        }

    }

    public void behandleNy() {
        try {
            this.kontroll.oppdaterKunde(this.nyttKnr.get().getText(), this.nyttFnavn.getText(), this.nyttEnavn.getText(), this.nyadresse.getText(), this.nyttPnr.getText(), this.nyttKjønn.getText());
            this.hentKunder();
        } catch (Exception var2) {
            System.out.println(var2.getMessage());
        }

        this.nyttKnr.get().clear();
        this.nyttFnavn.clear();
        this.nyttEnavn.clear();
        this.nyadresse.clear();
        this.nyttPnr.clear();
        this.nyttKjønn.clear();
    }

    public void hentKunder() {
        this.data.clear();

        try {
            ResultSet resultat = this.kontroll.lesKunder();

            while(resultat.next()) {
                ObservableList rad = FXCollections.observableArrayList();
                int kundenr = resultat.getInt(1);
                String fnavn = resultat.getString(2);
                String enavn = resultat.getString(3);
                String adr = resultat.getString(4);
                String postnr = resultat.getString(5);
                String kjønn = resultat.getString(6);
                this.data.add(new Kunde(kundenr, fnavn, enavn, adr, postnr, kjønn));
            }
        } catch (Exception var9) {
            System.out.println(var9.getMessage());
        }

    }

    public static void main(String[] args) {
        launch(args);
    }
}
