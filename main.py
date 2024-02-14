import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
import pandas as pd

st.set_page_config(layout="wide")

st.title('Try Mito: Use the spreadsheet below to generate Python')

@st.cache_data
def get_tesla_data():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/tesla-stock-price.csv')
    df = df.drop(0)
    df['volume'] = df['volume'].astype(float)
    return df

tesla_data = get_tesla_data()

new_dfs, code = spreadsheet(tesla_data)
st.code(code)