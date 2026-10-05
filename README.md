# 🚀 SpaceY IBM Data Science Capstone Project

## Project Overview

This project was developed as part of the IBM Data Science Professional Certificate Capstone.

The objective is to analyze SpaceX Falcon 9 launch data and build predictive models capable of estimating whether the first-stage booster will successfully land after launch.

Successful booster recovery significantly reduces launch costs, which is one of the main competitive advantages of SpaceX. Through data collection, exploratory analysis, visualization, dashboard development, and machine learning, this project investigates the factors that influence launch success.

---

## Business Problem

SpaceY wants to compete with SpaceX in the commercial aerospace industry.

Since a significant portion of launch costs is related to the first-stage booster, being able to predict whether a Falcon 9 booster will successfully land helps estimate the overall launch cost.

The goal of this project is to predict booster landing success using historical launch data.

---

## Project Workflow

### 1. Data Collection

Data was collected from:

- SpaceX REST API
- Wikipedia Falcon 9 launch records

Files:

- `jupyter-labs-spacex-data-collection-api.ipynb`
- `jupyter-labs-webscraping.ipynb`

---

### 2. Data Wrangling

Data cleaning and preprocessing activities included:

- Handling missing values
- Feature engineering
- Creation of the target variable (Class)

Files:

- `labs-jupyter-spaceX-Data wrangling.ipynb`

---

### 3. Exploratory Data Analysis (EDA)

Exploratory analysis was performed using:

- SQL queries
- Statistical summaries
- Visual analytics

Files:

- `jupyter-labs-eda-sql-coursera_sqlite.ipynb`
- `edadataviz.ipynb`

---

### 4. Geospatial Analysis

Launch site locations were analyzed using Folium maps.

Activities included:

- Launch site mapping
- Success and failure visualization
- Distance analysis to nearby infrastructure

Files:

- `lab_jupyter_launch_site_location.ipynb`

---

### 5. Interactive Dashboard

A Plotly Dash application was developed to allow interactive exploration of launch data.

Features include:

- Launch site selection
- Success rate visualization
- Payload range filtering
- Booster analysis

Files:

- `spacex-dash-app.py`
- `Dashboard with Plotly Dash.docx`

---

### 6. Predictive Modeling

Several machine learning algorithms were trained and evaluated:

- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- K-Nearest Neighbors (KNN)

Hyperparameter optimization was performed using GridSearchCV and cross-validation.

File:

- `SpaceX_Machine_Learning_Prediction.ipynb`

---

## Technologies Used

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Folium
- Plotly Dash
- SQLite
- Scikit-Learn

---

## Machine Learning Results

The following classification algorithms were evaluated:

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 83.33% |
| Support Vector Machine | 83.33% |
| Decision Tree | 83.33% |
| K-Nearest Neighbors | 83.33% |

All models achieved similar performance on the test dataset.

---

## Repository Structure

```text
SpaceY_IBM-Data-Science-Project
│
├── README.md
├── jupyter-labs-spacex-data-collection-api.ipynb
├── jupyter-labs-webscraping.ipynb
├── labs-jupyter-spaceX-Data wrangling.ipynb
├── jupyter-labs-eda-sql-coursera_sqlite.ipynb
├── edadataviz.ipynb
├── lab_jupyter_launch_site_location.ipynb
├── SpaceX_Machine_Learning_Prediction.ipynb
├── spacex-dash-app.py
└── Dashboard with Plotly Dash.docx
```


---

## Author

**Andres Julian Restrepo Duque**

IBM Data Science Professional Certificate Capstone Project
