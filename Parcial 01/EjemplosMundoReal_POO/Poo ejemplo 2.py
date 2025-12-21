class tienda:
    def __init__(self, nombre): #constructor de la clase tienda
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"Productos en la tienda {self.nombre}:")
        for producto in self.productos:
            print(f"- {producto.nombre}: ${producto.precio}")

class producto: #constructor de la clase producto
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class cliente: #constructor de la clase cliente
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_al_carrito(self, producto): #agregar producto al carrito
        self.carrito.append(producto)

    def mostrar_carrito(self):
        print(f"Carrito de {self.nombre}:")
        for producto in self.carrito:
            print(f"- {producto.nombre}: ${producto.precio}")

class empleado:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto

    def atender_cliente(self, cliente):
        return f"{self.nombre} está atendiendo a {cliente.nombre}"

# Ejemplo de uso
# Crear una tienda, agregar productos, crear un cliente y un empleado
tienda1 = tienda("La Esquina")
producto1 = producto("Manzana", 0.5)
producto2 = producto("Pan", 1.0)
tienda1.agregar_producto(producto1)
tienda1.agregar_producto(producto2)
tienda1.mostrar_productos()
cliente1 = cliente("Ana")
cliente1.agregar_al_carrito(producto1)
cliente1.agregar_al_carrito(producto2)
cliente1.mostrar_carrito()
empleado1 = empleado("Carlos", "Cajero")
print(empleado1.atender_cliente(cliente1))

# Explicación:
# En este ejemplo, hemos definido cuatro clases: tienda, producto, cliente y empleado.
# Cada clase tiene su propio constructor (__init__) y métodos para realizar acciones específicas.
# La clase tienda puede agregar y mostrar productos, la clase cliente puede agregar productos a su carrito y mostrarlo,
# y la clase empleado puede atender a un cliente. Este ejemplo ilustra cómo se pueden modelar entidades del mundo real utilizando la programación orientada a objetos.

