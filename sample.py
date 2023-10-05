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
st.write("This data currenty encomposses NBA player statistics for the 2022-2023 NBA Season. Eventually, this data will be expanded to around 15-20 seasons for better predictions. Other things that may need to be improved within our data is the recognition of special characters. Also, when players switch teams in the midst of the season they are given more than one data entry, which will need to be consolidated.")
st.header("Checkpoint Definition")
st.write("The definition of checkpoint will be defined by three things:")
st.write("1. Linear regression has been performed on the data")
st.write("2. The 2022-2023 MVP, DPOY, MIP, and Allstar teams have been predicted and cross-verified for accuracy")
st.write("3. The model is trained with the past 15 years of NBA statistical data for future predictions")
st.header("Timeline")

components.iframe(
    "https://onedrive.live.com/embed?resid=A783CC250FA9C04A%21105&authkey=%21AA3CMjNWTL09IXg&em=2&wdAllowInteractivity=False&wdHideGridlines=True&wdHideHeaders=True&wdDownloadButton=True&wdInConfigurator=True&wdInConfigurator=True", width=700, height=700)
st.write("If the timeline is not showing up please click this link: https://1drv.ms/x/s!AkrAqQ8lzIOnaYbrezMNI7FvfSA?e=FML6C2&nav=MTVfezAwMDAwMDAwLTAwMDEtMDAwMC0wMTAwLTAwMDAwMDAwMDAwMH0")
