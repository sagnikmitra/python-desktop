from rich.console import Console
from rich.table import Table

table = Table(title="Avengers Assemble")

table.add_column("Released", style="cyan", width=15)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 221", "Star Wars", "$16,346")
table.add_row("Dec 20, 221", "Star Wars", "$16,346")
table.add_row("Dec 20, 221", "Star Wars", "$16,346")

console = Console()
console.print(table)
