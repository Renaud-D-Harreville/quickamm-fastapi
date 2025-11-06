rm -rf .venv
python3.14 -m venv .venv --prompt quickamm-fastapi
source .venv/bin/activate
pip install -U pip setuptools
pip install -e .[dev]
