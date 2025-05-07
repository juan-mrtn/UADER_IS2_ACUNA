import java.util.ArrayList;
import java.util.List;

interface Componente {
    void mostrar(String indent);
}

class Pieza implements Componente {
    private String nombre;
    public Pieza(String nombre) {
        this.nombre = nombre;
    }
    public void mostrar(String indent) {
        System.out.println(indent + "- Pieza: " + nombre);
    }
}

class SubConjunto implements Componente {
    private String nombre;
    private List<Componente> componentes = new ArrayList<>();
    public SubConjunto(String nombre) {
        this.nombre = nombre;
    }
    public void agregar(Componente c) {
        componentes.add(c);
    }
    public void mostrar(String indent) {
        System.out.println(indent + "+ SubConjunto: " + nombre);
        for (Componente c : componentes) {
            c.mostrar(indent + "  ");
        }
    }
}

public class CompositeDemo {
    public static void main(String[] args) {
        SubConjunto prod = new SubConjunto("Producto Principal");
        for (int i = 1; i <= 3; i++) {
            SubConjunto sub = new SubConjunto("SubConjunto " + i);
            for (int j = 1; j <= 4; j++) {
                sub.agregar(new Pieza("Pieza " + i + "." + j));
            }
            prod.agregar(sub);
        }
        SubConjunto extra = new SubConjunto("SubConjunto Extra");
        for (int j = 1; j <= 4; j++) {
            extra.agregar(new Pieza("Pieza Extra." + j));
        }
        prod.agregar(extra);
        prod.mostrar("");
    }
}