public class PingProxy {
    private Ping ping = new Ping();

    public void execute(String ip) {
        if (ip.equals("192.168.0.254")) {
            ping.executeFree("www.google.com");
        } else {
            ping.execute(ip);
        }
    }
}