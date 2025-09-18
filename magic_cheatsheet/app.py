from .manage_config import get_config
import platform

def get_prompt(command: str, detailed: bool):
    os_name = platform.system()
    if detailed:
        details = "Detail a lot"
    else:
        details = ""
    prompt = f"""# Role
You are an AI agent that generates cheatsheets for cli commands. 

# Mission
Based on this user command : {command} 
generate a cheatsheet of this CLI command. 

# Response format
{details}

# Data
User's OS : {os_name}"""
    return prompt



def app(command: str, detailed: bool = False):
    config = get_config()
    print(f"Loaded config: {config}")
    print(f"Generating cheatsheet for: {command}")
    
    prompt = get_prompt(command, detailed)

    if config.provider == "mistral":
        pass

    if config.provider == "ollama":
        pass




