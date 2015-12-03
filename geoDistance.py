import socket
import http.client

if __name__ == "__main__":
    targetwebsites = open('targets.txt')
    for line in targetwebsites:
        #Remove carraige return
        website = line.strip()
        webaddres = socket.gethostbyname(website)
        h = http.client.HTTPConnection('http://freegeoip.net/xml/' + str(webaddres), 80).connect()
        response = h.getresponse()
        for line2 in response:
            print(str(line2))
        print(h)
    print('Done with everything')