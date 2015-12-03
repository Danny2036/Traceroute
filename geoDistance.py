import socket
import urllib2
import re
from math import radians, cos, sin, asin, sqrt
#The longitude latidude caluclation came from stackoverflow this is the Haversine Formula

def getdistance(website):
    #Gets starting IP
    #homeaddress = socket.gethostbyname(socket.gethostname())
    #homepoints = getlongandladpoints(homeaddress)
    #Remove carraige return
    website = line.strip()
    webaddress = socket.gethostbyname(website)
    destpoints = getlongandladpoints(webaddress)
    return haversine(0,0, destpoints[0], destpoints[1])

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km

def getlongandladpoints(address):
    response = urllib2.urlopen('http://freegeoip.net/xml/' + str(address))
    xmlresponse = []
    #Get cordinates of home
    for line2 in response:
        xmlresponse.append(str(line2))
    latitudetag = xmlresponse[10]
    longitudetag = xmlresponse[11]
    #Coordinates of this machine
    latitude = float(latitudetag[latitudetag.index('>') + 1 :latitudetag.index('<', 2)])
    longitude = float(longitudetag[longitudetag.index('>') + 1 :longitudetag.index('<', 2)])
    point = [longitude, latitude]
    return point

if __name__ == "__main__":
    line = 'google.com'
    print(str(getdistance(line)))

    targetwebsites = open('targets.txt')
    for line in targetwebsites:
        #Remove carraige return
        print(line.strip() +' is ' + str(getdistance(line.strip())) + 'km away.')
    print('Done with everything')