module com.example.demoreklangel {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.demoreklangel to javafx.fxml;
    exports com.example.demoreklangel;
}