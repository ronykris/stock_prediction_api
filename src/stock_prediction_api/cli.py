"""Console script for stock_prediction_api."""
import stock_prediction_api

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for stock_prediction_api."""
    console.print("Replace this message by putting your code into "
               "stock_prediction_api.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
