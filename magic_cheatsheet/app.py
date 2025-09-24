from .manage_config import get_config
from .prompt import get_prompt
from termcolor import colored
from mistralai import Mistral
from ollama import chat
from ollama import ChatResponse
import sys

def printer(message : str):
        print(' ')
        print(colored(message, "white", attrs=["dark"]))


def app(command: str, detailed: bool = False):
    config = get_config()
    
    # Validate config has required keys
    if not config:
        print("Error: Configuration not found. Please run 'magic-cheatsheet --config' to set up.")
        sys.exit(1)
    
    if "provider" not in config:
        print("Error: No provider specified in config. Please run 'magic-cheatsheet --config' to set up.")
        sys.exit(1)
    
    provider = config["provider"]
    
    # Validate provider-specific config
    if provider not in config:
        print(f"Error: Configuration for provider '{provider}' not found.")
        sys.exit(1)
    
    prompt = get_prompt(command, detailed)

    if provider == "mistral":
        print(colored("Asking to MistralAI...", "dark_grey"))
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
        printer(answer)

    elif provider == "ollama":
        print(colored("Asking Ollama...", "dark_grey"))

        model = config[provider]["model"]

        response: ChatResponse = chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
        ])

        answer = response.message.content
        printer(answer)
    
    else:
        print(f"Error: Unsupported provider '{provider}'. Please use 'mistral' or 'ollama'.")
        sys.exit(1)

