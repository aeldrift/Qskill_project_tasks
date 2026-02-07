import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# ----------------------------------
# Custom CSS (UI ONLY)
# ----------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #f8fafc, #eef2ff);
    }

    h1 {
        color: #1f2937;
        font-weight: 800;
    }

    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #e5e7eb;
    }

    .stButton > button {
        background-color: #4f46e5;
        color: white;
        border-radius: 8px;
        padding: 10px 16px;
        font-weight: 600;
        border: none;
    }

    .stButton > button:hover {
        background-color: #4338ca;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------------
# App Title
# ----------------------------------
st.markdown(
    """
    <div style="text-align:center; padding: 20px;">
        <h1>🏠 House Price Prediction App</h1>
        <p style="font-size:18px; color:#4b5563;">
            Predict house prices using a basic Machine Learning model
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------------
# Load Dataset
# ----------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/Housing.csv")

data = load_data()

# ----------------------------------
# Train Model
# ----------------------------------
X = data[["area", "bedrooms", "bathrooms", "stories", "parking"]]
y = data["price"]

model = LinearRegression()
model.fit(X, y)

# ----------------------------------
# Sidebar Inputs
# ----------------------------------
st.sidebar.header("Enter House Details")

area = st.sidebar.number_input(
    "Area (sq ft)",
    min_value=100,
    max_value=20000,
    value=3000,
    step=100
)

bedrooms = st.sidebar.slider("Bedrooms", 1, 6, 3)
bathrooms = st.sidebar.slider("Bathrooms", 1, 4, 2)
stories = st.sidebar.slider("Stories", 1, 4, 2)
parking = st.sidebar.slider("Parking Spaces", 0, 3, 1)

# ----------------------------------
# Prediction
# ----------------------------------
if st.sidebar.button("Predict Price"):
    input_data = pd.DataFrame(
        [[area, bedrooms, bathrooms, stories, parking]],
        columns=["area", "bedrooms", "bathrooms", "stories", "parking"]
    )

    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
        <div style="
            background-color:#ecfdf5;
            padding:20px;
            border-radius:12px;
            border-left:6px solid #10b981;
            font-size:22px;
            font-weight:700;
            color:#065f46;
            max-width:600px;
            margin:auto;
        ">
            🏷️ Estimated House Price: ₹ {prediction:,.0f}
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------------------
# Dataset Preview
# ----------------------------------
st.markdown("<hr style='border:1px solid #e5e7eb;'>", unsafe_allow_html=True)

st.markdown(
    """
    <h2 style="margin-top:20px;">📊 Dataset Preview</h2>
    <p style="color:#6b7280;">First 5 rows of the dataset</p>
    """,
    unsafe_allow_html=True
)

st.dataframe(data.head(), use_container_width=True)

# ----------------------------------
# Footer
# ----------------------------------
st.markdown(
    """
    <div style="text-align:center; color:#6b7280; padding:20px;">
        Built using Streamlit, Pandas & Machine Learning ❤️ 
    </div>
    """,
    unsafe_allow_html=True
)
