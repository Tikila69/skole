package com.example.demoreklangel;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

public class HelloApplication extends Application {


    public void start(Stage stage) {

        BorderPane root = new BorderPane();

        Rectangle rektangel = new Rectangle();

        rektangel.setX(150.0f);
        rektangel.setY(75.0f);

        rektangel.setWidth(200.0f);
        rektangel.setHeight(100.0f);

        rektangel.setFill(Color.RED);

        root.setCenter(rektangel);

        Scene scene = new Scene(root, 400, 400);
        stage.setScene(scene);
        stage.show();





    }

    public static void main(String[] args) {
        launch();
    }
}