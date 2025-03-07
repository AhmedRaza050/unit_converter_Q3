# import streamlit as st
# from streamlit_option_menu import option_menu  # type: ignore


# #Page Configuration
# st.set_page_config(page_title="Unit Converter", layout="centered")

# # Custom Styling
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #F8F9FA;
#         color: #333;
#         font-family: 'Poppins', sans-serif;
#     }
#     .stApp {
#         background: #FFFFFF;
#         padding: 30px;
#         border-radius: 12px;
#         box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
#     }
#     h1 {
#         text-align: center;
#         font-size: 36px;
#         color: #007BFF;
#     }
#     .stButton>button {
#         background: linear-gradient(135deg, #007BFF, #00BFFF);
#         color: white;
#         font-size: 18px;
#         padding: 12px 24px;
#         border-radius: 10px;
#         border: none;
#         transition: 0.3s;
#     }
#     .stButton>button:hover {
#         transform: scale(1.1);
#         background: linear-gradient(135deg, #FF6F61, #D72638);
#     }
#     .result-box {
#         text-align: center;
#         background: #E3F2FD;
#         padding: 20px;
#         margin-top: 20px;
#         border-radius: 10px;
#         font-size: 22px;
#         font-weight: bold;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Title
# st.markdown("<h1>Unit Converter</h1>", unsafe_allow_html=True)

# # Sidebar Navigation
# selected = option_menu(
#     menu_title=None,
#     options=["Length", "Weight", "Temperature"],
#     icons=["rulers", "scale", "thermometer"],
#     menu_icon="cast",
#     default_index=0,
#     orientation="horizontal"
# )

# value = st.number_input("Enter Value", min_value=0.0, step=0.1)
# col1, col2 = st.columns(2)

# # Unit Conversion Dictionaries
# length_units = {
#     'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
#     'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
# }

# weight_units = {
#     'Kilogram': 1, 'Gram': 1000, 'Milligrams': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
# }

# # Conversion Functions
# def length_convertor(value, from_unit, to_unit):
#     return (value / length_units[from_unit]) * length_units[to_unit]

# def weight_convertor(value, from_unit, to_unit):
#     return (value / weight_units[from_unit]) * weight_units[to_unit]

# def temp_convertor(value, from_unit, to_unit):
#     if from_unit == "Celsius":
#         return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
#     if from_unit == "Fahrenheit":
#         return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
#     if from_unit == "Kelvin":
#         return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
#     return value

# # Unit Selection
# if selected == "Length":
#     with col1:
#         from_unit = st.selectbox("From", list(length_units.keys()))
#     with col2:
#         to_unit = st.selectbox("To", list(length_units.keys()))
    
# elif selected == "Weight":
#     with col1:
#         from_unit = st.selectbox("From", list(weight_units.keys()))
#     with col2:
#         to_unit = st.selectbox("To", list(weight_units.keys()))

# elif selected == "Temperature":
#     with col1:
#         from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
#     with col2:
#         to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# # Conversion Button
# if st.button("Convert"):
#     if selected == "Length":
#         result = length_convertor(value, from_unit, to_unit)
#     elif selected == "Weight":
#         result = weight_convertor(value, from_unit, to_unit)
#     elif selected == "Temperature":
#         result = temp_convertor(value, from_unit, to_unit)
    
#     st.markdown(f"<div class='result-box'>{value:.2f} {from_unit} = {result:.2f} {to_unit}</div>", unsafe_allow_html=True)


import streamlit as st

# Page Configuration
st.set_page_config(page_title="Unit Converter", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
    body {
        background-color: #F0F8FF;
        color: #333;
        font-family: 'Poppins', sans-serif;
    }
    .stApp {
        background: #FFFFFF;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: #007BFF;
    }
    .stButton>button {
        background: linear-gradient(135deg, #007BFF, #00BFFF);
        color: white;
        font-size: 18px;
        padding: 12px 24px;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        background: linear-gradient(135deg, #FF6F61, #D72638);
    }
    .result-box {
        text-align: center;
        background: #E3F2FD;
        padding: 20px;
        margin-top: 20px;
        border-radius: 10px;
        font-size: 22px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1>Unit Converter</h1>", unsafe_allow_html=True)

# Sidebar Navigation
selected = st.selectbox("Choose a conversion type:", ["Length", "Weight", "Temperature"])

value = st.number_input("Enter Value", min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

# Unit dictionaries
length_units = {
    'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
    'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
}

weight_units = {
    'Kilogram': 1, 'Gram': 1000, 'Milligrams': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
}

# Conversion Functions
def length_convertor(value, from_unit, to_unit):
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    return value

# Unit Selection
if selected == "Length":
    with col1:
        from_unit = st.selectbox("From", list(length_units.keys()))
    with col2:
        to_unit = st.selectbox("To", list(length_units.keys()))

elif selected == "Weight":
    with col1:
        from_unit = st.selectbox("From", list(weight_units.keys()))
    with col2:
        to_unit = st.selectbox("To", list(weight_units.keys()))

elif selected == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Button
if st.button("Convert"):
    if selected == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif selected == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif selected == "Temperature":
        result = temp_convertor(value, from_unit, to_unit)
    
    st.markdown(f"<div class='result-box'>{value:.2f} {from_unit} = {result:.2f} {to_unit}</div>", unsafe_allow_html=True)
