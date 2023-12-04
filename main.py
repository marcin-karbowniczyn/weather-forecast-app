# DATA APP -> an app which shows Data as a visualisation.
import streamlit as st

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

if place:
    st.subheader(f'{option} for the next {days} days in {place}')
