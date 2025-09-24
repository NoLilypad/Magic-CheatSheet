*Actual useful AI...*

# Magic-CheatSheet
A fast and easy to use in-terminal cheatsheet generator


## Installation

You can install Magic-CheatSheet using pipx:

```bash
pipx install git+https://github.com/NoLilypad/Magic-CheatSheet
```

Or, if you want to install from source:

```bash
git clone https://github.com/NoLilypad/Magic-CheatSheet.git
cd Magic-CheatSheet
pipx install .
```

Additionally, add an alias : 
```bash
echo "alias mg='magic_cheatsheet'" >> ~/.bashrc && source ~/.bashrc
``` 

## Usage Example

To generate a cheatsheet for a command using the CLI:

```bash
magic_cheatsheet "git rebase"
```

Use the `--detailed` flag to get more in depth cheat sheets : 

```bash
magic_cheatsheet "pipx" --detailed
```

## Configuration

To configure your LLM provider : 

```bash
magic_cheatsheet --config
```

You can also specify options (see `--help` for all options):

```bash
magic_cheatsheet --help
```
