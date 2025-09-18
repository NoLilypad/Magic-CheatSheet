from .manage_config import get_config

def app(command: str, detailed: bool = False):
    config = get_config()
    print(f"Loaded config: {config}")
    print(f"Generating cheatsheet for: {command}")
    
    if detailed:
        print("(Detailed mode enabled)")
    # Here will be the core logic for generating the cheatsheet


