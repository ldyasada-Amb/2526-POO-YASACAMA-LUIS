class DispositivoElectico:
      def __init__(self,marca,precio):
          self.__marca=marca
          self.__precio=precio

      def encender_dispositivo(self):
            return f"El dispositivo {self.__marca} está encendido."

      def apagar_dispositivo(self):
            return f"El dispositivo {self.__marca} está apagado."

class LavadoraRopa(DispositivoElectico):
      def __init__(self,marca,precio,carga):
            super().__init__(marca,precio)
            self.__carga=carga

      def encender_dispositivo(self):
            return f"La lavadora {self._DispositivoElectico__marca} está encendida."

      def apagar_dispositivo(self):
            return f"La lavadora {self._DispositivoElectico__marca} está apagada."

class computadoraPortatil(DispositivoElectico):
      def __init__(self,marca,precio,tamano_pantalla):
            super().__init__(marca,precio)
            self.__tamano_pantalla=tamano_pantalla

      def encender_dispositivo(self):
            return f"La computadora portátil {self._DispositivoElectico__marca} está encendida."

      def apagar_dispositivo(self):
            return f"La computadora portátil {self._DispositivoElectico__marca} está apagada."

# Crear objetos de las clases y probar los métodos
lavadora = LavadoraRopa("LG", 500, 10)
computadora = computadoraPortatil("Dell", 800, 15.6)
print(lavadora.encender_dispositivo())
print(lavadora.apagar_dispositivo())
print(computadora.encender_dispositivo())
print(computadora.apagar_dispositivo())
# Este programa define una clase base DispositivoElectrico con métodos para encender y apagar el dispositivo. Luego, se crean dos clases derivadas, LavadoraRopa y computadoraPortatil,
# que heredan de DispositivoElectrico y sobrescriben los métodos para proporcionar mensajes específicos para cada tipo de dispositivo.