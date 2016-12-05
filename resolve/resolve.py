
"""
this sub package is actually a dependency required by the main
module directly in the IP package.

it resolves the names of IP addresses. Checks the state or return the IP
address of a particular hostname and vice versa.
Among other function I will define later.

------------------------------------------------------------------------------------------------------------------------
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

__all__ = ["Resolve"]


class Resolve:

    """
    I am going to use socket to get all the IP addresses
    that are specific and pertain to a particular hostname.
    And basically to perform net-mask and all that.
    """

    def __init__(self, addr: str):
        try:
            self.__host = addr if addr.isalpha() else socket.gethostbyaddr(addr)[0]
            self.__ip = socket.gethostbyname(addr) if not addr.isdigit() else addr
            self.__IP = ipaddress.ip_address(self.__ip)
        except socket.herror as he:
            print(he.args[1])
            print("[-] PLEASE PROVIDE A VALID ADDRESS")
            sys.exit()
        except socket.gaierror as ga:
            print(ga.args[1])
            print("[-] PLEASE PROVIDE A VALID ADDRESS")
            sys.exit()
        except socket.error as err:
            print(err.args[1])
            print("[-] SOMETHING SEEMS TO BE WRONG WITH YOUR IP ADDRESS. PLEASE PROVIDE A VALID ADDRESS")
            sys.exit()

    def __call__(self, *args, **kwargs):
        """
        :return: the class instance of the ipaddress.ip_address.
        """
        return self.__IP

    def __add__(self, other):
        return self.address + "/" + other

    @property
    def address(self):
        """
        :return: returns the raw IP address.
        """
        return self.__IP.exploded

    @address.setter
    def address(self, address):
        """
        :param address: sets the raw IP address by hostname or an address.
        :return:
        """
        self.__host, self.__ip = address if address.isalpha() else socket.gethostbyaddr(address), \
            socket.gethostbyname(address) if self.address.isalpha() else address

        self.__IP = ipaddress.ip_address(self.__ip)

    @property
    def hostname(self):
        """
        :return: the hostname of the ip address
        """
        return self.__host

    @property
    def all_ips(self):
        """
        :return: all the registered IP addresses signed
        """
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
        return "IPv" + str(self.__IP.version)

    @property
    def is_reversed(self):
        return self.__IP.is_reserved


if __name__ == '__main__':
    ad = "google.com"
    re = Resolve(ad)
    print(re.hostname)
    print(re.address)
    print(re.fqdn)
    print(re.all_ips)
    print(re.version)
