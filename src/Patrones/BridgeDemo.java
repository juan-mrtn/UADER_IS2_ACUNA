interface TrenLaminador {
    void laminar();
}

class Tren5mts implements TrenLaminador {
    public void laminar() {
        System.out.println("Laminando plancha de 5 metros");
    }
}

class Tren10mts implements TrenLaminador {
    public void laminar() {
        System.out.println("Laminando plancha de 10 metros");
    }
}

class Lamina {
    protected TrenLaminador tren;
    public Lamina(TrenLaminador tren) {
        this.tren = tren;
    }
    public void producir() {
        tren.laminar();
    }
}

public class BridgeDemo {
    public static void main(String[] args) {
        Lamina l1 = new Lamina(new Tren5mts());
        Lamina l2 = new Lamina(new Tren10mts());
        l1.producir();
        l2.producir();
    }
}