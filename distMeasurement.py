import socket


def main(destinationame):
    print('Looking for ' + destinationame)
    destinationaddress = socket.gethostbyname(destinationame)
    port = 33434
    maxnumhops = 30
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 1
    timeoutlength = 1
    while True:
        currentaddress = None
        currentname = None
        recevingsocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        recevingsocket.bind(("", port))
        recevingsocket.settimeout(timeoutlength)
        sendingsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        sendingsocket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        sendingsocket.sendto("", (destinationame, port))
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
            currenthost = "*Timed out"
        print("%d\t%s" % (ttl, currenthost))

        ttl += 1
        if currentaddress == destinationaddress or ttl > maxnumhops:
            break


if __name__ == "__main__":
    #targetwebsites = open('targets.txt')
    #for line in targetwebsites:
    #    main('line')
    #    print('Done with ' + line)
    #print('Done with everything')
    main('google.com')