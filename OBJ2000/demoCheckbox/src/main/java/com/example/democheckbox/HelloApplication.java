package com.example.democheckbox;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.CheckBox;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    CheckBox box1, box2, box3;
    @Override
    public void start(Stage stage) throws IOException {

        BorderPane root = new BorderPane();
        VBox knappepanel = new VBox();

        root.setLeft(knappepanel);

        box1= new CheckBox("OBJ2000");
        box2= new CheckBox("PRG1000");
        box3= new CheckBox("PRG1100");

        knappepanel.getChildren().addAll(box1,box2,box3);

        box1.setOnAction(e -> behandlerBox1());
        box2.setOnAction(e -> behandlerBox2());
        box3.setOnAction(e -> behandlerBox3());

        Scene scene = new Scene(root, 400, 400);
        stage.setTitle("Checkbox!");
        stage.setScene(scene);
        stage.show();
    }

    public void behandlerBox1() {
        System.out.println("Du valgte OBJ2000");
    }

    public void behandlerBox2() {
        System.out.println("Du valgte PRG1000");
    }

    public void behandlerBox3() {
        System.out.println("Du valgte PRG1100");
    }

    public static void main(String[] args) {
        launch();
    }
}