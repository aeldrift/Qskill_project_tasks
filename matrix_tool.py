import numpy as np

def get_matrix(name):
    """
    Takes matrix input from user with proper validation
    and returns it as a NumPy array.
    """

    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))

    print(f"Enter values for Matrix {name} row-wise (space separated):")

    matrix = []

    for i in range(rows):
        while True:
            row = list(map(float, input(f"Row {i+1}: ").split()))

            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"❌ Error: Please enter exactly {cols} values.")

    return np.array(matrix)


# Taking matrix input
A = get_matrix("A")
B = get_matrix("B")

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

while True:
    print("\n--- Matrix Operations Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Transpose")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if A.shape == B.shape:
            print("\nResult of Addition:")
            print(A + B)
        else:
            print("Addition not possible (different dimensions)")

    elif choice == "2":
        if A.shape == B.shape:
            print("\nResult of Subtraction:")
            print(A - B)
        else:
            print("Subtraction not possible (different dimensions)")

    elif choice == "3":
        matrix_choice = input("Transpose which matrix? (A/B): ").upper()

        if matrix_choice == "A":
            print("\nTranspose of Matrix A:")
            print(A.T)

        elif matrix_choice == "B":
            print("\nTranspose of Matrix B:")
            print(B.T)

        else:
            print("Invalid matrix choice. Please enter A or B.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
