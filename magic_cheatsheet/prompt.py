
import platform

default_prompt = """\n
# Role
You are an AI agent that generates cheatsheets for cli commands.

# Mission
Based on this user command: {command}, generate a cheatsheet of this CLI command. 
The cheatsheet should include: 
- a VERY short description of the tool or command (one line)
- how to install the tool if it is not generally already installed by default
- basic examples

{details}

# Format
Every command examples should follow this pattern : 

    [command]         #quick explanation

    [another command] #another explanation

    [third command]   #third explanation

Make sure to align the #explanations
Use # for titles, ## for second titles. 
DO NOT USE `` and ```bash``` formats.
DO NOT USE markdown formatting.
    
# Data
User's OS : {os_name}"""


def get_prompt(command: str, detailed: bool):
    os_name = platform.system()
    if detailed:
        details = "The cheatsheet should be detailed, max 40 lines. Include also how to uninstall the tool"
    else:
        details = "The cheatsheet should be short, max 20 lines."
    prompt = default_prompt.format(command=command, details=details, os_name=os_name)
    return prompt
