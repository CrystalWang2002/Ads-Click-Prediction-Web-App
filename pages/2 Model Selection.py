import streamlit as st


# set title
st.title("Model Selection")

# part 0
with st.expander("0. Model Performance Overview"):
    st.markdown("""
            **XG Boost** Model is the best model among all the models, with the highest accuracy, AUC and F1 Score.
            So we choose LightGBM Model as our final model.
    """)
    st.image("./pictures/33.png", use_column_width=True)
    st.image("./pictures/34.png", use_column_width=True)
    st.image("./pictures/35.png", use_column_width=True)
    

# part 1
with st.expander("1. Logit Model"):
    st.markdown("""
        ### Model Accuracy: 0.7291
        ### AUC: 0.7881
        ### F1 Score: 0.7154
        """)
    st.markdown("""
we can see almost all the features are significant at 1% level.      
""")
    st.image("./pictures/13.png", caption="logit Result Summary", use_column_width=True)
    st.image("./pictures/14.png", use_column_width=True)
    st.image("./pictures/15.png", use_column_width=True)
    st.image("./pictures/16.png", use_column_width=True)


# part 2
with st.expander("2. Decision Tree Model"):
    st.markdown("""
        ### Model Accuracy: 0.7736
        ### AUC: 0.7736
        ### F1 Score: 0.7738
        """)
    st.image("./pictures/17.png", use_column_width=True)
    st.image("./pictures/18.png", use_column_width=True)
    st.markdown("""
The bar graph show the importance of each feature, we can see the most important feature is the age, then is location, following is Ads Topic.   
""")
    st.image("./pictures/19.png", use_column_width=True)   
    
    
# part 3
with st.expander("3. KNN Model"):
    st.markdown("""
        ### Model Accuracy: 0.8037
        ### AUC: 0.8036
        ### F1 Score:0.7984
        """)
    st.image("./pictures/20.png", use_column_width=True)
    st.image("./pictures/21.png", use_column_width=True)

# part 4
with st.expander("4. SVM Model"):
    st.markdown("""
        ### Model Accuracy: 0.7244
        ### AUC: 0.7245
        ### F1 Score: 0.7006
        """)
    st.image("./pictures/25.png", use_column_width=True)
    st.image("./pictures/26.png", use_column_width=True)

# part 5
with st.expander("5. Random Forest Model"):
    st.markdown("""
        ### Model Accuracy: 0.8264
        ### AUC: 0.8264
        ### F1 Score: 0.8196
        """)
    st.image("./pictures/27.png", use_column_width=True)
    st.image("./pictures/28.png", use_column_width=True)

# part 6
with st.expander("6. LightGBM Model"):
    st.markdown("""
        ### Model Accuracy: 0.8559
        ### AUC: 0.8559
        ### F1 Score: 0.8532
        """)
    st.image("./pictures/29.png", use_column_width=True)
    st.image("./pictures/30.png", use_column_width=True)

# part 7
with st.expander("7. XGBoost Model"):
    st.markdown("""
        ### Model Accuracy: 0.8508
        ### AUC: 0.8508
        ### F1 Score: 0.8479
        """)
    st.image("./pictures/31.png", use_column_width=True)
    st.image("./pictures/32.png", use_column_width=True)

