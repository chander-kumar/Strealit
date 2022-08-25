import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

col1, col2 = st.columns([3,1])
col1.title('**My simple title**')
col2.write({"key1":1,"key2":2})

# Titanic=sns.load_dataset('titanic')
# df_gender=pd.get_dummies(Titanic["sex"])
# Titanic=pd.concat([Titanic,df_gender],axis=1)
# Titanic.drop(['sex',"survived","adult_male","deck","alone","embark_town","class","alive","who"],axis=1,inplace=True)
# Titanic.dropna(axis=0,inplace=True) 