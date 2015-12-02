import socket


def main(destinationName):
    destinationAddress = socket.gethostbyname(destinationName)
    port = 33434
    maxNumHops = 30
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 1
    while True:
        receivingSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        sendingSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        sendingSocket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        receivingSocket.bind(("", port))
        sendingSocket.sendto("", (destinationName, port))
        currentAddress = None
        currentName = None
        try:
            _, currentAddress = receivingSocket.recvfrom(512)
            currentAddress = currentAddress[0]
            try:
                currentName = socket.gethostbyaddr(currentAddress)[0]
            except socket.error:
                currentName = currentAddress
        except socket.error:
            pass
        finally:
            sendingSocket.close()
            receivingSocket.close()

        if currentAddress is not None:
            currentHost = "%s (%s)" % (currentName, currentAddress)
        else:
            currentHost = "*"
        print("%d\t%s" % (ttl, currentHost))

        ttl += 1
        if currentAddress == destinationAddress or ttl > maxNumHops:
            break


if __name__ == "__main__":
    main('google.com')
    print('Done')
