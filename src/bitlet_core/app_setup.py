import json
import os
from pathlib import Path

from bitlet_core.defaults import CONFIG_SCHEMA, SETTINGS_SCHEMA
from bitlet_core.config import prompt_set_cloud_dir


def setup_bitlet():
    local_appdata = Path(os.getenv("LOCALAPPDATA"))
    local_data_dir = local_appdata / "BitletApp"
    local_data_dir.mkdir(parents=True, exist_ok=True)

    config_file = local_data_dir / "config.json"
    config_file.write_text(json.dumps(CONFIG_SCHEMA, indent=4), encoding="utf-8")

    settings_file = local_data_dir / "settings.json"
    settings_file.write_text(json.dumps(SETTINGS_SCHEMA, indent=4), encoding="utf-8")

    shared_cloud_dir = Path(prompt_set_cloud_dir())

    bitlet_cloud_dir = shared_cloud_dir / "Bitlet"
    bitlet_cloud_dir.mkdir(parents=True, exist_ok=True)
    bitbox_dir = bitlet_cloud_dir / "BitBox"
    bitbox_dir.mkdir(parents=True, exist_ok=True)
    bitarchive_dir = bitlet_cloud_dir / "BitArchive"
    bitarchive_dir.mkdir(parents=True, exist_ok=True)

    with config_file.open("r", encoding="utf-8") as file:
        data = json.load(file)
        data["paths"]["local"]["local_data_dir"] = str(local_data_dir)
        data["paths"]["local"]["config_file"] = str(config_file)
        data["paths"]["local"]["settings_file"] = str(settings_file)
        data["paths"]["cloud"]["shared_cloud_dir"] = str(shared_cloud_dir)
        data["paths"]["cloud"]["bitlet_cloud_dir"] = str(bitlet_cloud_dir)
        data["paths"]["cloud"]["bitbox_dir"] = str(bitbox_dir)
        data["paths"]["cloud"]["bitarchive_dir"] = str(bitarchive_dir)

    with config_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return
