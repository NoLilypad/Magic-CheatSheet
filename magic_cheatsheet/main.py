
import argparse
import sys
from .app import app
from .manage_config import edit_config, create_config
import os
import subprocess

def main():
    create_config()

    parser = argparse.ArgumentParser(description="Generate a cheatsheet for a given command.")
    parser.add_argument("command", nargs="?", help="The command to generate a cheatsheet for")
    parser.add_argument("--detailed", action="store_true", help="Show a detailed cheatsheet")
    parser.add_argument("--version", action="store_true", help="Show the version of Magic-CheatSheet")
    parser.add_argument("--config", action="store_true", help="Configuration of the tool")

    args = parser.parse_args()

    if args.version:
        print("Magic-CheatSheet version 1.0.0")
        sys.exit(0)

    if args.config:
        edit_config()
        sys.exit(0)

    if not args.command:
        print("Usage: magic-cheatsheet <command> [--detailed] [--version]")
        sys.exit(1)

    app(args.command, args.detailed)
