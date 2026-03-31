# 🚢 Titanic Survival Prediction

[![Kaggle](https://img.shields.io/badge/Kaggle-Getting%20Started-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/competitions/titanic)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is a solution for the **[Kaggle Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic)** getting started competition. The goal is to predict which passengers survived the Titanic shipwreck using passenger data such as age, gender, ticket class, and more.

## 📂 Project Structure

```
Titanic_Prediction/
├── data/                  # Raw and processed datasets
├── models/                # Saved trained models
├── notebooks/
│   └── titanic-survivor-prediction.ipynb   # Main analysis notebook
├── src/                   # Source code modules
│   ├── processing/        # Data processing utilities
│   ├── tasks/             # Task pipelines
│   └── utils/             # Helper utilities
├── tests/                 # Unit tests
├── mlruns/                # MLflow experiment tracking
├── pyproject.toml         # Project configuration & dependencies
└── README.md
```

## 📓 Notebook Overview

The main notebook (`notebooks/titanic-survivor-prediction.ipynb`) follows a structured ML workflow:

### 1. Exploratory Data Analysis (EDA)
- Analyzed distributions, missing values, and correlations across features
- Visualized survival rates by passenger class, sex, age, and embarkation port

### 2. Feature Engineering
- Handled missing values and outliers
- Created new features and transformed existing ones to improve model performance
- Encoded categorical variables for model compatibility

### 3. Model Training
Trained and compared **6 classification models**:

| # | Model | Description |
|---|-------|-------------|
| 1 | **Logistic Regression** | Linear baseline classifier |
| 2 | **Random Forest** | Ensemble of decision trees |
| 3 | **XGBoost** | Gradient boosting (XGBoost) |
| 4 | **Gradient Boosting (GBoost)** | Scikit-learn gradient boosting |
| 5 | **K-Nearest Neighbors (KNN)** | Distance-based classifier |
| 6 | **Neural Networks** | Multi-layer perceptron |

### 4. Model Evaluation
Evaluated all models using multiple metrics for robust model selection:
- **Confusion Matrix** — to assess true/false positives and negatives
- **AUC (Area Under the Curve)** — to measure overall discriminative ability
- **ROC Curve** — to visualize the trade-off between sensitivity and specificity

## 🛠️ Tech Stack

- **Python 3.11+**
- **pandas** — Data manipulation
- **scikit-learn** — ML models & evaluation
- **XGBoost** — Gradient boosting
- **MLflow** — Experiment tracking
- **Loguru** — Logging
- **Pydantic / Pandantic** — Data validation

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/Titanic_Prediction.git
cd Titanic_Prediction

# Install dependencies using uv
uv sync

# Or using pip
pip install -e .
```

### Running the Notebook

```bash
jupyter notebook notebooks/titanic-survivor-prediction.ipynb
```

## 📊 Results

Model performance was compared using AUC-ROC scores and confusion matrices to select the best-performing classifier. Refer to the notebook for detailed metrics and visualizations.

## 🗺️ Roadmap

This project is evolving into a **production-grade, end-to-end ML pipeline**. Upcoming changes include:

- [ ] **Pydantic Data Contracts** — Define strict schemas for raw input, processed features, and prediction outputs using Pydantic models to ensure data integrity at every stage
- [ ] **Validated Ingestion Pipeline** — Automate data loading with Pydantic validation so malformed or unexpected records are caught before they reach the model
- [ ] **Feature Engineering Pipeline** — Build modular, reproducible transformation steps with validated inputs and outputs
- [ ] **Training Pipeline** — Orchestrate model training with config-driven hyperparameters managed via Pydantic settings
- [ ] **Model Registry & Versioning** — Integrate with MLflow for experiment tracking, model versioning, and artifact management
- [ ] **Prediction Service** — Expose a prediction endpoint with Pydantic request/response models for type-safe inference
- [ ] **CI/CD & Testing** — Add automated tests for data validation, model performance regression, and pipeline integrity

