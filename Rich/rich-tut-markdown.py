from rich.console import Console
from rich.markdown import Markdown

console = Console()

MARKDOWN = """
# This is an Header1
#### This is an Header4
"""

md = Markdown(MARKDOWN)
console.print(md)

"""
To run anykind of Markdown File through Python
just write
python -m rich.markdown README.md
"""
with open("README.md") as md:
    markdown = Markdown(md.read())
    console.print(markdown)
