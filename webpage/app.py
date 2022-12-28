## Python Module : Suicide Prediction Website


## library
import streamlit as st
from streamlit_lottie import st_lottie as st_lottie
import json
from PIL import Image
from streamlit.source_util import get_pages
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title="Suicide Prediction Website", page_icon=":tada:", layout="wide")

## load lottie file fucntion
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

## --- Load Assests ---#
lottie1 = load_lottiefile("C:/Users/AlanKoo99/Desktop/FYP coding/webpage/lottiefiles/healthcare.json")
img1 = Image.open("C:/Users/AlanKoo99/Desktop/FYP coding/webpage/images/1.jpg")


# --- Header Section ---#
st.subheader("Universiti Malaysia Sabah Cohort 2019 FYP (Koo Wei Quan BI19110227) :wave:")
st.title("--- Suicide Prediction Website ---")
st.write("A webiste for user to predict suicide from text.")
st.write("[How to Help Someone Who is Suicidal](https://www.youtube.com/watch?v=CAMAnPRLMH8)")


# --- GUIDE ---#
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Guide")

        st.write(
            """
            Procedure of predicting suicide form text
            1. click proceed button in section suicide prediction
            2. upload the text dataset file or input text
            3. click enter and wait for result 
            """
            )
        st.write('##')
        st.write(
            """
             Dataset file format
            - csv file format
            - contain only 1 column (text)
            """
            )
    with right_column:
        st.markdown('<<<<<<<<<<<<<<<<<<<<<<<<**_PREVENTION BETTER THAN CURE_**>>>>>>>>>>>>>>>>>>>>>>>>')
        st_lottie(
            lottie1,
            speed =2,
            reverse =False,
            loop = True,
            quality = "low",
            height = 300,
            width = 600,
            key = None
        )
        st.markdown('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<**_LIFE IS BEAUTIFUL_**>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

with st.container():
    st.write("---")
    # st.header("Suicide Prediction")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img1)
    with text_column:
        st.subheader("Suicide Prediction")
        if st.button('proceed'):
            switch_page("suicide_prediction")








# img = Image.open("C:/Users/AlanKoo99/Desktop/FYP coding/webpage/images/0.jpg")
# with st.container():
#     st.write("---")
#     st.header("My Project")
#     st.write("##")
#     image_column, text_column = st.columns((1,2))
#     with image_column:
#         st.image(img)
#     with text_column:
#         st.subheader("subheader here")
#         st.write(
#             """
#             information here .......
#             """
#         )
#         st.markdown("[watch video...](https://www.youtube.com/watch?v=tO2auFdoFDU)")
# st.write("[learn more emoji >](https://www.webfx.com/tools/emoji-cheat-sheet/)")

