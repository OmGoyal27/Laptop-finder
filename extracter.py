from pathlib import Path
commands_path = Path("commands.txt")
commands = commands_path.read_text(encoding='utf-8')