from rich.theme import Theme
from rich.console import Console

custom_theme = Theme({"success": "green", "error": "bold red"})
console = Console(theme=custom_theme)

console.print("Operation Successful", style="success")
console.print("Operation Failed", style="error")
