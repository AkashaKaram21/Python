"""
   Name:Akasha Karam 

   Problem: We have a String and we have to find the letter of the dni by dividing in 23.

   Soltution: Decalare a int with 8 digits beacuase dni have it also. After declare another int and dividit with 23 and with the residue find the postion of dni using char.
"""
def main():
    
    String dni = "TRWAGMYFPDXBNJZSQVHLCKE" 

    int digit = 12345678
    
    int result = digit / 23

    char letter = dni.charAt(result)

    
