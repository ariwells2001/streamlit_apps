import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Palmer's Penguins")
#penguins_df = pd.read_csv("penguins.csv")
#st.write(penguins_df.head())

#selected_species = st.selectbox("What species would you like to visualize?",['Adelie','Gentoo','Chinstrap'])
selected_x_var = st.selectbox("What woudl you want the x variable to be?",['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])
selected_y_var = st.selectbox('What about the you?',['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])

penguin_file = st.file_uploader('Select Your Local Penguins CSV')
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    st.stop()
#selected_penguin = penguins_df[penguins_df['species'] == selected_species]
#st.write(selected_penguin.head())
sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap": 'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(data=penguins_df,x = selected_x_var,y = selected_y_var, hue='species', markers = markers, style = 'species')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Scatterplot of Palmer's Penguins")
st.pyplot(fig)
st.button("Re-run")










