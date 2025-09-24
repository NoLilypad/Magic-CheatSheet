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
        default_config = {
            "mistral": {
                "api_key": "MISTRAL_API_KEY",
                "model": "codestral-latest"
            },
            "ollama": {
                "model": "llama3.2:3b",
                "url": "http://localhost:11434/api/chat"
            },
            "provider": "mistral"
        }
        with open(config_path, "w") as f:
            yaml.dump(default_config, f, default_flow_style=False, allow_unicode=True)
    return config_path

def edit_config():
    config_path = create_config()
    editor = os.environ.get("EDITOR", "nano")
    if config_path:
        try:
            subprocess.run([editor, config_path])
        except Exception as e:
            print(f"Error opening config: {e}")
            sys.exit(1)
    else:
        print("Config file path not found.")
    sys.exit(0)

# Read and return the configuration as a dictionary
def get_config():
    config_path = get_config_path()
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            try:
                return yaml.safe_load(f) or {}
            except yaml.YAMLError as e:
                print(f"Error reading config: {e}")
                return {}
    return {}
