module com.example.demosingleton {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;


    opens com.example.demosingleton to javafx.fxml;
    exports com.example.demosingleton;
}