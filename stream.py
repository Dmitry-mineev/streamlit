import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from datetime import date


st.title('Котировки акций компании Apple')

AAPL = yf.download('AAPL',start='2000-01-01', end=date.today())
AAPL.columns = AAPL.columns.droplevel(1)

def convert_df(AAPL):
   return AAPL.to_csv().encode("utf-8")

csv = convert_df(AAPL)

if 'button_clicked' not in st.session_state:
   st.session_state.button_clicked = False

def button_click():
   st.session_state.button_clicked = True

st.button('Показать', on_click=button_click)
    
if st.session_state.button_clicked: 
    st.sidebar.header('Диапазон')
    start = st.sidebar.date_input('Дата начала', AAPL.reset_index()['Date'].min())
    end = st.sidebar.date_input('Дата окончания')
    st.subheader(f'данные с {start} по {end}')
    st.write(AAPL.loc[start:end])
    st.download_button(label='Скачать', data=csv, file_name="Cotirovki.csv", mime="csv")