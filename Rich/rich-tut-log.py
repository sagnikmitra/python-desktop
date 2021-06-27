from rich.console import Console
import time
console = Console()
for i in range(10):
    console.log(f"Doing some important stuf ... {i}")
    time.sleep(0.2)
