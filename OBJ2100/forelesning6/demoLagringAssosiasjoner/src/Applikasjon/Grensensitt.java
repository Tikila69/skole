package Applikasjon;

import javax.swing.*;

public class Grensensitt {
    Bilregister kontroll = new Bilregister();
    public void lesFiler(){
        try {
            kontroll.lesAlleFiler();
        }catch (Exception e){
            JOptionPane.showMessageDialog(null,e.getMessage());
        }
    }
}