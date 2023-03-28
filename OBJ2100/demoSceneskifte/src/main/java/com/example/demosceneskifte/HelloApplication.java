package com.example.demosceneskifte;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.Border;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    Scene scene1, scene2;
    @Override
    public void start(Stage stage) throws IOException {
        BorderPane root = new BorderPane();

        //Scene 1
        Label label1 = new Label("Dette er scene 1");
        Button knapp1 = new Button("Neste Scene");
        knapp1.setOnAction(e-> stage.setScene(scene2));
        VBox layout1 = new VBox(20);
        layout1.getChildren().addAll(label1,knapp1);
        scene1 = new Scene(layout1, 320, 240);

        //Scene 2
        Label label2 = new Label("Dette er scene 2");
        Button knapp2 = new Button("Neste Scene");
        knapp2.setOnAction(e-> stage.setScene(scene1));
        VBox layout2 = new VBox(20);
        layout2.getChildren().addAll(label2,knapp2);
        scene2 = new Scene(layout2, 320, 240);



        stage.setTitle("Scenehelvette");
        stage.setScene(scene1);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}