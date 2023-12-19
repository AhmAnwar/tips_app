# import libraries
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns

# import data set
df = sns.load_dataset('tips')

# app
st.set_page_config(page_title='Tip Dashboard', layout='wide', menu_items=None, initial_sidebar_state='auto')
# sidebar
st.sidebar.header('Tips Dashboard')

st.sidebar.write('')
st.sidebar.subheader('Filter:')
categorical_filter = st.sidebar.selectbox(label='Categorical Filter', options=['sex', 'smoker', 'day', 'time'])
numerical_filter = st.sidebar.selectbox(label='Numerical Filter', options=['tip', 'total_bill'])

st.sidebar.write('')
st.sidebar.markdown('Made by [Ahmed Anwar](https://www.linkedin.com/in/ahmed-anwar-781235202)')

# body
# row 1
c1, c2, c3, c4 = st.columns(4)
c1.metric(label='Max. Total Bill', value=df['total_bill'].max())
c2.metric(label='Max. Tip', value=df['tip'].max())
c3.metric(label='Min. Total Bill', value=df['total_bill'].min())
c4.metric(label='Min. Tip', value=df['tip'].min())

# row 2
fig = px.scatter(data_frame=df,
                 x='total_bill',
                 y='tip',
                 color=categorical_filter,
                 size=numerical_filter,
                 title='Relation Between Total Bill & Tips')

st.plotly_chart(fig, use_container_width=True)

# row 3
c5, c6, c7 = st.columns([4, 3, 3])

with c5:
    fig = px.bar(data_frame=df,
                 x=categorical_filter,
                 y=numerical_filter,
                 color=categorical_filter,
                 title=str(numerical_filter) + ' by sex')
    st.plotly_chart(fig, use_container_width=True)

with c6:
    fig = px.pie(data_frame=df,
                 names=categorical_filter,
                 values='tip',
                 color=categorical_filter,
                 title='tip percentage')
    st.plotly_chart(fig, use_container_width=True)

with c7:
    fig = px.pie(data_frame=df,
                 names=categorical_filter,
                 values='total_bill',
                 hole=0.3,
                 color=categorical_filter,
                 title='total bill percentage')
    st.plotly_chart(fig, use_container_width=True)