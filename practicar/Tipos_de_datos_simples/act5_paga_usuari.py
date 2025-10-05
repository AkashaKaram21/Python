"""
Escribir un programa que pregunte al usuario por el número de horas 
trabajadas y el coste por hora. Después debe mostrar por pantalla 
la paga que le corresponde.

"""

def main():
    hores = int(input("Quantes hores treballes? "))
    paga = float(input("I el cost per hora? "))

    print(f"La paga que tens és {hores * paga}")
    
if __name__ == "__main__":
    main()