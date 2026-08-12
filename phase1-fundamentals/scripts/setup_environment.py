#!/usr/bin/env python3
"""
Setup Python environment for Quant VN Learn.
Thiết lập môi trường Python cho Quant VN Learn.

Usage / Cách sử dụng:
    python scripts/setup_environment.py
"""

from __future__ import annotations

import sys
from pathlib import Path


def check_python_version() -> bool:
    """Check if Python version is >= 3.13."""
    required = (3, 13)
    current = sys.version_info[:2]

    if current >= required:
        print(f"✅ Python {sys.version.split()[0]} - OK")
        return True
    else:
        print(f"❌ Python {sys.version.split()[0]} - Need Python 3.13+")
        return False


def check_package(package: str, import_name: str | None = None) -> bool:
    """Check if a package is installed."""
    import_name = import_name or package
    try:
        __import__(import_name)
        print(f"✅ {package} - OK")
        return True
    except ImportError:
        print(f"❌ {package} - Not installed")
        return False


def main() -> int:
    """Main setup check."""
    print("=" * 60)
    print("Quant VN Learn - Environment Check")
    print("=" * 60)
    print()

    # Check Python version
    print("📌 Python Version:")
    python_ok = check_python_version()
    print()

    if not python_ok:
        print("Please upgrade to Python 3.13+:")
        print("  brew install python@3.13  # macOS")
        print("  pyenv install 3.13.0     # or use pyenv")
        print()
        return 1

    # Core packages
    print("📌 Core Data Science Packages:")
    core_packages = [
        ("numpy", "numpy"),
        ("pandas", "pandas"),
        ("scipy", "scipy"),
        ("matplotlib", "matplotlib"),
        ("seaborn", "seaborn"),
        ("plotly", "plotly"),
    ]

    all_ok = all(check_package(p, i) for p, i in core_packages)
    print()

    # Jupyter
    print("📌 Jupyter:")
    jupyter_packages = [
        ("jupyter", "jupyter"),
        ("jupyterlab", "jupyterlab"),
    ]
    all_ok = all(check_package(p, i) for p, i in jupyter_packages) and all_ok
    print()

    # ML/Stats
    print("📌 ML & Statistics:")
    ml_packages = [
        ("scikit-learn", "sklearn"),
        ("statsmodels", "statsmodels"),
    ]
    all_ok = all(check_package(p, i) for p, i in ml_packages) and all_ok
    print()

    # Dev tools
    print("📌 Development Tools:")
    dev_packages = [
        ("pytest", "pytest"),
        ("black", "black"),
        ("ruff", "ruff"),
        ("mypy", "mypy"),
    ]
    all_ok = all(check_package(p, i) for p, i in dev_packages) and all_ok
    print()

    # Summary
    print("=" * 60)
    if all_ok:
        print("✅ All packages installed!")
        print()
        print("Next steps:")
        print("  1. jupyter lab  # Start JupyterLab")
        print("  2. Open notebooks/01-python-essentials.ipynb")
    else:
        print("⚠️  Some packages missing.")
        print()
        print("Install with:")
        print("  pip install -r requirements.txt")
    print("=" * 60)

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
