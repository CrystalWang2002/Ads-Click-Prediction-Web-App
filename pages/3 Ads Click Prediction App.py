import streamlit as st
import pandas as pd
import pickle
import xgboost as xgb
from sklearn.preprocessing import StandardScaler,LabelEncoder

# Load the trained model from the file
with open('xgb_model.pkl', 'rb') as model_file:
    xgb_model = pickle.load(model_file)

#Load the label encoders for categorical features
with open('label_encoders.pkl', 'rb') as le_file:
    label_encoders = pickle.load(le_file)

# Load the scaler for numerical features
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Load the unique values for categorical features
data = pd.read_csv('data_before_code.csv') 
unique_countries = sorted(data['Country'].unique())
unique_cities = sorted(data['City'].unique())
unique_ad_topic = sorted(data['Ad Topic Line'].unique())

# Define mapping for weekdays
weekdays_mapping = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}

# Define gender options
genders = ['Male', 'Female']

# Design
st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

# Title of the app
st.title('Ad Click Prediction App')
st.write("Fill in the following information to predict whether a user will click on an advertisement.")


# Layout design
#slider input
col1, col2 = st.columns(2)
with col1:
    age = st.number_input('Age', min_value=18, max_value=100, step=1, format='%d')
with col2: 
    gender = st.selectbox('Gender', genders) 

col1, col2, col3 = st.columns(3)

with col1:
    month = st.number_input('Month', min_value=1, max_value=12, step=1)
    ad_topic_line = st.selectbox('Ad Topic Line',unique_ad_topic)
with col2:  
    weekday_name = st.selectbox('Day of the Week', list(weekdays_mapping.keys()))
    country = st.selectbox('Country', unique_countries)
with col3: 
    hour = st.number_input('Hour of the Day', min_value=0, max_value=23, step=1,format='%d') 
    area_income = st.number_input('Area Income (USD)', min_value=15000, max_value=80000, step=1000,format='%d')

#slider input
col1, col2 = st.columns(2)
with col1:
    daily_time_spent_on_site = st.slider('Daily Time Spent on Site (minutes)', 30, 100, step=1)
with col2:
    daily_internet_usage = st.slider('Daily Internet Usage (minutes)', 100, 300, step=1)

# Prepare input features
input_features = {
    'Daily Time Spent on Site': daily_time_spent_on_site,
    'Age': age,
    'Area Income': area_income,
    'Daily Internet Usage': daily_internet_usage,
    'Ad Topic Line': ad_topic_line,
    'Gender': gender,
    'Country': country,
    'hour': hour,
    'weekday': weekdays_mapping[weekday_name],
    'month': month
}
        
# Convert categorical features using label encoders
for feature in ['Gender', 'Country','Ad Topic Line']:
    le = label_encoders[feature]
    input_features[feature] = le.transform([input_features[feature]])[0]

# Scale numerical features
for feature in ['Daily Time Spent on Site','Area Income','Daily Internet Usage','Ad Topic Line','Country']:
    input_features[feature] = scaler.transform([[input_features[feature]]])[0][0]


# Convert categorical features to numerical representation (dummy variables)
input_df = pd.DataFrame([input_features])

# Predict using the model
predicted_click = xgb_model.predict(input_df)[0]

# Display prediction
if st.button('Predict'):
    if predicted_click == 1:
        st.markdown("### 🎉The user is likely to click on the advertisement! ", unsafe_allow_html=True)
    else:
        st.markdown("### 😭The user is unlikely to click on the advertisement...", unsafe_allow_html=True)

