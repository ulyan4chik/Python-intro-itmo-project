import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


with open("../data/lemmatized_text", "r", encoding="utf-8") as f:
    lemmatized_text = f.read()

teams = ["зенит", "спартак", "динамо", "цска", "локомотив", "рубин", "ростов", "краснодар", "ахмат", "урал", "крылья советов", "сочи", "факел", "торпедо", "партизан", "ротор"]
mention_counts = {team: lemmatized_text.count(team) for team in teams}

st.title('Частота упоминания команд')
sns.set(style="whitegrid", palette="muted")
fig, ax = plt.subplots(figsize=(14, 7))
sns.barplot(x=list(mention_counts.keys()), y=list(mention_counts.values()), palette='hls')
ax.set_xlabel('Команда', fontsize=14, fontweight='bold', color='black')
ax.set_ylabel('Количество упоминаний', fontsize=14, fontweight='bold', color='black')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig)
