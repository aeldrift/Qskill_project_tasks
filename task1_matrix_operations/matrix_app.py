import streamlit as st
import numpy as np
import io
import sys

#  IMPORT YOUR LOCKED FILE (name must match)
import matrix_operations_tool as mot


st.set_page_config(
    page_title="Matrix Operations Tool",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Matrix Operations Tool")
st.caption("Streamlit UI built on top of locked CLI logic")

# MATRIX INPUT 
def matrix_input(name):
    st.subheader(f"Matrix {name}")

    rows = st.number_input(
        f"Enter number of rows for Matrix {name}",
        min_value=1, max_value=10, value=3, key=f"{name}_r"
    )

    cols = st.number_input(
        f"Enter number of columns for Matrix {name}",
        min_value=1, max_value=10, value=3, key=f"{name}_c"
    )

    data = []
    for i in range(rows):
        data.append(
            st.text_input(
                f"Row {i+1} (space separated)",
                key=f"{name}_row_{i}"
            )
        )