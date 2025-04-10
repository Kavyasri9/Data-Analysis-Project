# Base Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


import warnings
warnings.filterwarnings("ignore")

# UI Library

import streamlit as st

################################# Dashboard ##########################################

# Ref for Streamlit commands: https://docs.streamlit.io/develop/api-reference

st.subheader(":green[Sample Data Analytics]")
st.divider()
st.write(":blue[Data Taken For Analysis..]")
df = pd.read_excel("C://Users//KAVYASRI//Downloads//finalDAdata.xlsx")
st.dataframe(df.head())
st.divider()
st.subheader(":red[Uni-Variate Analytics (Single Column Data Study):]")
st.divider()

cola, colb , colc = st.columns(3)
with colb:
    colname = st.selectbox("Select Column:", df.columns)

if df[colname].dtype==object:
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"{colname} Stats:")
        st.divider()
        st.write(df[colname].value_counts())
    with col2:
        st.write(f"{colname} Bar Chart:")
        st.divider()
        st.bar_chart(df[colname].value_counts())
