""" 
Escribir un programa que pregunte al usuario la fecha 
de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
el día, el mes y el año. Adaptar el programa anterior para que 
también funcione cuando el día o el mes se introduzcan 
con un solo carácter.

"""
def main():
    fecha = input("Introduiex el teu data de naixament en aquest format dd/mm/aaaa: ")
    #agafa el dos valor de abans / que serian el de dia 
    dia = fecha[:fecha.find('/')]
    #agafa tot els valor despres de / y per això + 1 que seria mm/aaaa
    mesaño = fecha[fecha.find('/')+1:]
    #agafa el 2 valor abans de / que serian el mes mm
    mes = mesaño[:mesaño.find('/')]
    #agafa el 2 valor despres de / que seria aaaa
    año = mesaño[mesaño.find('/')+1:]
    print('Día', dia)
    print('Mes', mes)
    print('Año', año)
    
if __name__ =="__main__":
    main()