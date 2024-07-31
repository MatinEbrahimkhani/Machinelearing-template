# ML_Project

This project provides a framework for applying common machine learning algorithms to various datasets.

## Project Structure

```
ML_Project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   ├── save_load.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── main.py
```

## Installation

1. Clone the repository.
2. Install the required packages:

```sh
pip install -r requirements.txt
```

## Usage

Run the main script with the following command:

```sh
python main.py data/raw/your_data.csv model_type target_column models/your_model.pkl
```

Replace `your_data.csv`, `model_type`, `target_column`, and `your_model.pkl` with your specific file names and parameters.
