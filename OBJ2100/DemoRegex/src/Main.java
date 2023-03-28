import javax.swing.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author Didrik
 * @return void
 * @param
 */
public class Main {

    private static final String EMAIL_PATTERN = "^(?=.{1,64}@)[A-Za-z0-9_-]+(\\\\.[A-Za-z0-9_-]+)*@[^-][A-Za-z0-9-]+(\\\\.[A-Za-z0-9-]+)*(\\\\.[A-Za-z]{2,})$";
    private static Pattern mønster = Pattern.compile(EMAIL_PATTERN);
    private static Matcher matcher;
    public static void main(String[] args) {
        String epost = "didrik@hotmail.com";
        sjekkEpost(epost);
    }

    public static boolean validate(final String epost) {

        matcher = mønster.matcher(epost);

        return matcher.matches();
    }

    public static void sjekkEpost(String epost) {
        boolean gyldig = validate(epost);
        if (gyldig){
            JOptionPane.showMessageDialog(null,"Eposten " + epost + " er gyldig.");
        } else {
            JOptionPane.showMessageDialog(null,"Eposten " + epost + " er ugyldig.");
        }
    }
}