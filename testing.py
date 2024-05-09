from pathlib import Path

new_path = Path("commands.txt")
command = new_path.read_text(encoding='utf-8')
print(command)
commands_path = Path("log.txt")
commands_path.write_text('utf-8')