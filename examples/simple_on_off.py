import time
from framework.startup import start
from framework.keyboard_handler import KeyboardHandler

fd_exec = start()
kh = KeyboardHandler(fd_exec=fd_exec)
editing = False


kh.set('a', 'p1', 'pluck(pC)')
kh.set('a', 'p1', 'bass([C, C, G, G, G+s, G+s, F+s, F+s], dur=2)')
while True:
    time.sleep(100)
