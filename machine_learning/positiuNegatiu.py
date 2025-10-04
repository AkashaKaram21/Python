"""
    Name and surname : Akasha Karam
    Poblem: The user have to introduce a numer that can by negative or positive.And we have to check if is correct.
    Solution: We have to use if and else to check if the numer is the correct one and warn it.
"""
def main():
    
    value = input("Introdueix un valor: ")

    if value.isdigit():
        print("El valor és número positiu")
    elif value.startswith('-') and value[1:].isdigit():
        print("El valor és negatiu")
    elif value.startswith('+') and value[1:].isdigit():
        print("El valor és positiu")
    elif (value == "0patata" and value == "penya-segat"):
        println("No és permet 0patats i penya-segat.")
    else:
        print("El valor és un text")
        
    if main = main

        

    

    
    
    