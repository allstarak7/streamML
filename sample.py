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
st.write("Some columns of the dataset contained missing values, specifically statistics that involved some sort of percentage (i.e. 3 point percentage, free throw percentage, etc.). This was due to some players attempting zero shots, resulting in an undefined value. We decided that the best fix for this was to impute the mean of those columns, essentially making the assumption that if those players were to attempt shots, they would complete them at a percentage equal to the average of all other players in the league.")
st.write("To reduce the size of the dataset and remove irrelevant data (players that have essentially zero chance of winning the MVP award), we determined that for a player’s stats to be taken into account, they must meet a threshold of 10 minutes played per game, around one standard deviation from the mean. This removed around 3,000 rows, which will hopefully aid with model efficiency and accuracy. To further improve our models in the future, we will consider increasing this threshold to further narrow the dataset.")
st.write("To select the features for training, we made a few important modifications to the dataset. First, we removed some redundant features that could be derived from others; for example, since field goals made can be directly calculated from field goal percentage and field goals attempted, that column was removed.")
st.write("Next, we selected a group of features that we felt were crucial to a player’s MVP chances based on our previous knowledge of the sport. These are features like points, rebounds, assists, field goal percentage, etc.")
st.write("To further select important features, we utilized a basic variance threshold. All columns with a variance less than 1 were removed from the dataset. This was done as an effort to remove statistics that don’t vary much from player to player, and are therefore not informative when training our models. This removed around 15 features, leaving us with around 35. After examining the new list of features, we determined with our knowledge of the sport that they were a good representation of statistics that might impact a player’s MVP chances.")
st.write("When we have more models implemented in the future, we will explore utilizing other methods like forward or backward feature selection. This will be a more comprehensive method of determining the best features and will ensure maximum model accuracy.")
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