import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_excel("C://Users//KAVYASRI//Downloads//finalDAdata.xlsx")
st.dataframe(df.head())
st.divider()

# Define columns globally after loading the dataframe
columns = df.columns.tolist()
# Multivariate Analysis
st.subheader(":blue[Multivariate Analytics (Multiple Column Data Study):]")
st.divider()

# Let the user choose multiple columns for multivariate analysis
st.sidebar.header("Select Columns for Multivariate Analysis")
selected_columns = st.sidebar.multiselect("Select Columns for Multivariate Analysis", columns, default=columns[:3])

# Function for multivariate analysis
def multivariate_analysis(df, selected_columns):
    # Check if selected columns are numeric
    numeric_columns = df[selected_columns].select_dtypes(include=[np.number]).columns.tolist()

    if len(numeric_columns) > 1:
        # Pairplot (Pairwise relationships in a dataset)
        st.subheader("Pairplot (Pairwise relationships between selected columns)")
        pairplot = sns.pairplot(df[numeric_columns])
        st.pyplot(pairplot)

        # Correlation Heatmap
        st.subheader("Correlation Heatmap between selected variables")
        corr_matrix = df[numeric_columns].corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        st.pyplot(plt)

        # 3D Scatter Plot (if there are 3 numeric columns selected)
        if len(numeric_columns) >= 3:
            from mpl_toolkits.mplot3d import Axes3D
            st.subheader("3D Scatter Plot between 3 numeric columns")
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')

            # Create 3D scatter plot
            ax.scatter(df[numeric_columns[0]], df[numeric_columns[1]], df[numeric_columns[2]], c='r', marker='o')
            ax.set_xlabel(numeric_columns[0])
            ax.set_ylabel(numeric_columns[1])
            ax.set_zlabel(numeric_columns[2])
            st.pyplot(fig)
    else:
        st.write("Please select at least two numeric columns for multivariate analysis.")

# Perform multivariate analysis if columns are selected
if selected_columns:
    multivariate_analysis(df, selected_columns)

