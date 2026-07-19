from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_dashboard():


    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table

    console = Console()

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

    table.add_row("-", "-", "-")

    console.print(table)