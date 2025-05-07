import java.util.HashMap;
import java.util.Map;

class PiezaCompartida {
    private String tipo, color, textura;
    public PiezaCompartida(String tipo, String color, String textura) {
        this.tipo = tipo; this.color = color; this.textura = textura;
    }
    public void mostrar(int x, int y) {
        System.out.println("Tipo: " + tipo + ", Color: " + color + ", Textura: " + textura + " en (" + x + "," + y + ")");
    }
}

class PiezaFactory {
    private static Map<String, PiezaCompartida> pool = new HashMap<>();
    public static PiezaCompartida getPieza(String tipo, String color, String textura) {
        String key = tipo + color + textura;
        pool.putIfAbsent(key, new PiezaCompartida(tipo, color, textura));
        return pool.get(key);
    }
}

public class FlyweightDemo {
    public static void main(String[] args) {
        for (int i = 0; i < 1000; i++) {
            PiezaCompartida p = PiezaFactory.getPieza("tornillo", "gris", "metal");
            p.mostrar(i, i * 2);
        }
    }
}