module com.example.listboxdemo {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.listboxdemo to javafx.fxml;
    exports com.example.listboxdemo;
}