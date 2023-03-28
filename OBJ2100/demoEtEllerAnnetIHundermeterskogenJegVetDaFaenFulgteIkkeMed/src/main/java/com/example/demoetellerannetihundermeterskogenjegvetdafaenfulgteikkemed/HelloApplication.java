package com.example.demoetellerannetihundermeterskogenjegvetdafaenfulgteikkemed;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    private Stage vindu;
    private Scene scene1, scene2;
    private TableView tabell;
    private TextField txtNavn, txtAdresse, txtTelefon;
    //ObservableList for personobjekter:
    private ObservableList<Person> data = FXCollections.observableArrayList(
            new Person("Didrik","Benterud","95767711"),
            new Person("Robin","Byen","42069420"));
    @Override
    public void start(Stage stage) throws IOException {
        try {
            vindu = stage;
            lageScene1();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public void lageScene1(){
        BorderPane rotpanel = new BorderPane();
        scene1 = new Scene(rotpanel,400,300);
        vindu.setTitle("Enkel Tabell");
        vindu.setWidth(400);
        vindu.setHeight(300);
        tabell = new TableView<>();
        TableColumn colnavn = new TableColumn<>("Navn:");
        colnavn.setMinWidth(100);
        colnavn.setCellFactory(new PropertyValueFactory<Person, String>("navn"));

        TableColumn coladresse = new TableColumn<>("Adresse:");
        coladresse.setMinWidth(100);
        coladresse.setCellFactory(new PropertyValueFactory<Person, String>("adresse"));

        TableColumn coltelefon = new TableColumn<>("Telefon:");
        coltelefon.setMinWidth(100);
        coltelefon.setCellFactory(new PropertyValueFactory<Person, String>("telefon"));

        lageScene2();
        Button ny = new Button("Ny Person");
        ny.setOnAction(e-> vindu.setScene(scene2));
        tabell.getColumns().addAll(colnavn,coladresse,coltelefon);
        tabell.setItems(data);
        rotpanel.setCenter(tabell);
        rotpanel.setBottom(ny);
        vindu.show();
    }

    public void lageScene2(){
        GridPane root = new GridPane();

    }

    public static void main(String[] args) {
        launch();
    }
}