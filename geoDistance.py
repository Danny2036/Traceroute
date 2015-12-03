import socket
import urllib2
from math import radians, cos, sin, asin, sqrt

def getdistance(website):
    #Gets starting IP
    homeaddress = socket.getprotobyname(socket.gethostname())
    homepoints = getlongandladpoints(homeaddress)
    #Remove carraige return
    website = line.strip()
    webaddress = socket.gethostbyname(website)
    destpoints = getlongandladpoints(webaddress)
    return haversine(homepoints[0], homepoints[1], destpoints[0], destpoints[1])

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
    for line2 in homeresponse:
        xmlresponse.append(str(line2))
    latitudetag = xmlresponse[10]
    longitudetag = xmlresponse[11]
    #Coordinates of this machine
    latitude = float(latitudetag[10:17])
    longitude = float(longitudetag[10:17])
    return point[longitude, latitude]

if __name__ == "__main__":
    line = 'google.com'
    print(str(getdistance(line)))
    print('Done with everything')