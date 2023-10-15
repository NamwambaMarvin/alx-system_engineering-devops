#What happens when you type google.com in your browser and press Enter
When you type google.com and press enter, there are a series of events that take place locally on your machine like listening of keys, autocomplete and many others. However these are too technical and our main point os interest is the process that takes place before we get the final response.

##DNS RESOLUTION

####What is a DNS?
The Domain Name System (DNS) is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses. DNS translates domain names to IP addresses so browsers can load Internet resources. (Cloud flare, Oct 2023)
####What is a DNS request?
A DNS query (also known as a DNS request) is a demand for information sent from a user's computer (DNS client) to a DNS server. In most cases a DNS request is sent, to ask for the IP address associated with a domain name. An attempt to reach a domain, is actually a DNS client querying the DNS servers to get the IP address, related to that domain.(clouddns.com, 2023)
####DNS Lookup
There are 8 steps in a DNS Look up.
1. A user types ‘example.com’ into a web browser and the query travels into the Internet and is received by a DNS recursive resolver.
2. The resolver then queries a DNS root nameserver (.).
3. The root server then responds to the resolver with the address of a Top Level Domain (TLD) DNS server (such as .com or .net), which stores the information for its domains. When searching for example.com, our request is pointed toward the .com TLD.
4. The resolver then makes a request to the .com TLD.
5. The TLD server then responds with the IP address of the domain’s nameserver, example.com.
6. Lastly, the recursive resolver sends a query to the domain’s nameserver.
7. The IP address for example.com is then returned to the resolver from the nameserver.
8. The DNS resolver then responds to the web browser with the IP address of the domain requested initially.
(Cloud flare, Oct 2023)

## CONNECTION TO THE SERVER
After the browser gets the ip address, since we queried using the browser, it will automatically try to establish a secure connection via port 80.
It uses http and https protocols exchange information between your browser and the server. Https is used to establish a secure connection.

Hypertext Transfer Protocol Secure (HTTPS) is an extension of the Hypertext Transfer Protocol (HTTP). It uses encryption for secure communication over a computer network, and is widely used on the Internet.[1][2] In HTTPS, the communication protocol is encrypted using Transport Layer Security (TLS) or, formerly, Secure Sockets Layer (SSL). The protocol is therefore also referred to as HTTP over TLS,[3] or HTTP over SSL.
(Wikipedia, October, 2023)

## EXCHANGE OF INFORMATION
When a secure connection is established, the web server(Software) on the the server(hardware) responds with the requested page. It is not a mere page though.

The page served is dynamically created by the application server behind the web server. The application server contains the code running the search engine.
An application server is a server that hosts applications or software that delivers a business application through a communication protocol.

An application server framework is a service layer model. It includes software components available to a software developer through an application programming interface. An application server may have features such as clustering, fail-over, and load-balancing. The goal is for developers to focus on the business logic.

(Wikipedia, October 2023)

Behind the application server, there is a database that contains information. But since you have not queried anything yet, the will be no much use of the application server hitting the database

###REFERENCES
Application server. (2022, December 31). In Wikipedia. https://en.wikipedia.org/wiki/Application_server
HTTPS. (2023, October 11). In Wikipedia. https://en.wikipedia.org/wiki/HTTPS
CloudFlare (n.d.). What is DNS? | How DNS works. Retrieved October 16, 2023, from https://www.cloudflare.com/learning/dns/what-is-dns/
CloudDNS (2023, March 15). What is a DNS query? Retrieved October 16, 2023, from https://www.cloudns.net/wiki/article/254/