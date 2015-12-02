import socket
import time
#Referenced Ksplice blog tutorial on tracerouting
#Referenced Silver moon raw socker programming in python

def main(destinationame, retrynumber):
    start = time.time()
    #If it does not does not recive a response after 3 attempts, stop trying
    if retrynumber < 3:
        print('Looking for ' + destinationame + '. Attempt ' + str(retrynumber))
        #Gets ip address based off of name
        destinationaddress = socket.gethostbyname(destinationame)
        port = 33434
        maxnumhops = 128
        ttl = 1
        icmp = socket.getprotobyname('icmp')
        udp = socket.getprotobyname('udp')
        timeoutlength = 1
        timeoutcount = 0
        while True:
            currentaddress = None
            currentname = None
            #Creates a socket to listen for responses
            recevingsocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
            recevingsocket.bind(("", port))
            recevingsocket.settimeout(timeoutlength)
            #Creates a socket that will be sending out requests
            sendingsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
            sendingsocket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
            sendingsocket.sendto("", (destinationame, port))
            try:
                _, currentaddress = recevingsocket.recvfrom(512)
                currentaddress = currentaddress[0]
                try:
                    #Tries to get a name for ip address the is more than numbers
                    currentname = socket.gethostbyaddr(currentaddress)[0]
                except socket.error:
                    #If no name to use, set the name to the ip address
                    currentname = currentaddress
            except socket.error:
                pass
            finally:
                sendingsocket.close()
                recevingsocket.close()

            if currentaddress is not None:
                #If something is returned on the recieving socket
                currenthost = "%s (%s)" % (currentname, currentaddress)
                #If this prints it means something was recived and the timeouts were broken
                timeoutcount = 0
            else:
                currenthost = "*Timed out"
                timeoutcount += 1
            print("%d\t%s" % (ttl, currenthost))

            if timeoutcount > 5:
                #If not enough response retry from the beginning
                print('Could not reach destination. Starting again.')
                if retrynumber + 1 > 2:
                    end = time.time()
                    print('Timed out after '+ str(ttl) + ' hops in ' + str(end-start) + 'seconds')
                main(destinationame, retrynumber +1)
                break

            ttl += 1
            if currentaddress == destinationaddress or ttl > maxnumhops:
                #If the destination is found or the number of hops has been exceeded then end
                print('The destination was reached in '+ str(ttl) + ' hops in ' + str(end-start) + 'seconds')
                break
    else:
        return


if __name__ == "__main__":
    targetwebsites = open('targets.txt')
    for line in targetwebsites:
        #Remove carraige return
        main(line.strip(), 0)
        print('Done with ' + line)
    print('Done with everything')
    #main('google.com')