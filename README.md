# IP
A lightweight package for manipulating IP addresses, masking networks / subnet and checking features of an IP address.
Has support for both versions of IP addresses: IPv4 and IPv6.

## DESCRIPTION

###SUB PACKAGES

**`resolve`** The base package that resolve the features of a specific IP address or hostname

**`utils`** The sub package that exposes the Localhost Object and lets you interact with
and see the feature of your host machine.

**`tests`** The test suite. Contains Test Cases for the various classes available in the package.

###MODULES
**`main`** The main module runs the tests in the tests package.

**`setup`** As the name suggests, this module helps you setup the package on your system

**`ipAddress`** This is the main interface, which is what you would use most to mask network address, get all host
 or subnet within a network range among other's. see usage below


##FEATURES

###resolve

    from ip import Resolve

**`USAGE`** This package accepts the top-level hostname or the IP Address and resolves several features about the IP
address or the hostname. top-level hostname is the name of the host without the protocol. eg. google.com and not
www.google.com or 127.0.0.1 or facebook.com.

It raises an UnResolvedException error when the hostname passed is not known or the ip address is wrong. eg.
thesexypanda.com or 1222.802.1242.0.

Also, calling print on an instance of the Resolved class prints several features of the ip/hostname such as the version
Hostname, state(up or down). Below is a full list of the properties on the Resolved Object.

```python3
    from ip import Resolve

    res = Resolve("google.com") or Resolve("216.34.89.23")
    # initializes the object and returns an instance of the Resolve Object.
    # throws an error if name cannot be resolved or ip address is wrong.

    res.address # returns the current ip address.
    res.address = "facebook.com"
    # sets the current address or host name. Overrides the initial one. BEWARE!

    res.hostname
    # returns the current hostname of the ip address

    res.state
    # returns the state of the current ip addressed passed.

    res.app_ips
    # returns all other IP addresses that are associated with this IP addresses. Public IP address that
    # belong to the same network.

    res.version
    # return the version of the IP address.

    res.fqdn
    # returns the fully qualified domain name of the IP address or hostname.

    ### THERE ARE OTHER PROPERTIES THAT ARE AVAILABLE, PLEASE DO CHECK!!!

```







> Then you call the class just like you'd call any other normal function and then you pass the the name of the site or

> IP address of the site if you know it and then you get the IP instance where you operate on it using methods.

```python
 
 *this_ip(iface=None)*
 	
 	# this is just a function that returns the current ip address of the machine that you are currently using.
 	
 	# you can pass an iface which is just the ip address on that particular interface if it exists.
 	
 	# else it returns a dictionary containing all the interfaces and the corresponding IP addresses.

 *ip = IP("localhost")*
 
 **ip.address**
 # returns the ip address of the hostname 

 *ip.address = "remote_host"*
 
 # sets the name of the ip address to the remote host

 *ip.hostname
 
 # returns the hostname of the ip address or the same hostname passed 

 *ip.all_ips
 
 # this methods works just like the nslookup tool in case you have used that before. All this that is to return all the
 
 # list ip addresses registered to a particular name.

 *ip.fqdn
 
 # this method returns the fully qualified domain name of the ip or the host

 *ip.is_local
 
 # returns true if the ip is local ip

 *ip.is_private
 
 # returns true if the ip is private

 *ip.version
 
 # returns the version of the ip address v4 or v6

 *ip.is_reserved
 
 # returns true if the ip is reserved.

 *network = ip.mask(mask_no) eg: network = ip.mask(24)
 
 # In case you are familiar with subnet masking. Using numbers to mask/represent a whole network, you will find this
 
 # method really great to use. Pass a number that masks the subnet and then it returns an object. hence it returns the
 
 # whole network.

    *network.network_address*
    
    # returns the network address as in localhost/24 or 127.0.0.1./24

    *network.hostmask*
    
    # returns a mask of all the hosts in the network 0.0.0.255 

    *network.netstat*
    
    # returns the network mask of the network 255.255.255.0

    *network.number_of_hosts*
    
    # returns the number of hosts in the network

    *network.hosts*
    
    # returns a generator object of all the hosts in the network

    *network.subnets*
    
    # returns a list of all the subnets in the network which you can manipulate like a netowrk because it technically
    
    # is a network

    * network.check_up
    
    # returns a list of all the hosts that are up in the network. this might take a while depending on your internet connection

```

*this is just as simple as it is, actually very simple.*

**thank you**

:metal:

:+1: :sparkles:

DANNY MCWAVES
