import streamlit as st
import pandas as pd
import numpy as np

st.title('Ml4641 Team 5')
st.header("Written Proposal")
st.subheader("3 Sources")
st.header("Contibution Table")
conSer = pd.Series(["Clean Dataset, Sources","Writing, Sources","Writing","Video, Sources","Video"], index = ["Aditya", "Matthew", "Sohum", "William", "David"])
conDf = pd.DataFrame(data=conSer, index = ["Aditya", "Matthew", "Sohum", "William", "David"],  columns=["Contributions"])
st.table(conDf)
st.header("Dataset")
data = pd.read_csv("2022-2023 NBA Player Stats - Regular.csv", sep=';',encoding='latin-1')
print(data)
st.write(data)
st.header("Checkpoint Definition")
st.header("Timeline")


# streamlit run sample.py