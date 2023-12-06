# DATA APP -> an app which shows Data as a visualisation.
import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(page_title='Weather Forecast App', layout='wide')

empty_col_left, col_content, empty_col_right = st.columns(3)
with col_content:
    # 1. Add title, text input, slider, selectbox and subheader
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

st.divider()

if place:
    try:
        # 2. Get the data after place is provided by the user
        data = get_data(place, days)

        # 2a. Display chart if temperatures
        if option == 'Temperature':
            # Create subheader fot temperatures
            st.subheader(f'{option} for the next {days} days in {place}')

            # Extract temperatures and dates
            temperatures = [el['main']['temp'] for el in data]
            dates = [el['dt_txt'] for el in data]

            # px.line creates a graph/plot, which we use in st.plotly_chart to display on a webpage
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature'})
            st.plotly_chart(figure, use_container_width=True)

        # 2b. Display chart if sky
        elif option == 'Sky':
            # Create centered layout for sky icons
            sky_col_left, sky_content, sky_col_right = st.columns(3)
            with sky_content:
                # Create subheader fot sky
                st.subheader(f'{option} for the next {days} days in {place}')

                # Extract sky conditions and dates
                sky_conditions = [el['weather'][0]['main'] for el in data]
                dates = [el['dt_txt'] for el in data]
                images = [f"images/{el.lower()}.png" for el in sky_conditions]
                st.image(images, width=115, caption=dates)

    except KeyError:
        st.error(f"Can't find a place named {place}. Please try again.")
