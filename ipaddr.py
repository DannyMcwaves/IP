"""
This is just some simple stuff that i want to call connect for connecting to external
servers.

useful methods of the socket will include:
    1. gethostname -- returns the name of this host.
    2. gethostbyname -- returns the ip address of the host
    3. gethostbyname_ex -- returns the hostname, canonical name, and a list of other IP addresses like nslookup.
    4. gethostbyaddr -- works just like the gethostbyname_ex method, except this time the parameter is an IP address
    5. getfqdn -- returns the fully qualified domain name for the server.
    6. getservebyname -- returns the port of server by name. eg http is 80
    7. getservebyport -- returns the type of the server by the name. eg 22 is ssh
    8. getaddrinfo -- returns the a list of 5-tuple addresses of the hostname and port
                    In the tuple;
                        0. usually a number that reps the family name. eg AF_INET, AF_PACKET.
                        1. this is also a number but is the socket type. eg SOCK_D_GRAM, SOCK_STREAM.
                        2. represents the canonical name.
                        3. a tuple of the IP address and the port number.
    9.socket();
        a. connect -- connects and then raises an error if connection fails
        b. connect_ex -- connects and then returns a connection result. 0 means successful.

    10. os.popen to run a command and the return a file-like object, to work with. ping -c for linux and ping -n for win
    11. In case of any ICMP request block or filter, use the three way handshake by using the connect function available
        in the socket module.
    12. get the current ip address of this machine.

"""
import socket
import sys
import os
import ipaddress
import re
from netmap import scanner


class IP:

    """
    I am going to use socket to get all the IP addresses
    that are specific and pertain to a particular hostname.
    And basically to perform net-mask and all that.
    """

    def __init__(self, address):
        if not address.isdigit():
            self.__host = address
            self.__ip = socket.gethostbyname(address)
        else:
            self.__host = None
            self.__ip = address

        self.__IP = ipaddress.ip_address(self.address)

    @property
    def address(self):
        return self.__ip

    @address.setter
    def address(self, value):
        if value.isalpha():
            self.__ip = socket.gethostbyname(value)
        else:
            self.__ip = value
        pass

    @property
    def hostname(self):
        return self.__host if self.__host is not None else socket.gethostbyaddr(self.address)[0]

    @property
    def all_ips(self):
        return socket.gethostbyname_ex(self.hostname)[-1]

    @property
    def fqdn(self):
        return socket.getfqdn(self.hostname)

    @property
    def is_local(self):
        return self.__IP.is_loopback
    
    @property
    def is_private(self):
        return self.__IP.is_private
    
    @property
    def version(self):
        return self.__IP.version

    @property
    def is_reversed(self):
        return self.__IP.is_reserved

    def mask(self, prefix):
        return Mask(self.address, prefix)


def this_ip(iface=None):
        if iface is None:
            command = "ipconfig" if sys.platform.lower() == "windows" else "ifconfig"
        else:
            command = "ipconfig " + iface if sys.platform.lower() == "windows" else "ifconfig " + iface
        addrs = re.findall(r"addr:\d+\.\d+\.\d+\.\d+", os.popen(command).read(-1))

        if len(addrs) == 3:
            return {
                "local": addrs[0][5:],
                "wifi": addrs[2][5:],
                "other": addrs[1][5:]
            }
        elif len(addrs) == 4:
            return {
                "modem/wired": addrs[0][5:],
                "local": addrs[1][5:],
                "wifi": addrs[3][5:],
                "other": addrs[2][5:]
            }
        try:
            return addrs[0][5:]
        except IndexError:
            return NotImplemented


class Mask:
    """
    this is just a class under the IP class that is used to mask this IP address and then return network types and
    subnets for this IP network.
    """

    UP = []

    def __init__(self, address, mask):
        """
        :param address: The IP address
        :param mask: this is the mask it should take for the number of hosts that you are planning to access
                      the mask can be a valid host mask or a valid net_mask or a num_digit slash.
                      host mask starts with 0 and contain either 0's and 255's
                      net masks start with 255 and contain either 0's and 255's
        """
        self.address = address + "/" + str(mask)
        self.mask_addr = ipaddress.IPv4Network(self.address, strict=False)

    @property
    def hostmask(self):
        return self.mask_addr.hostmask

    @property
    def netmask(self):
        return self.mask_addr.netmask

    @property
    def network_address(self):
        return self.mask_addr.network_address

    @property
    def check_up(self):
        self.UP = scanner(self.address).ping()
        return self.UP

    @property
    def number_of_hosts(self):
        return self.mask_addr.num_addresses

    @property
    def hosts(self):
        return self.mask_addr.hosts()

    @property
    def subnets(self):
        return self.mask_addr.subnets()


if __name__ == '__main__':
    # from pprint import pprint
    ip = IP("gstatic.com")
    print(ip.address)
    print(ip.hostname)
    m = ip.mask(24)
    print(m.address)
    print(m.number_of_hosts)
    print([x for x in m.subnets])
    for i in m.hosts:
        print(i)
