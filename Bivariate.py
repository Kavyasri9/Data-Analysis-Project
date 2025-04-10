import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_excel("C://Users//KAVYASRI//Downloads//finalDAdata.xlsx")
st.dataframe(df.head())
st.divider()
# Bivariate Analysis
st.subheader(":red[Bivariate Analytics (Two Column Data Study):]")
st.divider()

# Let the user choose columns for bivariate analysis
st.sidebar.header("Select Columns for Bivariate Analysis")
columns = df.columns.tolist()
x_column = st.sidebar.selectbox("Select X Column", columns, index=0)
y_column = st.sidebar.selectbox("Select Y Column", columns, index=1)

# Function for bivariate analysis
def bivariate_analysis(df, x_column, y_column):
    # Check if both columns are numeric before calculating correlation
    if pd.api.types.is_numeric_dtype(df[x_column]) and pd.api.types.is_numeric_dtype(df[y_column]):
        # Calculate correlation
        correlation = df[[x_column, y_column]].corr().iloc[0, 1]
        st.write(f"Correlation between {x_column} and {y_column}: {correlation:.2f}")
    else:
        st.write(f"Cannot calculate correlation because one or both columns ({x_column}, {y_column}) are non-numeric.")
    # Scatter Plot
    st.subheader(f"Scatter Plot between {x_column} and {y_column}")
    plt.figure(figsize=(8, 6))
    plt.xticks(rotation=90)
    sns.scatterplot(data=df, x=x_column, y=y_column)
    st.pyplot(plt)
    # Box Plot: To show distribution of `y_column` across categories of `x_column`
    st.subheader(f"Box Plot of {y_column} by {x_column}")
    plt.figure(figsize=(8, 6))
    plt.xticks(rotation=90)
    sns.boxplot(data=df, x=x_column, y=y_column)
    st.pyplot(plt)

    # Bar Chart: Aggregated values (mean) of `y_column` grouped by `x_column`
    st.subheader(f"Bar Chart of mean {y_column} by {x_column}")
    bar_data = df.groupby(x_column)[y_column].mean().reset_index()
    plt.figure(figsize=(8, 6))
    plt.xticks(rotation=90)
    sns.barplot(data=bar_data, x=x_column, y=y_column)
    st.pyplot(plt)

# Perform bivariate analysis if columns are selected
if x_column and y_column:
    bivariate_analysis(df, x_column, y_column)

