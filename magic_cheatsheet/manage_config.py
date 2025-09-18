import os
import sys
import subprocess
from platformdirs import user_config_dir
import yaml

def get_config_path():
    config_dir = user_config_dir("Magic-CheatSheet")
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, "config.yaml")

def create_config():
    config_path = get_config_path()
    if not os.path.exists(config_path):
        default_config = {"example_key": "example_value"}
        with open(config_path, "w") as f:
            yaml.dump(default_config, f)
    return config_path

def edit_config():
    config_path = create_config()
    editor = os.environ.get("EDITOR", "nano")
    if config_path:
        try:
            subprocess.run([editor, config_path])
        except Exception as e:
            print(f" Error opening config: {e}")
            sys.exit(1)
    else:
        print("Config file path not found.")
    sys.exit(0)
