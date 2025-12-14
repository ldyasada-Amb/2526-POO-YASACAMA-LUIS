# Progamacion Tradicional en Python

print("Calculo del promedio semamal de temperaturas")
listas_temperaturas = []
def ingreso_temperatura():
    while True:
        temperatura = int(input("Ingrese una temperatura: "))
        listas_temperaturas.append(temperatura)
        opcion = input("Desea ingresar otra temperatura? (s/n): ")
        if opcion.lower() == "n":
            break
    return  listas_temperaturas

def calcular_promedio(listas_temperaturas):
    suma = 0
    for i in listas_temperaturas:
        suma = suma + i

    promedio = suma / len(listas_temperaturas)
    print(f"El promedio semanal de las temperaturas ingresadas es: {promedio}")



while True: # Menu principal
    print("Welcome to the Temperature Average Calculator")
    print("Elija una opcion")
    print("1. Ingresar temperaturas")
    print("2 calcular promedio")
    print("3. Salir")
    opcion = input("Ingrese una opcion (1-3): ")
    if opcion == "1":
        ingreso_temperatura() # Llamada a la funcion de ingreso de temperaturas
    elif opcion == "2":
        calcular_promedio(listas_temperaturas) # Llamada a la funcion de calculo de promedio
    elif opcion == "3":
        print("Salir")
        break







