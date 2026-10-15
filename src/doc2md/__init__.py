from doc2md.cli import app


def main() -> None:
    """命令行入口，对应 pyproject.toml 里的 [project.scripts]。"""
    app()


__all__ = ["main"]
