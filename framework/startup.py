from __future__ import absolute_import, division, print_function

from FoxDot.lib import FoxDotCode
from FoxDot.lib.Code import execute
# from framework.foxdot_constants import setup_consts
from keyboard_handler import KeyboardHandler

def start():

    from FoxDot.lib.Workspace.Editor import workspace

    fd_workspace = workspace(FoxDotCode)
    execute('from framework.foxdot_constants import *')
    fd_workspace.run()
#    fd_exec = lambda x: FoxDotCode()(x, verbose=True, verbose_error=True)
#    setup_consts(fd_exec)
#    return fd_exec

start()