Novozymes Enzyme Stability Prediction
==============================

This project aims to address a featured prediction competition problem from the Kaggle plataform named: __Novozymes Enzyme Stability Prediction__.
The objective is to identify the thermostable mutations in enzymes. In other words, the goal is to determine the change on the thermostability (tm) (also known as melting temperature) of enzyme variants.
This is done through the analysis of the effect on single (or multiple) mutation(s) in a protein sequence.

For instance, lets say we have the following protein sequence, with it's corresponding tm:

`sequence, tm = "PROTEINSEQUENCE", 65`

And a mutation of the sequence

`mut_sequence, new_tm = "PROTEINQEQUENCE", 60`

Our task will be to predict the `new_tm` with the `sequence` and `mut_sequence` information.

For more information you can access the following [link](https://www.kaggle.com/competitions/novozymes-enzyme-stability-prediction/overview/description)



![](./img1.jpg)



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. 
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


--------

Important dates:

- September 21, 2022 - Start Date.
- December 27, 2022 - Entry Deadline. You must accept the competition rules before this date in order to compete.
- December 27, 2022* - Team Merger Deadline. This is the last day participants may join or merge teams.
- January 3, 2023 - Final Submission Deadline.