from rich.console import Console
console = Console()
console.print("This is some text")
console.print("This is some text", style="bold underline")
console.print("This is some text", style="bold underline red")
console.print("This is some text", style="underline red on white")
console.print("[bold]This [cyan]is[/] some text.[/]")
