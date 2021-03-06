"""
the main entry point of the ip package is the __init__ file.
------------------------------------------------------------
specifies a few dependencies for the app and coagulates all the
several pieces into one for easy imports.
"""

from ip.resolve import Resolve, UnResolvedException
from ip.utils import Localhost
from ip._ip import IP
__all__ = ["IP", "Localhost", "Resolve", "UnResolvedException"]
