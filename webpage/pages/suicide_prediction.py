## Python Module : Suicide Prediction Website


## library
import streamlit as st
from streamlit_lottie import st_lottie as st_lottie
import json
from PIL import Image
import data_loading
import testing_3_instance_typing
import text_highlight
import pandas as pd
import data_preprocessing
import feature_engineering_sentiment_polarity
import feature_engineering_emotion
import prediction_model
import statistical_analysis
import suicide_keyword_analysis

st.set_page_config(page_title="prediction model", page_icon=":tada:", layout="wide")

## load lottie file fucntion
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# --- Load Assests ---#
# lottie1 = load_lottiefile("C:/Users/AlanKoo99/Desktop/FYP coding/webpage/lottiefiles/healthcare.json")
img1 = Image.open("C:/Users/AlanKoo99/Desktop/FYP coding/webpage/images/2.png")
data = data_loading.load_data(r'C:\Users\AlanKoo99\Desktop\FYP coding\data\experiment_test_2_emotion.csv')

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.placeholder = "input text here"   
        
# --- Header Section ---#
st.subheader("Universiti Malaysia Sabah Cohort 2019 FYP (Koo Wei Quan BI19110227) :wave:")
st.title("--- Suicide Prediction Website ---")
st.write("A webiste for user to predict suicide from text.")
st.write("[How to Help Someone Who is Suicidal](https://www.youtube.com/watch?v=CAMAnPRLMH8)")

def v_spacer(height):
    for _ in range(height):
        st.write('\n')
right_sec = 0

# --- Suicide prediction with uploaded dataset ---#
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Please Upload Dataset File")
        uploaded_files = st.file_uploader("Upload CSV dataset file")
        if uploaded_files is not None:
            right_sec = 1
            uploaded_data = pd.read_csv(uploaded_files)
            st.write(uploaded_data)
            # st.write(uploaded_data.text[0])
            uploaded_data = data_preprocessing.row_removal_missing_data(uploaded_data)
            uploaded_data = data_preprocessing.expand_contractions(uploaded_data)
            uploaded_data = data_preprocessing.punctuation_removal(uploaded_data)
            uploaded_data = data_preprocessing.stop_words_removal(uploaded_data) 
            uploaded_data = data_preprocessing.lower_casing(uploaded_data)
            uploaded_data = data_preprocessing.stemming(uploaded_data) 
            uploaded_data = data_preprocessing.lemmatization(uploaded_data)
            uploaded_data = data_preprocessing.digit_removal(uploaded_data) 
            uploaded_data = data_preprocessing.removal_rephrase_unwanted_pattern_text(uploaded_data)
            uploaded_data = data_preprocessing.removal_duplicate_data(uploaded_data)
            uploaded_data = feature_engineering_sentiment_polarity.feature_engineering_Sentiment_Polarity(uploaded_data)
            uploaded_data = feature_engineering_emotion.feature_engineering_Emotion(uploaded_data)
            uploaded_data_result = prediction_model.model_20_testing(data, uploaded_data)
            sp_class_value, sp_level_value, emotion_value, new_overall, new_overall1 = statistical_analysis.statistic_analysis(uploaded_data_result)
            word_data = suicide_keyword_analysis.suicide_keyword_analysis(uploaded_data_result)
            
            
            
    with right_column:
        if right_sec == 1:
            v_spacer(height=12)
            st.subheader("Suicide Prediction Result")
            # uploaded_data = pd.read_csv(uploaded_files)
            st.write(uploaded_data_result)    
            
            ##print result button
            def convert_df(df):
                return df.to_csv(index=False).encode('utf-8')
            csv = convert_df(uploaded_data)
            csv_result = convert_df(uploaded_data_result)
            st.download_button(
               "Press to Download Result",
               csv_result,
               "result.csv",
               "text/csv",
               key='download-csv'
            )

#--- Statistical result1 ---#
if right_sec == 1:
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Statistical result")
            st.subheader("Number of Suicide Text with Different Class of Sentiment Polarity")
            statistical_analysis.bar_pie_plot_1_1(sp_class_value)
        with right_column:
            v_spacer(height=6)
            st.subheader("Number of Suicide Text with Different Class of Sentiment Polarity")
            statistical_analysis.bar_pie_plot_1_2(sp_class_value)

#--- Statistical result2 ---#
if right_sec == 1:
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Number of Suicide Text with Different Level of Sentiment Polarity")
            statistical_analysis.bar_pie_plot_2_1(sp_level_value)
        with right_column:
            st.subheader("Number of Suicide Text with Different Level of Sentiment Polarity")
            statistical_analysis.bar_pie_plot_2_2(sp_level_value)

#--- Statistical result3 ---#
if right_sec == 1:
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Number of Suicide Text with Different Emotion Class")
            statistical_analysis.bar_pie_plot_3_1(emotion_value)
        with right_column:
            st.subheader("Number of Suicide Text with Different Emotion Class")
            statistical_analysis.bar_pie_plot_3_2(emotion_value)

#--- Statistical result4 ---#
if right_sec == 1:
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Number of Suicide Text with Different Combination of Sentiment Polarity Class and Emotion")
            statistical_analysis.bar_pie_plot2_1(new_overall)
        with right_column:
            st.subheader("Number of Suicide Text with Different Combination of Sentiment Polarity Level and Emotion")
            statistical_analysis.bar_pie_plot2_2(new_overall1)

#--- Wordcloud result ---#
if right_sec == 1:
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Positive Word Cloud")
            suicide_keyword_analysis.word_cloud(word_data.pos_word)    
        with right_column:
            st.subheader("Negative Word Cloud")
            suicide_keyword_analysis.word_cloud(word_data.neg_word)


# --- Suicide prediction with input text ---#
with st.container():
    st.write("---")
    # st.header("Input Text")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img1)
    with text_column:
        st.header("Input Text")
        text_input = st.text_input(
            "Input text :",
            label_visibility = st.session_state.visibility,
            disabled = st.session_state.disabled,
            placeholder = st.session_state.placeholder,
        )
        if text_input:
            st.subheader("Suicide Prediction Result")
            # text_replaced = text_highlight.highlight_keyword(text_input)
            st.write("You entered: ", text_input)
            pos, neg, compound, emotion, p_result =testing_3_instance_typing.model_20_testing(data, text_input)
            st.write("positive polarity: ", pos)
            st.write("negative polarity: ", neg)
            st.write("compound polarity: ", compound)
            st.write("emotion: ", emotion)
            st.write("prediction: ", p_result[0])
        # st.write(
        #     """
        #     information here .......
        #     """
        # )
        # if st.button('Print Result'):
        #     st.write('OK')
        # st.markdown("[watch video...](https://www.youtube.com/watch?v=tO2auFdoFDU)")






