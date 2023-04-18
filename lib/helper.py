# Diese Funktionen helfen dir komplexere Dinge zu erledigen.
# Sie kümmern sich zum Beispiel um die Verbindung zum WLAN
# oder aktualisieren die interne Uhr des Mikrocontrollers.


def connect_to_wlan(wlan_name, wlan_password):
    """
    connect_to_wlan() stellt die Verbindung zu einem WLAN-Netzwerk her.
    wlan_name: Name des WLANs
    wlan_passwort: Passwort des WLANs
    """
    import network

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect(wlan_name, wlan_password)
        while not wlan.isconnected():
            pass
    print("network config:", wlan.ifconfig())


def get_exact_time():
    """
    get_exact_time() fragt bei einem Online-Dienst nach der aktuellen,
    sehr genauen Uhrzeit.
    """
    import socket
    import struct
    import time

    host = "de.pool.ntp.org"
    NTP_DELTA = 3155673600

    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(10)
    res = s.sendto(NTP_QUERY, addr)
    msg = s.recv(48)
    s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    t = val - NTP_DELTA
    loc_time = time.localtime(t)
    return loc_time[0:3] + (0,) + loc_time[3:6] + (0,)


def set_exact_time(rtc: RTC):
    """
    set_exact_time() setzt die exakte, vorher abgefragte Uhrzeit in der
    internen Uhr des Mikrocontrollers.
    """
    ntptime = get_exact_time()

    rtc.datetime((ntptime))  # should be ntp time
    print(rtc.datetime())
