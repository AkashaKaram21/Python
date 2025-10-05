"""
Escribir un programa que pregunte el nombre completo del usuario en
la consola y después muestre por pantalla el nombre completo del
usuario tres veces, una con todas las letras minúsculas, 
otra con todas las letras mayúsculas y otra solo con la primera
letra del nombre y de los apellidos en mayúscula. El usuario 
puede introducir su nombre combinando mayúsculas 
y minúsculas como quiera.
"""
def main():
    # Preguntem el nom complet de l'usuari
    nom = input("Nom: ")
    cognom = input("Cognom: ")

    # Mostrem el nom complet en minúscules
    print((nom + " " + cognom).lower())

    # Mostrem el nom complet en majúscules
    print((nom + " " + cognom).upper())

    # Mostrem el nom complet amb la primera lletra en majúscula
    print((nom + " " + cognom).title())

if __name__ == "__main__":
    main()

    
    