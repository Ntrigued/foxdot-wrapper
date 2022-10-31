"""
    FoxDot __main__.py
    ------------------

    Use FoxDot's interface by running this as a Python script, e.g.
    python __main__.py or python -m FoxDot if you have FoxDot correctly
    installed and Python on your path.

"""


from __future__ import absolute_import, division, print_function

from FoxDot.lib import FoxDotCode
from .foxdot_constants import setup_consts

def start():
    fd_exec = lambda x: FoxDotCode()(x, verbose=True, verbose_error=True)
    setup_consts(fd_exec)
    return fd_exec
