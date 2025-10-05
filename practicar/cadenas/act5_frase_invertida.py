""" 
Escribir un programa que pida al usuario que introduzca una frase
en la consola y muestre por pantalla la frase invertida.

"""
def main():
    frase = input("Introduiex una frase: ")
    
    print("La frase invertida és " + frase[::-1])
    
if __name__ == "__main__":
    main()