from rich.syntax import Syntax
from rich.console import Console
console = Console()
mycode = """
from rich.text import Text
from rich.console import Console
from rich.theme import Theme
import streamlit as st
console = Console()

# Emoji
console.print(
    ":thumbs_up: :stuck_out_tongue_winking_eye: File Downloaded Successfully")
"""

synt = Syntax(mycode, "python", theme="monokai", line_numbers=True)
console.print(synt)
