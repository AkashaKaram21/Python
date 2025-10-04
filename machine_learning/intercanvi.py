"""
Name and surname: Akasha Karam
In this activity, we have to declare two variables, exchange their values, 
and then sum them.
"""

# The user must enter two integer values
def main():
    num1 = int(input("Posa el primer valor de tipus int: "))
    num2 = int(input("Posa el segon valor de tipus int: "))

    # Show the values entered
    print("Valors introduïts:", num1, num2)

    # Exchange the values with each other
    num1, num2 = num2, num1
    print("Després d'intercanviar-los:", num1, num2)

    # Sum them
    sum_val = num1 + num2

    # Show the result
    print(f"La suma de {num1} i {num2} és {sum_val}")

# Run the main function
if __name__ == "__main__":
    main()
