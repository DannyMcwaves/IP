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


##MAIN API's

###Resolve

    from ip import Resolve

**`USAGE`** This package accepts the top-level hostname or the IP Address and resolves several features about the IP
address or the hostname. top-level hostname is the name of the host without the protocol. eg. google.com and not
www.google.com or 127.0.0.1 or facebook.com.

It raises an UnResolvedException error when the hostname passed is not known or the ip address is wrong. eg.
thesexypanda.com or 1222.802.1242.0.

Also, calling print on an instance of the Resolved class prints several features of the ip/hostname such as the version
Hostname, state(up or down). Below is a full list of the properties on the Resolved Object.

```python
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
    # returns all other IP addresses that are associated with this IP addresses:
    # Public IP address that belong to the same network.

    res.version
    # return the version of the IP address.

    res.fqdn
    # returns the fully qualified domain name of the IP address or hostname.

    ### THERE ARE OTHER PROPERTIES THAT ARE AVAILABLE, PLEASE DO CHECK!!!
```

###IP

    from ip import IP

**`USAGE`** The IP object is the main interface to the ip package. Like the Resolve Object, it takes an IP address or
a hostname argument, and it also takes a second argument called 'mask' which is optional. the mask is the network mask
of the ip address, the default mask is 32, so your full IP network address is "127.0.0.1/32". You can define it later
with the mask property. The mask suggests the range of the network. the value is between 0-32. 32 refers to a particular
computer and 0 refers to the whole internet -- I KNOW !!.

When you call an instance of the IP Object it returns a resolved object.
    _ip = IP("facebook.com")
    res = _ip()
    # the res variable is an instance of the Resolve Object defined above. It has all the properties defined above.

The IP Object has a Duck Type dependency on the Resolve method and as such all that is said for the Resolved Object
applies to the IP object, like passing a wrong IP address or hostname.

Here is a difference to take away, the IP Object works with networks and the Resolve Object works with single IP address

Below is full list of the properties on the IP Object

```python
    from ip import IP
    _ip = IP("facebook.com")

    res = _ip()
    # calling an instance of the IP object returns a Resolve Object.

    _ip.address
    # returns the full masked address of the network. eg 123.456.789.001/32

    _ip.mask
    # returns the current network mask. eg. 32.
    _ip.mask = 24
    # sets a new network mask. so the new address will be 123.456.789.0/24

    _ip.hostmask
    # returns the number of hosts masked in the network address in the form 0.0.0.225

    _ip.netmask
    # the opposite of the hostmask is the netmask. returns the subnet mask in the form 255.255.255.0

    _ip.network_address
    # after setting a mask lower that 32 the IP address changes to a network address.
    # when you call this property, it return that address.

    _ip.number_of_hosts
    # this returns the entire number of hosts in the network.

    _ip.hosts
    # returns a list of all the IP addresses of the hosts in the network. Yes all of them.
    # this is not advisable for large network ranges. Instead use subnet to divide the large network
    # and get the hosts property on it.

    _ip.subnets
    # returns the subnets under this network.
```

###Localhost

    from ip import Localhost

**`USAGE`** As stated earlier, this lets you interact with your system and see several features of your computer. For
example, hostname, ip addresses of the host, ip addresses on the various network interfaces, the os_release,
the os_version among others.

Below is a list of properties available.

```python
    from ip import Localhost
    localhost = Localhost()
    # you dont need to pass anything to it.

    localhost.hostname
    # will almost always return 'localhost'

    localhost.ip
    # returns the standard ip address of localhost.

    localhost.platform
    # returns the name of the platform of the local machine. Usually Linux, Unix or Window

    localhost.node
    # returns an alternative name set for this computer.
    # For instance I call my computer mcbook even though it is not a mcbook.

    localhost.processor
    # the current processor on this machine

    localhost.os_version
    # returns the version of the OS this machine running on.

    localhost.os_release
    # the current os release of this machine.

    localhost.ipaddress(iface=None)
    # if the iface option is none, it returns a dictionary of all the ip address on their corrresponding
    # network interfaces. If you specify the iface and it has internet connection it returns the IP address on that
    particular interface. the interface option include "wlan0, eth0, eth2, l0, virbr0"
```


## Need help?
Feel free to [create an issue](http://github.com/DannyMcwaves/IP/issues),
[tweet me](http://twitter.com/DannyMcwaves), or [send me an email](mailto:dannymcwaves96@gmail.com).
I'd be glad to help where I can!

:smile::smile::smile::smiley::+1::+1::+1::ok_hand::metal::hand::raised_hands::muscle::clap::wave:

