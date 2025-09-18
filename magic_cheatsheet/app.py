from .manage_config import get_config
import platform
from termcolor import colored

from mistralai import Mistral
from ollama import chat
from ollama import ChatResponse

def get_prompt(command: str, detailed: bool):
    os_name = platform.system()
    if detailed:
        details = "- how to uninstall the tool \n Detail un a functionnal way"
    else:
        details = "Keep it simple, concise and functionnal, under 20 lines"
    prompt = f"""# Role
You are an AI agent that generates cheatsheets for cli commands. 

# Mission
Based on this user command : {command} 
generate a cheatsheet of this CLI command. 
The cheatsheet should include : 
- how to install the tool if it is not generally already installed by default
- The usage pattern of the tool, followed by specific examples
{details}

# Format
The cheatsheet will be printed directly in the terminal; format response accordingly to avoid clutter. Simple formatting.

# Data
User's OS : {os_name}"""
    return prompt



def app(command: str, detailed: bool = False):
    config = get_config()
    provider = config["provider"]    
    prompt = get_prompt(command, detailed)

    if provider == "mistral":
        print("Asking MistralAI...")
        client = Mistral(api_key=config[provider]["api_key"])
        chat_response = client.chat.complete(
           model = config[provider]["model"],
            messages = [
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )

        answer = chat_response.choices[0].message.content
        print(colored(answer, "dark_grey"))

    if provider == "ollama":
        model = config[provider]["model"]

        response: ChatResponse = chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
        ])

        answer = response.message.content
        print(colored(answer, "dark_grey"))


