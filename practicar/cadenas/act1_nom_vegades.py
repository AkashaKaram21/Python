"""
Escribir un programa que pregunte el nombre del usuario en la consola y
un número entero e imprima por pantalla en líneas distintas el nombre del
usuario tantas veces como el número introducido.
"""

def main():
    nom = input("Posa el teu nom:")
    numero = int(input("Posa un número enter:"))
    
    resultat = nom * numero
    
    print(f"El nom és {nom} i és multiplica per {numero} el resultat és {resultat}")

if __name__ == "__main__":
    main()