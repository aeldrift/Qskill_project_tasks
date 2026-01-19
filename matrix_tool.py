import numpy as np

def get_matrix(name):
    """
    Takes matrix input from user with proper validation
    and returns it as a NumPy array.
    """
    # Input rows and columns
    while True:
        try:
            rows = int(input(f"Enter number of rows for Matrix {name}: "))
            cols = int(input(f"Enter number of columns for Matrix {name}: "))

            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive numbers.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

    # Input matrix values
    print(f"Enter values for Matrix {name} row-wise (space separated):")
    matrix = []

    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i+1}: ").split()))
                if len(row) == cols:
                    matrix.append(row)
                    break
                else:
                    print(f"Please enter exactly {cols} values.")
            except ValueError:
                print("Invalid input. Please enter numeric values only.")

    return np.array(matrix)


def analyze_matrix(M, name):
    rows, cols = M.shape
    print(f"\n--- Analysis of Matrix {name} ---")

    # Shape type
    if rows == cols:
        print("• Square Matrix")
    else:
        print("• Rectangular Matrix")

    if rows == 1:
        print("• Row Matrix")
    if cols == 1:
        print("• Column Matrix")

    # Zero matrix
    if np.all(M == 0):
        print("• Zero Matrix")

    # Square matrix checks
    if rows == cols:
        if np.allclose(M, np.diag(np.diag(M))):
            print("• Diagonal Matrix")

            if np.all(M.diagonal() == M.diagonal()[0]):
                print("• Scalar Matrix")

        if np.allclose(M, np.eye(rows)):
            print("• Identity Matrix")

        if np.allclose(M, M.T):
            print("• Symmetric Matrix")

        if np.allclose(M, -M.T):
            print("• Skew-Symmetric Matrix")


# Taking matrix input
A = get_matrix("A")
B = get_matrix("B")

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Menu-driven operations
while True:
    print("\n--- Matrix Operations Menu ---")
    print("1. Matrix Analysis")
    print("2. Addition")
    print("3. Subtraction")
    print("4. Transpose")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        matrix_choice = input("Analyze which matrix? (A/B): ").upper()
        if matrix_choice == "A":
            analyze_matrix(A, "A")
        elif matrix_choice == "B":
            analyze_matrix(B, "B")
        else:
            print("Invalid matrix choice.")

    elif choice == "2":
        if A.shape == B.shape:
            print("\nResult of Addition:")
            print(A + B)
        else:
            print("Addition not possible (different dimensions).")

    elif choice == "3":
        if A.shape == B.shape:
            print("\nResult of Subtraction:")
            print(A - B)
        else:
            print("Subtraction not possible (different dimensions).")

    elif choice == "4":
        matrix_choice = input("Transpose which matrix? (A/B): ").upper()
        if matrix_choice == "A":
            print("\nTranspose of Matrix A:")
            print(A.T)
        elif matrix_choice == "B":
            print("\nTranspose of Matrix B:")
            print(B.T)
        else:
            print("Invalid matrix choice.")

    elif choice == "5":
        print("Program Exit.")
        break

    else:
        print("Invalid choice. Try again.")
        continue

    cont = input("\nDo you want to perform another operation? (Y/N): ").upper()
    if cont != "Y":
        print("Thank you for using the Matrix Operations Tool.")
        break
