import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Palmer's Penguins")
penguins_df = pd.read_csv("penguins.csv")
st.write(penguins_df.head())

selected_species = st.selectbox("What species would you like to visualize?",['Adelie','Gentoo','Chinstrap'])
selected_x_var = st.selectbox("What woudl you want the x variable to be?",['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])
selected_y_var = st.selectbox('What about the you?',['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])

selected_penguin = penguins_df[penguins_df['species'] == selected_species]
st.write(selected_penguin.head())

fig, ax = plt.subplots()
ax = sns.scatterplot(x = selected_penguin[selected_x_var],y = selected_penguin[selected_y_var])
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title('Scatterplot of {} Penguins'.format(selected_species))
st.pyplot(fig)
st.button("Re-run")