import requests
import streamlit as st

st.title("What's For Today?")

st.subheader("Please choose your choice of cuisine below:")
cuisine = st.selectbox('Cuisine', {'无', '自助餐', '中餐', '西餐'})
if cuisine == '无':
    cuisine = None

st.subheader("Please choose the area of the restaurant below:")
area = st.selectbox('Area', {'无', '外滩', '新天地', '中山公园'})
if area == '无':
    area = None

if st.button('Show restaurants!'):
    data = None
    if cuisine and area:
        data = {'cuisine': cuisine, 'area': area}
    elif cuisine:
        data = {'cuisine': cuisine}
    elif area:
        data = {'area': area}
    st.write(data)
    if data:
        response = requests.get("https://whats-for-today-backend.herokuapp.com/get", params=data)
        if response.ok:
            st.header('Response: ' + str(response.json()))
        elif response.status_code == 400:
            st.header("Something went wrong: " + str(response.json()))
    else:
        st.write('Cuisine and/or area is required!')