import streamlit as st
import seaborn as sns
import pandas as pd
import altair as alt
pengs = sns.load_dataset("penguins")
#df_form = pd.DataFrame(pengs.data)
st.write("""
# Penguins Dataset
How penguins dataset vary with the species 
""")
dom = ['Biscoe', 'Dream', 'Torgersen']
rng = ['red', 'green', 'black']

pengs_model = alt.Chart(pengs).mark_point().encode(x=alt.X("flipper_length_mm",axis=alt.Axis(title='flipper_length_mm', grid=False)),y=alt.Y("body_mass_g",axis=alt.Axis(title='body_mass_g', grid=False)),
                                    color=alt.Color('island', legend=alt.Legend(title="island by color",orient='left'),scale=alt.Scale(domain=dom, range=rng)),tooltip=['island','flipper_length_mm','bill_length_mm','body_mass_g','sex'], 
                                   facet=alt.Facet('species', columns=1),).properties(title='filpper_length vs body_mass of various species',width=300,height=250).configure_view(strokeWidth=0).interactive()
st.altair_chart(pengs_model)