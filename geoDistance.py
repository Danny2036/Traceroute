import socket
import urllib2

if __name__ == "__main__":
    targetwebsites = open('targets.txt')
    for line in targetwebsites:
        #Remove carraige return
        website = line.strip()
        webaddres = socket.gethostbyname(website)
        response = urllib2.urlopen('http://freegeoip.net/xml/' + str(webaddres))
        for line2 in response:
            print(str(line2))
        print(h)
    print('Done with everything')