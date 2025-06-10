import os
import mimetypes
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from shutil import move, copy2

from win32clipboard import (
    OpenClipboard,
    IsClipboardFormatAvailable,
    GetClipboardData,
    CloseClipboard,
    SetClipboardText,
    EmptyClipboard,
)
from win32con import CF_UNICODETEXT, CF_TEXT, CF_HDROP

from bitlet_core.config import get_paths, ICON_ICO_PATH


def bit_from_clipboard():
    OpenClipboard()
    try:
        if IsClipboardFormatAvailable(CF_UNICODETEXT):
            text = GetClipboardData(CF_UNICODETEXT)
            transfer_textbit(str(text))
            return
        if IsClipboardFormatAvailable(CF_TEXT):
            raw = GetClipboardData(CF_TEXT)
            text = raw.decode('mbcs', errors='replace')
            transfer_textbit(str(text))
            return
        if IsClipboardFormatAvailable(CF_HDROP):
            paths = GetClipboardData(CF_HDROP)
            for path in paths:
                mime_type, _ = mimetypes.guess_type(path)
                mime_type = mime_type or "unknown"
                transfer_filebit(str(path))
            return
    finally:
        CloseClipboard()


def empty_bitbox() -> None:
    paths = get_paths()
    bitbox_dir = paths.bitbox_dir
    bitarchive_dir = paths.bitarchive_dir
    bitarchive_dir.mkdir(parents=True, exist_ok=True)

    for file in bitbox_dir.iterdir():
        if file.is_file():
            move(str(file), str(bitarchive_dir / file.name))


def transfer_textbit(text: str) -> None:
    paths = get_paths()
    empty_bitbox()
    textbit_file = paths.bitbox_dir / "TextBit.txt"
    textbit_file.write_text(text, encoding="utf-8")


def transfer_filebit(file_path: str) -> None:
    empty_bitbox()
    paths = get_paths()
    source = Path(file_path)
    stem = source.stem
    ext = source.suffix
    new_name = f"FileBit_{stem}{ext}"
    destination = paths.bitbox_dir / new_name
    copy2(source, destination)


def fetch_latest_bits() -> None:
    paths = get_paths()
    bitbox_dir = paths.bitbox_dir
    for file in bitbox_dir.iterdir():
        if file.is_file():
            if "TextBit" in file.name:
                text = file.read_text(encoding="utf-8")
                OpenClipboard()
                EmptyClipboard()
                SetClipboardText(text)
                CloseClipboard()
            else:
                display_name = file.name
                if display_name.startswith("FileBit_"):
                    display_name = display_name.removeprefix("FileBit_")

                download_dir = Path.home() / "Downloads"
                if not download_dir.exists():
                    download_dir = os.getcwd()

                window = tk.Tk()
                window.iconbitmap(str(ICON_ICO_PATH))
                window.lift()
                window.attributes("-topmost", True)
                window.withdraw()
                
                dest_dir = filedialog.askdirectory(
                    parent=window,
                    initialdir=download_dir,
                    title="Select shared cloud folder..."
                )
                window.destroy()

                if dest_dir:
                    dest_path = Path(dest_dir) / display_name
                    copy2(file, dest_path)

    empty_bitbox()
