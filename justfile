set shell := ["zsh", "-cu"]

install-pyproject:
    uv venv .venv --clear
    uv pip install -e /home/carol/titanic/Titanic_Prediction/

lint:
    ruff check .


transform_data data_type="training":
    cd Titanic_Prediction && uv run python -m src.tasks.transform --data-type "{{data_type}}"
