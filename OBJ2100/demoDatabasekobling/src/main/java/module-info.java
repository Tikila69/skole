module com.example.demodatabasekobling {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demodatabasekobling to javafx.fxml;
    exports com.example.demodatabasekobling;
}