from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_dashboard(assets=None):

    console.print(
        Panel.fit(
            "[bold green]GemAI Trader v0.2[/bold green]\n"
            "[cyan]READ ONLY MODE[/cyan]",
            title="Dashboard",
        )
    )

    table = Table(title="Portfolio")

    table.add_column("Coin")
    table.add_column("Balance", justify="right")
    table.add_column("AUD Value", justify="right")
    if not assets:
            table.add_row("-", "-", "-")
    else:
          for asset in assets:
                table.add_row(
                    asset["coin"],
                    str(asset["balance"]),
                    f"${asset['value']:.2f}",
            )

    console.print(table)