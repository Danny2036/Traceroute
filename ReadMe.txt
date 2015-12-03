README
There are two programs here that will be run. Both methods do not need input as they are both self contained. 

	Then input do the distMeasurment main method takes two parameters. The first parameter is the name of a web-
site. Examples can be found within he target.txt file. The second input is the number of times the webpage has 
been attempted to visit. i.e. If you try to ping the website and fail twice the second input value would be 2.
After that the program will print to the system the trace of traversal to reach the destination then lastly 
print the destination, number of hops, and the time.
	The geoDistance takes no inputs and pulls from the target.txt file as well. This prints the webpage and the 
distance when run.
	Any outside sources that were used to complete this code are commented at the top of the file that used the
code that was unoriginal. 

Explain the technique you use to measure the hop distance from your machine to destination using a single probe.
	-The hop distance is done by counting each router that is visitied that is not the destination. So in my code
	 every time I visit a router, I increment the TTL by one

How you will match ICMP responses with the probes you are sending out?
	-You can send an ICMP echo request out, then listen for the response. If there is a response then it can get
	 marked, but if there is no response then that means that it was unsuccessful and would be marked failed.

(list all possible reasons you can think of for not getting the answer when probing an arbitrary host)
	-If a packets get lost in transit or there is an issue with connection the prevents conacting a host then that
	 will prevent an answer
	-Some hosts have it set to drop a packet when probed as a security measure to prevent malcious people from 
	 seeing parts of Networks and other services 

The best fit lines on the graph did not really display useful information, that is due to general outliers in the 
graphed.