import streamlit as st

st.title("Main Page")

st.write("""
### Welcome to this ML Project for Ads Click Prediction!👩🏻‍💻
         
### 1.Project Background📝   
In the rapidly evolving digital marketing landscape, understanding the factors that influence user behavior is crucial for optimizing ad campaigns. 
The ability to predict whether a user will click on an advertisement can significantly enhance targeting strategies, 
leading to better engagement and higher conversion rates. This project aims to explore the key determinants of user clicks and develop 
predictive models to forecast click behavior.


### 2.Exploratory Data Analysis (EDA)🔍
The project begins with a comprehensive exploratory data analysis (EDA) to understand the underlying patterns and relationships within the dataset. 
Key statistics, distributions, and correlations between variables are examined. Visualizations are used to identify trends and outliers 
that may impact model performance.

### 3.Model Selection📈
Following the EDA, multiple machine learning models are employed to predict user click behavior. The models used include:
- **Logistic Regression** 
- **Decision Tree**
- **Random Forest** 
- **K-Nearest Neighbors (KNN)** 
- **Support Vector Machine (SVM)** 
- **Light GBM** 
- **XGBoost** 

Each model is trained and evaluated using standard metrics such as accuracy, ROC-AUC score and F1-score. 

### 4. Ads click Prediction App📲
The final part of the project involves developing a user-friendly web interface.
This allows users to input specific parameters, enabling the system to predict whether a user will click on an advertisement based on the XGBoost model.

""")
