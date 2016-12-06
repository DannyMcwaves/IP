"""
this is the main module that provides most of the functionality I am trying to implement
in this package
"""

import ipaddress
from ip import Resolve, UnResolvedException
import sys

__all__ = ["IP"]


class IP:

    """
    the main purpose of the IP is for manipulating ip addresses, masking subnets, checking for the attributes
    on IPS. the subclasses they belong or the hostmask.
    """

    def __init__(self, address: str, mask: int=32):
        """
        :param address: The IP address
        :param mask: this is the mask it should take for the number of hosts that you are planning to access
                      the mask can be a valid host mask or a valid net_mask or a num_digit slash.
                      host mask starts with 0 and contain either 0's and 255's
                      net masks start with 255 and contain either 0's and 255's
        """
        try:
            self.ip_address = Resolve(address)
            self.__mask = mask
            addr = self.ip_address + str(mask)
            self.mask_addr = ipaddress.IPv4Network(addr, strict=False) if self.ip_address.version == "IPv4" else \
                ipaddress.IPv6Network(addr, strict=False)
        except UnResolvedException as unRes:
            print(unRes.args[1])
            sys.exit()

    def __call__(self, *args, **kwargs):
        """
        :param args: None.
        :param kwargs: None.
        :return: The raw IP address where you can get features of the IP address.
        """
        return self.ip_address

    @property
    def address(self):
        """
        :return: The current mask address of the network
        """
        return self.mask_addr

    @property
    def mask(self):
        """
        :return: The current mask of the network address.
        """
        return self.__mask

    @mask.setter
    def mask(self, value: int):
        """
        :param value: the value to mask the network
        :return: None. just masks the ip address to a network
        """
        self.__mask = value
        addr = self.ip_address + str(value)
        self.mask_addr = ipaddress.IPv4Network(addr, strict=False) if self.ip_address.version == "IPv4" else \
            ipaddress.IPv6Network(addr, strict=False)

    @property
    def hostmask(self):
        """
        :return: The hostmask address of this particular.
        """
        return self.mask_addr.hostmask

    @property
    def netmask(self):
        """
        :return: The netmask address of this particular network address.
        """
        return self.mask_addr.netmask

    @property
    def network_address(self):
        """
        :return: the network address of this particular network. All numbers before '/'
        """
        return self.mask_addr.network_address

    @property
    def number_of_hosts(self):
        """
        :return: The number of hosts within this network.
        """
        return self.mask_addr.num_addresses

    @property
    def hosts(self):
        """
        :return: A generator with all the hosts in this network.
        """
        return self.mask_addr.hosts()

    @property
    def subnets(self):
        """
        :return: A generator of the two subnets directly beneath this network
        """
        return self.mask_addr.subnets()

    @property
    def supernet(self):
        """
        :return: the direct immediate supernet of this network address.
        """
        return self.mask_addr.supernet()


if __name__ == '__main__':
    ip = IP("facebook.com")
    ipaddr = ip()
    ip.mask = 24
    print(ipaddr)
    print(ip.address)
    print(ip.supernet)
    print(ip.subnets)
    print(ip.network_address)

