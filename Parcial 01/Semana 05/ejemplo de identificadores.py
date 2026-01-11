class CalculoFigura: # CAMEL_CASE cada palabra inicia con mayuscula
    def __init__(self, nombre_figura): # SNAKE_case todas las palabras en minuscula separadas por guion bajo
        self.nombre_figura = nombre_figura

    def calculo_area(self): # SNAKE_case todas las palabras en minuscula separadas por guion bajo
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def calculo_perimetro(self): # SNAKE_case todas las palabras en minuscula separadas por guion bajo
        raise NotImplementedError("Este método debe ser implementado por las subclases")


class RetanguloCalculos(CalculoFigura): # CAMEL_CASE cada palabra inicia con mayuscula
    def __init__(self, nombre_figura, base, altura):
        super().__init__(nombre_figura)
        self.base = base
        self.altura = altura

    def calculo_area(self): # SNAKE_case todas las palabras en minuscula separadas por guion bajo
        return self.base * self.altura

    def calculo_perimetro(self):
        return 2 * (self.base + self.altura)

class CuadradoCalculos(CalculoFigura): # CAMEL_CASE cada palabra inicia con mayuscula
    def __init__(self, nombre_figura, lado):
        super().__init__(nombre_figura)
        self.lado = lado

    def calculo_area(self): # SNAKE_case todas las palabras en minuscula separadas por guion bajo
        return self.lado ** 2

    def calculo_perimetro(self):
        return 4 * self.lado

# Crear objetos de las clases y probar los métodos
rectangulo = RetanguloCalculos("Rectángulo", 5, 10)
cuadrado = CuadradoCalculos("Cuadrado", 4)

print(f"Área del {rectangulo.nombre_figura}: {rectangulo.calculo_area()}")
print(f"Perímetro del {rectangulo.nombre_figura}: {rectangulo.calculo_perimetro()}")
print(f"Área del {cuadrado.nombre_figura}: {cuadrado.calculo_area()}")
print(f"Perímetro del {cuadrado.nombre_figura}: {cuadrado.calculo_perimetro()}")

# este progrmaa define una clase base CalculoFigura con métodos para calcular el área y el perímetro. y usa camel case para los nombres de las clases y snake case para los nombres de los métodos y atributos.
