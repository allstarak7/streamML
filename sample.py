import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

st.title('Ml4641 Team 5')
st.header("Written Proposal")
st.subheader("3 Sources")
st.header("Contibution Table")
conSer = pd.Series(["Repo Setup, Streamlit, Clean Dataset, Checkpoint", "Writing, Sources, Dataset Retrieval, Timeline (Gantt Chart)",
                   "Writing, Sources", "Video, Writing, Sources", "Video, Writing"], index=["Aditya", "Michael", "Sohum", "William", "David"])
conDf = pd.DataFrame(data=conSer, index=[
                     "Aditya", "Michael", "Sohum", "William", "David"],  columns=["Contributions"])
st.table(conDf)
st.header("Dataset")
data = pd.read_csv("2022-2023 NBA Player Stats - Regular.csv",
                   sep=';', encoding='latin-1')
st.write(data)
st.write("This data currenty encomposses NBA player statistics for the 2022-2023 NBA Season. Eventually, this data will be expanded to around 15-20 seasons for better predictions. Other things that my need to be improved within our data is the recognition of special characters. Also, when players switch teams in the midst of the season they are given more than one data entry, which will need to be consolidated.")
st.header("Checkpoint Definition")
st.header("Timeline")

components.iframe(
    "https://gtvault-my.sharepoint.com/personal/mboling6_gatech_edu/_layouts/15/Doc.aspx?sourcedoc={eb5c569f-4699-4b2d-af77-92c693256e1e}&action=embedview&wdAllowInteractivity=False&wdHideGridlines=True&wdHideHeaders=True&wdDownloadButton=True&wdInConfigurator=True&wdInConfigurator=True", width=700, height=700)


# streamlit run sample.py
