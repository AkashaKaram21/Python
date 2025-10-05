"""
Escribir un programa que pregunte al usuario su edad y 
muestre por pantalla si es mayor de edad o no.
"""
def main():
    edat = int(input("Introdueix la teva edat: "))
    
    if edat >= 18:
        print("Ets major d'edat")
    else:
        print("Ets menor d'edat")


if __name__ == "__main__":
    main()
