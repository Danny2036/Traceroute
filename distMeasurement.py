import socket


def main(destinationame):
    destinationaddress = socket.gethostbyname(destinationame)
    port = 33434
    maxnumhops = 30
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 1
    while True:
        recevingsocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        sendingsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        sendingsocket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        recevingsocket.bind(("", port))
        sendingsocket.sendto("", (destinationame, port))
        currentaddress = None
        currentname = None
        try:
            _, currentaddress = recevingsocket.recvfrom(512)
            currentaddress = currentaddress[0]
            try:
                currentname = socket.gethostbyaddr(currentaddress)[0]
            except socket.error:
                currentname = currentaddress
        except socket.error:
            pass
        finally:
            sendingsocket.close()
            recevingsocket.close()

        if currentaddress is not None:
            currenthost = "%s (%s)" % (currentname, currentaddress)
        else:
            currenthost = "*"
        print("%d\t%s" % (ttl, currenthost))

        ttl += 1
        if currentaddress == destinationaddress or ttl > maxnumhops:
            break


if __name__ == "__main__":
    targetwebsites = open('targets.txt')
    for line in targetwebsites:
        main('line')
    print('Done')
