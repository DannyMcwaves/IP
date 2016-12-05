"""
this contains at least three base classes that are used to test for the
various classes available in this package.

TESTS should be provided for Resolve, IP, and Localhost
"""


from unittest import TestCase, TestSuite
from ip import Resolve
from ip import Localhost
from ip import IP


class ResolveTestCase(TestCase):
    """
    Test case for the Resolve package.
    """


class LocalhostTestCase(TestCase):
    """
    Test case for the Localhost package.
    """


class IPTestCase(TestCase):
    """
    Test case for the IP Package.
    """