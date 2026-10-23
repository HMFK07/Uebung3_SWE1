/** Kleiner reproduzierbarer Regressionstest ohne Testframework. */
public class SchliessfachServiceTest {
    public static void main(String[] args) {
        SchliessfachService fach = new SchliessfachService();
        if (!fach.reservieren()) {
            throw new AssertionError("Erste Reservierung müsste gelingen");
        }
        if (fach.reservieren()) {
            throw new AssertionError("Zweite Reservierung muss abgelehnt werden");
        }
        System.out.println("Alle Tests bestanden");
    }
}
