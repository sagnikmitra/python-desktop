from rich.text import Text
from rich.console import Console
console = Console()

console.print("[bold] This is[/][magenta]Hello Bro[/]Hi thre.")
text = Text("Hello World!")
text.stylize("bold magenta", 0, 6)
console.print(text)
