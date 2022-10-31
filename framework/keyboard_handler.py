from typing import Any, Dict, List, Optional, Union

from pynput import keyboard


class KeyboardHandler:
    def __init__(self, fd_exec):
        self.keys: Dict[Any, keyboard.Listener] = {}
        self.fd_exec = fd_exec

    def get(self, key: Any) -> Optional[keyboard.Listener]:
        if key in self.keys:
            return self.keys[key]
        return None

    def check_and_set(self, key: Any, player: str, assignment: str, warn=False) -> Union[bool, keyboard.Listener]:
        if self.get(key):
            if warn:
                print(f'{key} already has a listener')
            return False
        return self.set(key, player, assignment)

    def set(self, key: Any, player: str, assignment: str) -> keyboard.Listener:
        def on_press(keypress):
            k = None
            try:
                k = keypress.char  # single-char keys
            except:
                k = keypress.name  # other keys
            if k == key:
                self.fd_exec(f'{player}.stop() if {player}.isplaying else {player} >> {assignment} ')
        self.unset(key)
        self.keys[key] = keyboard.Listener(on_press=on_press)
        self.keys[key].start()
        return self.keys[key]

    def unset(self, key: Any) -> bool:
        if key in self.keys:
            self.keys[key].stop()
            del self.keys[key]
            return True
        return False
