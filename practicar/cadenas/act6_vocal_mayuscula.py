""" 
Escribir un programa que pida al usuario que introduzca una frase
en la consola y una vocal, y después muestre por pantalla la misma 
frase pero con la vocal introducida en mayúscula.

"""
def main():
    frase = input("Introduiex una frase: ")
    vocal = input("Introduiex una vocal: ")
    
    print(frase.replace(vocal,vocal.upper()))

if __name__ == "__main__":
    main()
    
    