""" 
Escribir un programa que almacene la cadena de caracteres contraseña
en una variable, pregunte al usuario por la contraseña e imprima 
por pantalla si la contraseña introducida por el usuario coincide 
con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

"""
def main():
    contrasenay_usuari= input("Introdueix una contrasenay: ")
    
    contrasenay_guardada = "a123"
    
    if(contrasenay_guardada == contrasenay_usuari.lower()):
        print("La contrasenya concedeix")
    else:
        print("La contrasenya es incorrecte")
    
if __name__ == "__main__":
    main()
    