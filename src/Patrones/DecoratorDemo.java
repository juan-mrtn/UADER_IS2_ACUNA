interface Numero {
    double getValor();
}

class NumeroBase implements Numero {
    private double valor;
    public NumeroBase(double valor) {
        this.valor = valor;
    }
    public double getValor() {
        return valor;
    }
}

abstract class OperacionDecorator implements Numero {
    protected Numero numero;
    public OperacionDecorator(Numero numero) {
        this.numero = numero;
    }
}

class Sumar2 extends OperacionDecorator {
    public Sumar2(Numero n) { super(n); }
    public double getValor() { return numero.getValor() + 2; }
}

class MultiplicarPor2 extends OperacionDecorator {
    public MultiplicarPor2(Numero n) { super(n); }
    public double getValor() { return numero.getValor() * 2; }
}

class DividirPor3 extends OperacionDecorator {
    public DividirPor3(Numero n) { super(n); }
    public double getValor() { return numero.getValor() / 3; }
}

public class DecoratorDemo {
    public static void main(String[] args) {
        Numero n = new NumeroBase(6);
        System.out.println("Base: " + n.getValor());
        Numero conSuma = new Sumar2(n);
        Numero conMult = new MultiplicarPor2(conSuma);
        Numero conDiv = new DividirPor3(conMult);
        System.out.println("Resultado final: " + conDiv.getValor());
    }
}