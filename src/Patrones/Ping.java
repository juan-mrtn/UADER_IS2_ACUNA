public class Ping {
    public void execute(String ip) {
        if (ip.startsWith("192.")) {
            System.out.println("Ejecutando ping seguro a: " + ip);
            doPing(ip);
        } else {
            System.out.println("Dirección IP no permitida.");
        }
    }

    public void executeFree(String ip) {
        System.out.println("Ejecutando ping libre a: " + ip);
        doPing(ip);
    }

    private void doPing(String ip) {
        for (int i = 0; i < 10; i++) {
            System.out.println("Ping " + (i+1) + " a " + ip);
        }
    }
}