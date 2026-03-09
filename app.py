import streamlit as st
import pandas as pd
from datalab.loader import load_data
from datalab.cleaner import clean_missing
from datalab.analyzer import show_summary
from datalab.visualizer import plot_column

st.set_page_config(page_title="Mini DataLab", page_icon="📊")

st.title("📊 Mini DataLab")
st.write("Simple data analysis tool built with Python.")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Preview of Dataset")
    st.dataframe(df.head())

    st.sidebar.title("Actions")

    option = st.sidebar.selectbox(
        "Choose Action",
        ["Show Summary", "Clean Missing Values", "Plot Column"]
    )

    if option == "Show Summary":
        st.subheader("Summary Statistics")
        st.write(df.describe())

    elif option == "Clean Missing Values":
        df = clean_missing(df)
        st.success("Missing values removed.")
        st.dataframe(df)

    elif option == "Plot Column":

        numeric_columns = df.select_dtypes(include="number").columns

        column = st.selectbox(
            "Select numeric column",
            numeric_columns
        )

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.hist(df[column])
        ax.set_title(f"Distribution of {column}")

        st.pyplot(fig)

else:
    st.info("Upload a CSV file to begin.")
