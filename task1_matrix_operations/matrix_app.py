import streamlit as st
import numpy as np
import io
import sys

# 🔁 CHANGE THIS ONLY IF YOUR FILE NAME IS DIFFERENT
import matrix_operations_tool as mot


#  PAGE CONFIG 
st.set_page_config(
    page_title="Matrix Operations Tool",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Matrix Operations Tool")
st.caption("Streamlit UI built on top of existing CLI logic")

#  MATRIX INPUT 
def matrix_input(name):
    st.subheader(f"Matrix {name}")

    rows = st.number_input(
        f"Enter number of rows for Matrix {name}",
        min_value=1,
        max_value=10,
        value=3,
        key=f"{name}_rows"
    )

    cols = st.number_input(
        f"Enter number of columns for Matrix {name}",
        min_value=1,
        max_value=10,
        value=3,
        key=f"{name}_cols"
    )

    data = []
    for i in range(rows):
        data.append(
            st.text_input(
                f"Row {i+1} (space separated)",
                key=f"{name}_row_{i}"
            )
        )

    # Validation
    if any(d.strip() == "" for d in data):
        return None

    try:
        matrix = np.array([list(map(float, r.split())) for r in data])
        if matrix.shape == (rows, cols):
            return matrix
    except:
        return None

    return None


#  GET MATRICES 
A = matrix_input("A")
B = matrix_input("B")

if A is None or B is None:
    st.info("⬆️ Please enter valid values for both matrices to continue")
    st.stop()

st.success("✅ Matrices loaded successfully")

st.write("### Matrix A")
st.write(A)

st.write("### Matrix B")
st.write(B)


#  MENU 
st.divider()
st.subheader("Matrix Operations Menu")

choice = st.selectbox(
    "Select Operation",
    [
        "Matrix Analysis",
        "Addition",
        "Subtraction",
        "Multiplication",
        "Transpose",
        "Determinant"
    ]
)

# Matrix selection (ONLY when required)
selected_matrix = None
if choice in ["Matrix Analysis", "Transpose", "Determinant"]:
    selected_matrix = st.radio(
        "Choose Matrix",
        ["A", "B"],
        horizontal=True
    )

#  EXECUTE 
execute = st.button("Execute")

if execute:

    # Capture printed output from locked CLI code
    buffer = io.StringIO()
    sys.stdout = buffer

    try:
        if choice == "Matrix Analysis":
            if selected_matrix == "A":
                mot.analyze_matrix(A, "A")
            else:
                mot.analyze_matrix(B, "B")

        elif choice == "Addition":
            if A.shape == B.shape:
                mot.print_matrix(A + B, "A + B")
            else:
                print("Addition not possible (different dimensions).")

        elif choice == "Subtraction":
            if A.shape == B.shape:
                mot.print_matrix(A - B, "A - B")
            else:
                print("Subtraction not possible (different dimensions).")

        elif choice == "Multiplication":
            if A.shape[1] == B.shape[0]:
                mot.print_matrix(A @ B, "A × B")
            else:
                print("Multiplication not possible (columns of A ≠ rows of B).")

        elif choice == "Transpose":
            if selected_matrix == "A":
                mot.print_matrix(A.T, "Transpose of Matrix A")
            else:
                mot.print_matrix(B.T, "Transpose of Matrix B")

        elif choice == "Determinant":
            if selected_matrix == "A":
                mot.determinant_matrix(A, "A")
            else:
                mot.determinant_matrix(B, "B")

    finally:
        sys.stdout = sys.__stdout__

    # Display output exactly like CLI
    st.code(buffer.getvalue())
