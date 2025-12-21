class Deportista:
    def __init__(self,nombre,edad): #constructor de la clase Deportista
        self.nombre=nombre #atributos
        self.edad=edad

    def entrenar(self): #metodos
        return f"{self.nombre} está entrenando"

    def hidratarse(self):
        return f"{self.nombre} se está hidratando"

class Nadador(Deportista): #herencia de la clase Deportista
    def __init__(self,nombre,edad,estilo): #constructor de la clase Nadador
        super().__init__(nombre,edad) #llamada al constructor de la clase base
        self.estilo=estilo

    def entrenar(self): # metodo sobreescrito
        return f"{self.nombre} está nadando estilo {self.estilo}"

    def hidratarse(self):
        return f"{self.nombre} se está hidratando con agua"

class Futbolista(Deportista): #herencia de la clase Deportista
    def __init__(self,nombre,edad,posicion): #
        super().__init__(nombre,edad)
        self.posicion=posicion

    def entrenar(self): # metodo sobreescrito polimorfismo
        return f"{self.nombre} está entrenando en la posición de {self.posicion}"

    def hidratarse(self): # poli
        return f"{self.nombre} se está hidratando con bebida isotónica"

#crear objetos de las clases y probar los métodos
nadador1=Nadador("Carlos",20,"crol")
futbolista1=Futbolista("Luis",25,"delantero")
#probar los métodos
print(nadador1.entrenar())
print(nadador1.hidratarse())
print(futbolista1.entrenar())
print(futbolista1.hidratarse())

#Explicación:
#En este ejemplo, hemos definido una clase base Deportista con atributos y métodos comunes.
#Luego, hemos creado dos clases derivadas, Nadador y Futbolista, que heredan de Deportista.
#Cada clase derivada tiene su propio constructor y métodos que sobrescriben los métodos de la clase base.
#Esto demuestra los conceptos de herencia y polimorfismo en la programación orientada a objetos.
