import typer
from .commands import hello

# Create an app instance
app = typer.Typer()

# Register commands
app.command()(hello)
