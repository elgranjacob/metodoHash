class TablaHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]

    def funcion_hash(self, clave):
        return clave % self.tamano

    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        for elemento in self.tabla[indice]:
            if elemento[0] == clave:  
                elemento[1] = valor
                return
        self.tabla[indice].append([clave, valor])

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        for elemento in self.tabla[indice]:
            if elemento[0] == clave:
                return elemento[1]  
        return None

    def eliminar(self, clave):
        indice = self.funcion_hash(clave)
        for i, elemento in enumerate(self.tabla[indice]):
            if elemento[0] == clave:
                del self.tabla[indice][i]
                return True
        return False


def menu_encadenamiento():
    tamano = int(input("Ingresa el tamaño de la tabla hash: "))
    tabla = TablaHash(tamano)

    while True:
        print("\n--- Tabla Hash con Encadenamiento ---")
        print("1. Insertar elemento")
        print("2. Buscar elemento")
        print("3. Eliminar elemento")
        print("4. Mostrar tabla completa")
        print("5. Salir")

        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            clave = int(input("Ingresa la clave (entero): "))
            valor = input("Ingresa el valor: ")
            tabla.insertar(clave, valor)
            print("Elemento insertado.")
        elif opcion == 2:
            clave = int(input("Ingresa la clave que deseas buscar: "))
            resultado = tabla.buscar(clave)
            if resultado is not None:
                print(f"Valor encontrado: {resultado}")
            else:
                print("Clave no encontrada.")
        elif opcion == 3:
            clave = int(input("Ingresa la clave que deseas eliminar: "))
            if tabla.eliminar(clave):
                print("Elemento eliminado.")
            else:
                print("Clave no encontrada.")
        elif opcion == 4:
            print("Contenido de la tabla hash:")
            for i, lista in enumerate(tabla.tabla):
                print(f"Índice {i}: {lista}")
        elif opcion == 5:
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

menu_encadenamiento()
