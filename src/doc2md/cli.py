import typer

app = typer.Typer(help="doc2md — 把文档批量转换成 Markdown")


@app.callback()
def main() -> None:
    """doc2md — 把文档批量转换成 Markdown"""


@app.command()
def hello(name: str = "world") -> None:
    """打印一句问候，用来验证 CLI 骨架是否正常工作。"""
    typer.echo(f"hello {name}")


if __name__ == "__main__":
    app()