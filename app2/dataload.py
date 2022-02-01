import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import time


st.title("Palmer's Penguins")
penguin_file = st.file_uploader('Select Your Local Penguins CSV')

@st.cache
def load_file(penguin_file):
    time.sleep(10)
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv('penguins.csv')
    return (df)

penguins_df = load_file(penguin_file)

#selected_species = st.selectbox("What species would you like to visualize?",['Adelie','Gentoo','Chinstrap'])
selected_x_var = st.selectbox("What woudl you want the x variable to be?",['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])
selected_y_var = st.selectbox('What about the you?',['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])
selected_gender = st.selectbox('What gender do you want to filter for?',['all penguins','male penguins','female penguins'])

if selected_gender == 'male penguins':
    penguins_df = penguins_df[penguins_df['sex']== 'male']
elif selected_gender == 'female penguins':
    penguins_df = penguins_df[penguins_df['sex']== 'female']
else:
    pass



#selected_penguin = penguins_df[penguins_df['species'] == selected_species]
#st.write(selected_penguin.head())
sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap": 'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(data=penguins_df,x = selected_x_var,y = selected_y_var, hue='species', markers = markers, style = 'species')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Scatterplot of Palmer's Penguins: {}".format(selected_gender))
st.pyplot(fig)
st.button("Re-run")