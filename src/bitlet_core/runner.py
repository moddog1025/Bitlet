import os
import time
import ctypes

import keyboard

from bitlet_core.bit_handler import fetch_latest_bits, bit_from_clipboard
from bitlet_core.config import get_paths


if os.name == 'nt':
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


def on_hotkey_transfer():
    bit_from_clipboard()


def on_hotkey_fetch():
    fetch_latest_bits()


def start_hotkey_loop():
    keyboard.add_hotkey("ctrl+alt+z", on_hotkey_transfer)
    keyboard.add_hotkey("ctrl+shift+z", on_hotkey_fetch)
    while True:
        time.sleep(1)
