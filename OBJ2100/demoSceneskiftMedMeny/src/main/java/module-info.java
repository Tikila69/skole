module oppgave.demosceneskiftmedmeny {
    requires javafx.controls;
    requires javafx.fxml;


    opens oppgave.demosceneskiftmedmeny to javafx.fxml;
    exports oppgave.demosceneskiftmedmeny;
}