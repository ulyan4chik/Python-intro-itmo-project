import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("matchtv_news.json", encoding="utf-8")
topic_counts = df['topic'].value_counts()

st.title('Распределение тем в новостном паблике Матч ТВ')
sns.set(style="whitegrid", palette="muted")
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x=topic_counts.index, y=topic_counts.values, palette='coolwarm', ax=ax)
ax.set_xlabel('Тема', fontsize=14, fontweight='bold', color='black')
ax.set_ylabel('Количество новостей', fontsize=14, fontweight='bold', color='black')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig)
