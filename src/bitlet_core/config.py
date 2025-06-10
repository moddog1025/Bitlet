import os
import json
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from dataclasses import dataclass


@dataclass
class FilePaths:
    local_data_dir: Path
    config_file: Path
    settings_file: Path
    shared_cloud_dir: Path
    bitlet_cloud_dir: Path
    bitbox_dir: Path
    bitarchive_dir: Path

CONFIG_PATH = Path(os.getenv("LOCALAPPDATA")) / "BitletApp" / "config.json"
_cached_paths = None

ICON_ICO_PATH = Path(__file__).parents[2] / "assets" / "bitlet_icon.ico"
ICON_PNG_PATH = Path(__file__).parents[2] / "assets" / "bitlet_icon.png"

DEF_CLOUD_DIRS = ["iCloud Drive", "iCloudDrive", "Dropbox", "OneDrive"]

def setup_check() -> bool:
    if CONFIG_PATH.exists():
        return False
    else:
        return True


def get_paths():
    global _cached_paths
    if _cached_paths is None:
        if not CONFIG_PATH.exists():
            raise RuntimeError("Bitlet is not set up yet.")
        _cached_paths = load_paths()
    return _cached_paths


def load_paths() -> FilePaths:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        raw = json.load(file)
    local_data = raw["paths"]["local"]
    shared_cloud = raw["paths"]["cloud"]
    return FilePaths(
        local_data_dir=Path(local_data["local_data_dir"]),
        config_file=Path(local_data["config_file"]),
        settings_file=Path(local_data["settings_file"]),
        shared_cloud_dir=Path(shared_cloud["shared_cloud_dir"]),
        bitlet_cloud_dir=Path(shared_cloud["bitlet_cloud_dir"]),
        bitbox_dir=Path(shared_cloud["bitbox_dir"]),
        bitarchive_dir=Path(shared_cloud["bitarchive_dir"]),
    )

def get_def_cloud_dir() -> str:
    for dir in DEF_CLOUD_DIRS:
        def_dir = Path.home() / dir
        if def_dir.exists():
            return str(def_dir)
    return str(Path.home() / "Documents")

def prompt_set_cloud_dir() -> str:
    window = tk.Tk()
    window.iconbitmap(str(ICON_ICO_PATH))
    window.withdraw()
    path = filedialog.askdirectory(
        parent=window,
        initialdir=get_def_cloud_dir(),
        title="Select shared cloud folder..."
    )
    window.destroy()
    return path


def change_setting(settings_path: Path, setting: str, new_value) -> None:
    with settings_path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    data["settings"][setting] = new_value
    with settings_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
