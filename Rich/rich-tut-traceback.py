from rich.traceback import install
from rich.console import Console
console = Console()
install()


def add(x, y):
    console.log("Adding two numbers", log_locals=True)
    return x+y


add(1, 2)
add(1, 3)
add(1, "Str")
