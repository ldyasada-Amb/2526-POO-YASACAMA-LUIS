print("Ejemplo de Constructor y Destructor en Python")

class Persona:
    def __init__(self,nombre,cedula): # constructor
        self.nombre = nombre
        self.cedula = cedula
        print(f"Constructor: Persona {self.nombre} con cédula {self.cedula} ha sido creada.")

    def __del__(self): #destructor sive para liberar recursos
        print(f"Destructor: Persona {self.nombre} con cédula {self.cedula} ha sido eliminada.")
# Crear una instancia de la clase Persona
persona1 = Persona("Juan Perez", "123456789")
# ESTE ES UN EJEMPLO SIMPLIFICADO, EN LA VIDA REAL NO ES RECOMENDABLE USAR EL DESTRUCTOR PARA LIBERAR RECURSOS MANUALMENTE


print("\nEjemplo de Constructor y Destructor con manejo de archivos en Python number 2")

class ArchivoPrincipal:
    def __init__(self,nombre_archivo): # constructor sirve para inicializar recursos
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, 'w')
        print(f"Constructor: Archivo {self.nombre_archivo} ha sido abierto para escritura.")

    def escribir(self, palabras):
        self.archivo.write(palabras + '\n')
        print(f"Escribiendo en el archivo: {palabras}")

    def __del__(self): # destructor sirve para liberar recursos
        self.archivo.close()
        print(f"Destructor: Archivo {self.nombre_archivo} ha sido cerrado.")

# Crear una instancia de la clase ArchivoPrincipal
archivo1 = ArchivoPrincipal("ejemplo.txt") #
archivo1.escribir("Hola, este es un ejemplo de uso de constructor y destructor en Python.")
archivo1.escribir("El archivo se cerrará automáticamente cuando el objeto sea destruido.")
print("Ejemplo de constructor y destructor con manejo de archivos en python finalizado.")


