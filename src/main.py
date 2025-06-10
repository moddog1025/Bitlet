import sys
import time
from threading import Thread

from bitlet_core.runner import start_hotkey_loop
from bitlet_core.config import setup_check
from bitlet_core.app_setup import setup_bitlet


def main():
    if setup_check():
        setup_bitlet()
    Thread(target=start_hotkey_loop, daemon=True).start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
