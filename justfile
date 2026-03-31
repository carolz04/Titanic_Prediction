set shell := ["zsh", "-cu"]

install-pyproject:
    uv venv .venv --clear
    uv pip install -e /home/carol/titanic/Titanic_Prediction/

lint:
    ruff check .


transform_data training:
    uv run python -m src.tasks.transform --data-type "training"