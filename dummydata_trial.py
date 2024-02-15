import pandas as pd
import altair as alt

# Create the DataFrame
dat = pd.DataFrame({
    'studynames': ['study1', 'study1', 'study1', 'study1', 'study1', 'study1', 'study2', 'study2', 'study2', 'study2','study3', 'study3', 'study3', 'study3'],
    'Treatment': ['RYGB', 'SG', 'CG', 'RYGB', 'SG', 'CG','BAND','COT','BAND','COT','SOG','MT','SOG','MT'],
    'Class': ['intervention', 'intervention', 'control', 'intervention', 'intervention', 'control','intervention', 'control','intervention', 'control','intervention', 'control','intervention', 'control'],
    'BMI': [25, 20, 30, 40, 35, 32,21,30,29,26,21,30,29,26],
    'SBP': [120, 119, 130, 115, 140, 126,120,110,135,132,121,112,137,142],
    'Timeline': [0, 0, 0, 1, 1, 1,0,0,1,1,0,0,1,1]
})

# Filter the DataFrame for RYGB vs CG and SG vs CG
study2 = dat[(~dat['Treatment'].isin(['RYGB', 'CG','SG']))]
rygb_cg = dat[(dat['Treatment'].isin(['RYGB', 'CG']))]
sg_cg = dat[(dat['Treatment'].isin(['SG', 'CG']))]

# Create Altair Chart for RYGB vs CG
chart_rygb_cg = alt.Chart(rygb_cg).mark_line().encode(
    x='Timeline:N',
    y='SBP:Q',
    color='Class:N',
    tooltip=['BMI:Q', 'SBP:Q', 'Class:N', 'Treatment:N']
).properties(
    title='RYGB vs CG'
)

# Create Altair Chart for SG vs CG
chart_sg_cg = alt.Chart(sg_cg).mark_line().encode(
    x='Timeline:N',
    y='SBP:Q',
    color='Class:N',
    tooltip=['BMI:Q', 'SBP:Q', 'Class:N', 'Treatment:N']
).properties(
    title='SG vs CG'
)

# Main plot without more than two treatment or control arms
chart_study2 = alt.Chart(study2).mark_line().encode(
    x='Timeline:N',
    y='SBP:Q',
    color='Class:N',
    tooltip=['BMI:Q', 'SBP:Q', 'Class:N', 'Treatment:N']
).properties(
    title=' Band vs COT '
)

chartf=chart_study2.facet('studynames')

# Display the charts
chart_rygb_cg | chart_sg_cg |chartf