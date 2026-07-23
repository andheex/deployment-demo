"""Small starter application for Module 02."""

from __future__ import annotations

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


def main() -> None:
    """Print a small smoke-test message for the project environment."""
    print("Project deployment-demo siap dijalankan.")
    print(f"Root project: {PROJECT_ROOT}")
    print(f"Interpreter: {sys.executable}")


if __name__ == "__main__":
    main()
