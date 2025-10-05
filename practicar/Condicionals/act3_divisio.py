""" 
Escribir un programa que pida al usuario dos números y muestre 
por pantalla su división. Si el divisor es cero el programa debe 
mostrar un error.

"""
def main():
    num1 = int(input("Introdueix un número: "))
    num2 = int(input("Introdueix altre número: "))
    
    if(num1 == 0 or num2 == 0):
        print("No es pot dividir entre 0")
    else:
        print(num1/num2)
    
if __name__ == "__main__":
    main()