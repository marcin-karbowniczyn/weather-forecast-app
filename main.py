# DATA APP -> an app which shows Data as a visualisation.
import streamlit as st
import plotly.express as px
from backend import get_data

st.write(st.session_state)

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place:', key='place_input')

days = st.slider('Forecast Days',
                 min_value=1,
                 max_value=5,
                 help='Select the number of forcast days.',
                 key='slider')

option = st.selectbox('Select the data to view',
                      options=('Temperature', 'Sky'),
                      key='selectbox')

get_data(place, days, option)

if place:
    st.subheader(f'{option} for the next {days} days in {place}')

    dates = ['2022-25-10', '2022-26-10', '2022-27-10']
    temperatures = [10, 11, 15]
    # px.line creates a graph/plot, which we use in st.plotly_chart to display on a webpage
    figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature'})
    st.plotly_chart(figure)
