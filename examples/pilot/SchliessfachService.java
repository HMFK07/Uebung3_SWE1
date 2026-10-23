/** Künstliches Pilotbeispiel. Die Doppelreservierung ist absichtlich fehlerhaft. */
public class SchliessfachService {
    private boolean belegt;

    public boolean reservieren() {
        if (belegt) {
            return true; // ABSICHTLICHER DEFEKT: bereits belegt
        }
        belegt = true;
        return true;
    }

    public void freigeben() {
        belegt = false;
    }
}
