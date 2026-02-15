# Sistema de gestión de inventario para una tienda de artículos electrónicos
class Producto:
    def __init__(self, ID, nombre, precio, cantidad,):
        self.ID = ID
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        

class Inventario (Producto):
    def __init__(self, ID, nombre, precio, cantidad):
        self.lista_productos = []

    def añadir_producto(self, producto):
        while True:
            ID = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            producto_ingresado = {"ID": ID, "nombre": nombre, "precio": precio, "cantidad": cantidad}    
            self.lista_productos.append(producto_ingresado)
            opcion = input("¿Desea ingresar otro producto? si/no: ")
            if opcion.lower() == "no":
                break
    
    def eliminar_producto_por_ID(self, ID):
        for producto in self.lista_productos:
            if producto["ID"] == ID:
                self.lista_productos.remove(producto)
                print(f"Producto con ID {ID} eliminado.")
                return
        print(f"No se encontró un producto con ID {ID}.")
    
    def actualizar_cantidad_por_ID(self, ID, nueva_cantidad):
        for producto in self.lista_productos:
            if producto["ID"] == ID:
                producto["cantidad"] = nueva_cantidad
                print(f"Cantidad del producto con ID {ID} actualizada a {nueva_cantidad}.")
                return
        print(f"No se encontró un producto con ID {ID}.")
    
    def actualizar_precio_por_ID(self, ID, nuevo_precio):
        for producto in self.lista_productos:
            if producto["ID"] == ID:
                producto["precio"] = nuevo_precio
                print(f"Precio del producto con ID {ID} actualizado a {nuevo_precio}.")
                return
        print(f"No se encontró un producto con ID {ID}.")

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.lista_productos:
            if producto["nombre"].lower() == nombre.lower():
                print(f"Producto encontrado: ID: {producto['ID']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
                return
        print(f"No se encontró un producto con el nombre {nombre}.")

    def mostrar_inventario(self):
        if not self.lista_productos:
            print("El inventario está vacío.")
        else:
            print("Inventario de productos:")
            for producto in self.lista_productos:
                print(f"ID: {producto['ID']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
# Menú principal
# Sistema de gestión de inventario para una tienda de artículos electrónicos
empresa = Inventario ( ID="", nombre="", precio=0.0, cantidad=0)
while True:
    print("\nWelcome to the Inventory Management System")
    print("Elija una opción")
    print("1. Añadir producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad por ID")  
    print("4. Actualizar precio por ID")
    print("5. Buscar producto por nombre")
    print("6. Mostrar inventario")
    print("7. Salir")

    opcion = input("Ingrese una opción (1-7): ")
    if opcion == "1":
        empresa.añadir_producto(Producto)
    elif opcion == "2":
        ID = input("Ingrese el ID del producto a eliminar: ")
        empresa.eliminar_producto_por_ID(ID)
    elif opcion == "3":
        ID = input("Ingrese el ID del producto a actualizar la cantidad: ")
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        empresa.actualizar_cantidad_por_ID(ID, nueva_cantidad)
    elif opcion == "4":
        ID = input("Ingrese el ID del producto a actualizar el precio: ")
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        empresa.actualizar_precio_por_ID(ID, nuevo_precio)
    elif opcion == "5":
        nombre = input("Ingrese el nombre del producto a buscar: ")
        empresa.buscar_producto_por_nombre(nombre)
    elif opcion == "6":
        empresa.mostrar_inventario()
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    

    

    
    

    

