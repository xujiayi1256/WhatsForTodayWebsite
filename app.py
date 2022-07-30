import requests
import streamlit as st

st.title("What's For Today?")


cuisine_choices = [
    "全部",
    "日本菜",
    "韩国料理",
    "东南亚菜",
    "西餐",
    "烤肉",
    "本帮江浙菜",
    "川菜",
    "粤菜",
    "火锅",
    "小吃快餐",
]

area_choices = [
    "全部",
    "徐汇区",
    "静安区",
    "长宁区",
    "闵行区",
    "浦东新区",
    "黄浦区",
    "普陀区",
    "虹口区",
    "杨浦区",
    "宝山区",
    "松江区",
    "嘉定区",
    "青浦区",
    "奉贤区",
    "金山区",
    "崇明区",
]
st.subheader("Please choose your choice of cuisine below:")
cuisine = st.selectbox('Cuisine', cuisine_choices)
if cuisine == '全部':
    cuisine = None

st.subheader("Please choose the area of the restaurant below:")
area = st.selectbox('Area', area_choices)
if area == '全部':
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
    response = requests.get("https://whats-for-today-backend.herokuapp.com/get", params=data)
    if response.ok:
        for restaurant in response.json():
            st.write(restaurant)
    elif response.status_code == 400:
        st.header("Something went wrong: " + str(response.json()))
    else:
        st.header("Something went wrong...")
