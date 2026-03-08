class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # diccionario ISBN -> Libro
        self.usuarios = {}  # diccionario ID -> Usuario
        self.ids_unicos = set()  # conjunto para IDs únicos

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.ids_unicos:
            self.usuarios[usuario.user_id] = usuario
            self.ids_unicos.add(usuario.user_id)

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.ids_unicos.remove(user_id)

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros[isbn]
            usuario.libros_prestados.append(libro)
            del self.libros[isbn]

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    break

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and libro.info[0] == valor:
                resultados.append(libro)
            elif criterio == "autor" and libro.info[1] == valor:
                resultados.append(libro)
            elif criterio == "categoria" and libro.categoria == valor:
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            return self.usuarios[user_id].libros_prestados
        return []


# Menú interactivo
def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n--- Menú Biblioteca ---")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros")
        print("8. Listar libros prestados")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.agregar_libro(Libro(titulo, autor, categoria, isbn))
        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)
        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID único: ")
            biblioteca.registrar_usuario(Usuario(nombre, user_id))
        elif opcion == "4":
            user_id = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(user_id)
        elif opcion == "5":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(user_id, isbn)
        elif opcion == "6":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.devolver_libro(user_id, isbn)
        elif opcion == "7":
            criterio = input("Buscar por (titulo/autor/categoria): ")
            valor = input("Valor: ")
            resultados = biblioteca.buscar_libros(criterio, valor)
            for libro in resultados:
                print(libro)
        elif opcion == "8":
            user_id = input("ID del usuario: ")
            libros = biblioteca.listar_libros_prestados(user_id)
            for libro in libros:
                print(libro)
        elif opcion == "9":
            break
        else:
            print("Opción inválida.")


# Ejecutar menú
menu()

