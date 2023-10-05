import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

st.title('Ml4641 Team 5')
st.header("Written Proposal")
st.subheader("Intro/Background")
st.write("The National Basketball Association (NBA) is one of the biggest professional sports organizations in the world. With hundreds of players, dozens of teams, and over 1,000 games played per season, there is a vast amount of data available to analyze. Due to this, many efforts have been made to use AI and Machine Learning methods to predict basketball outcomes. IBM first utilized data mining in the 90’s with Advanced Scout, a tool for NBA management to better analyze hidden trends in basketball statistics (Colet, 1997). Independent projects have also been led, like Nigel Ma developing a model to predict a team’s playoff chances (Ma, 2021) or a group of Carnegie Mellon students using classification methods to predict individual game outcomes (Beckler, Wang, Papamichael).")
st.write("In this project, we are attempting to predict the winners of various awards given out annually by the NBA, such as Most Valuable Player (MVP), Defensive Player of the Year (DPOY), Most Improved Player, and more. Using features like individual players’ stats, team(s) played for, etc. over multiple years, we will train a model to predict the winners of different awards for the upcoming 2023-2024 NBA season.")
st.subheader("Problem Definition")
st.write("Our objective is to create a predictive model that can estimate the chances of an NBA player winning awards like MVP or Defensive Player of the Year based on their season statistics. We aim to explore how player performance metrics relate to these award outcomes.")
st.subheader("Methods & Algos")
st.write("We will use the Gaussian Means Model to gain a comprehensive view of player performance with soft clustering. This will allow us to organize our data in the exploratory analysis phase. We will then employ linear regression models to analyze a multitude of player statistics as independent variables, aiming to predict the likelihood of winning NBA awards like the MVP, Defensive Player of the Year, and more. This method involves data collection, preprocessing, and feature selection to identify influential metrics. We’ll create separate regression models for each award, utilizing historical award data for training and evaluation.")
st.subheader("Potential Outcomes, Results")
st.write("The goal is to explore the statistical relationships between player performance metrics and award outcomes, recognizing that while statistical factors play a role, the model may not account for subjective elements like team success and voter bias that influence award decisions. ")
st.subheader("3 Sources")
st.write("Bhandari, I., Colet, E., Parker, J. et al. Advanced Scout: Data Mining and Knowledge Discovery in NBA Data. Data Mining and Knowledge Discovery 1, 121–125 (1997). https://doi.org/10.1023/A:1009782106822")
st.write("N. Ma, NBA Playoff Prediction Using Several Machine Learning Methods, 2021 3rd International Conference on Machine Learning, Big Data and Business Intelligence (MLBDBI), Taiyuan, China, 2021, pp. 113-116, doi: 10.1109/MLBDBI54094.2021.00030.")
st.write("Beckler, M., Wang, H., &amp; Papamichael, M. (n.d.). (rep.). NBA Oracle. https://www.mbeckler.org/coursework/2008-2009/10701_report.pdf")
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