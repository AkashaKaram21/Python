""" 
Escribir un programa que pregunte por consola el precio de un 
producto en euros con dos decimales y muestre por pantalla 
el número de euros y el número de céntimos del precio introducido.
"""
def main():
    producto = input("Introduiex el preu del producte: ")
    
    euro = producto[:producto.find('.')]
    decimas = producto[producto.find('.')+1:]
    
    print(f"El número de euros és {euro} i el número de centims és {decimas}")

if __name__ == "__main__":
    main()