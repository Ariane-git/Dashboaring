import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('bank.csv')
st.set_page_config(page_title="Bank Time Science Dashboard",page_icon="✅", layout="wide")
st.title("Real Time/Live Data Analysis Dashboard")

#filtrer sur le type job
job_filter=st.selectbox("Select a Job", pd.unique(df["job"]))

#creer un endroit p[our le filtre
df=df[df["job"]==job_filter]

#indicateurs
avg_age=np.mean(df["age"])
count_married= int(df[(df["marital"]== 'married')]['marital'].count())
balance=np.mean(df["balance"])

kpi1, kpi2, kpi3= st.columns(3)
kpi1.metric(label="Age ⏳", value=round(avg_age),delta=round(avg_age))
kpi2.metric(label="Married 💍", value=int(count_married), delta=round(count_married))
kpi3.metric(label="Balance 💰", value=f"${round(balance, 2)}", delta=round(balance/count_married)*100)

#graphiques
col1, col2= st.columns(2)
with col1:
    st.markdown("### FIRST CHART")
    fig1=plt.figure()
    sns.barplot(data=df, x="marital", y="age",palette="mako")
    st.pyplot(fig1)
with col2:
    st.markdown("### SECOND CHART")
    fig2=plt.figure()
    sns.histplot(data=df, y="age", bins=20, color="green")
    st.pyplot(fig2)
    
st.markdown("###DETAILLED Data VIEW")
st.dataframe(df)   