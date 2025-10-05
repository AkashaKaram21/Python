""" 
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es par o impar.

"""

def main():
    numero = int(input("Introduiex un número: "))
    
    if(numero % 2 == 0):
        print("És par")
    else:
        print("És impar")

if __name__ == "__main__":
    main()