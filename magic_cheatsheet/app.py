from .manage_config import get_config
from .prompt import get_prompt
from termcolor import colored
from mistralai import Mistral
from ollama import chat
from ollama import ChatResponse



def app(command: str, detailed: bool = False):
    config = get_config()
    provider = config["provider"]    
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
        print(colored(answer, "white", attrs=["dark"]))

    if provider == "ollama":
        print(colored("Asking Ollama...", "light_grey"))

        model = config[provider]["model"]

        response: ChatResponse = chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
        ])

        answer = response.message.content
        print(colored(answer, "white", attrs=["bold"]))


