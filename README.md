# Antenna Fault Detection

Machine-learning analysis for classifying antenna fault types from RF measurements.

## Repository layout

- `notebooks/` contains the exploratory analysis and model comparison notebook.
- `src/antenna_fault_detection/` contains reusable data preparation and feature engineering code.
- `data/` is reserved for the local dataset and documents the expected input schema.

## Setup

Create and activate a virtual environment, then install the pinned project dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Place the source data at `data/antenna_dataset.csv`. The dataset is intentionally not committed because it was not included with the notebook and may contain project-specific data.

Launch the analysis with:

```powershell
jupyter lab notebooks/antenna_fault_detection.ipynb
```

The notebook expects the working directory to be the repository root. If it is opened elsewhere, set `URL_DATA` to the absolute path of the CSV.

## Reproducibility

- The notebook uses random seed `42` for splits, cross-validation, and model training.
- Hyperparameter optimization is configured for 20 Optuna trials across 7 stratified folds.
- The original notebook outputs are retained so the analysis remains auditable; rerunning it regenerates the charts and metrics.

## Dataset columns

See [`data/README.md`](data/README.md) for the required columns and target labels.