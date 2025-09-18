def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: magic-cheatsheet <commande>")
        sys.exit(1)
    command = sys.argv[1]
    print(f"Generating cheatsheet for : {command}")
