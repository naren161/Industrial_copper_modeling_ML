# Industrial_copper_modelling_using_ML

The Industrial Copper Modelling is a Streamlit application designed for predicting copper prices and determining the status of transactions based on input features. The application leverages machine learning models, specifically a RandomForestRegressor for copper price prediction and a RandomForestClassifier for status prediction.

**Introduction** : The objective of this project is to create two machine learning models specifically designed for the copper business. These models will be developed to tackle the difficulties associated with accurately anticipating selling prices and effectively classifying lead. The process of making forecasts manually may be a time-intensive task and may not provide appropriate price choices or effectively collect leads. The models will employ sophisticated methodologies, including data normalization, outlier detection and treatment, handling of improperly formatted data, identification of feature distributions, and utilization of tree-based models, particularly the decision tree algorithm, to accurately forecast the selling price and leads.

## Prerequisites
1. **Python** -- Programming Language
2. **pandas** -- Data Preprocessing
3. **Matplotlib and Seaborn** --Data Visualisation
4. **Streamlit** --  User Interface
5. **scikit-learn** -- Machine Learning library for the Python programming language

## Project Workflow
The following is a fundamental outline of the project:
  - This analysis aims to investigate the presence of skewness and outliers within the dataset.
  - The data will be converted into a format that is appropriate for analysis, and any required cleaning and pre-processing procedures will be carried out.
  - The objective of this study is to construct a machine learning regression model that utilizes the decision tree regressor to accurately forecast the continuous variable 'Selling_Price'.
  - The objective of this study is to construct a machine learning classification model using the decision tree classifier to accurately predict the outcome of a given task, namely whether it will result in a "WON" or "LOST" status.
  - The objective is to develop a Streamlit webpage that enables users to input values for each column and get the expected Selling_Price value or determine the Status (Won/Lost).
