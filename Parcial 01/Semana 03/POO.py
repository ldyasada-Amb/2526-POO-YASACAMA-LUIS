
class calculo_temperatura:
    def __init__(self, dias):
        self.dias = dias
        self.temperaturas = []  # lista donde se almacenan las temperaturas por dia

    def ingreso_temperatura(self): 
        while True:
            dia = input("Ingrese el día: ")
            temp = int(input("Ingrese la temperatura: "))
            temperaturasemanal = {"dia": dia, "temperatura": temp}
            self.temperaturas.append(temperaturasemanal)

            opcion = input("¿Desea ingresar otra temperatura? si/no: ")
            if opcion.lower() == "no":
                break

    def calcular_promedio(self):
        suma = 0
        for registro in self.temperaturas:   # recorremos la lista  ver linea 5
            suma += registro["temperatura"]  # accedemos al valor de la clave
        promedio = suma / len(self.temperaturas)
        print(f"El promedio semanal de las temperaturas ingresadas es: {promedio}")


# Menú principal
calculo = calculo_temperatura(dias=7)

while True:
    print("\nWelcome to the Temperature Average Calculator")
    print("Elija una opción")
    print("1. Ingresar temperaturas")
    print("2. Calcular promedio")
    print("3. Salir")
    opcion = input("Ingrese una opción (1-3): ")

    if opcion == "1":
        calculo.ingreso_temperatura()
    elif opcion == "2":
        calculo.calcular_promedio()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
