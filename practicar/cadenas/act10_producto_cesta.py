""" 
Escribir un programa que pregunte por consola por los productos 
de una cesta de la compra, separados por comas, y muestre por pantalla 
cada uno de los productos en una línea distinta.

"""
def main():
    cesta = input("Intoduiex el nom del productes separat per coma: ")
    
    #cambiamos el , por espacio 
    print(cesta.replace(',', '\n'))
    
if __name__ == "__main__":
    main()