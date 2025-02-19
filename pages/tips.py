import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io 
from datetime import date

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)

st.title('Исследование по чаевым\n (датасет tips.csv)')

start = st.sidebar.date_input('Начало', '2023-01-01')
end = st.sidebar.date_input('Конец', date.today())

q = pd.date_range(start = start, end = end)
tips['time_order'] = np.random.choice(q, size=len(tips))
q = tips.groupby('time_order')['tip'].sum().reset_index()

st.header('Динамика')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=q , x='time_order', y='tip')
plt.ylabel('Чаевые')
plt.xlabel('Период')
st.pyplot(fig)
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
st.download_button("Скачать график", data=buf, file_name='Dinamika.png',mime='image/png')

st.header('Распределение на обед и ужин')
r = tips.query('time == "Dinner"')
e = tips.query('time == "Lunch"')
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
sns.histplot(r['tip'], bins=10, ax=axes[0],color='red')
plt.ylabel('Количество')
plt.xlabel("Чаевые")
sns.histplot(e['tip'], bins=10, ax=axes[1])
plt.ylabel('Количество')
plt.xlabel("Чаевые")
axes[1].set(title = 'Обед')
axes[0].set(title = 'Ужин')
st.pyplot(fig)
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
st.download_button("Скачать график", data=buf, file_name='Raspredelenie.png',mime='image/png')