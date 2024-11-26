class TablaHashLineal:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [None] * tamano
        self.borrado = object()

    def funcion_hash(self, clave):
        return clave % self.tamano

    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        for _ in range(self.tamano):
            if self.tabla[indice] is None or self.tabla[indice] is self.borrado:
                self.tabla[indice] = (clave, valor)
                return
            elif self.tabla[indice][0] == clave:
                self.tabla[indice] = (clave, valor)
                return
            indice = (indice + 1) % self.tamano
        raise Exception("Tabla hash llena")

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        for _ in range(self.tamano):
            if self.tabla[indice] is None:
                return None
            if self.tabla[indice] is not self.borrado and self.tabla[indice][0] == clave:
                return self.tabla[indice][1]
            indice = (indice + 1) % self.tamano
        return None

    def eliminar(self, clave):
        indice = self.funcion_hash(clave)
        for _ in range(self.tamano):
            if self.tabla[indice] is None:
                return False
            if self.tabla[indice] is not self.borrado and self.tabla[indice][0] == clave:
                self.tabla[indice] = self.borrado
                return True
            indice = (indice + 1) % self.tamano
        return False


def menu_direccion_abierta():
    tamano = int(input("Ingresa el tamaño de la tabla hash: "))
    tabla = TablaHashLineal(tamano)

    while True:
        print("\n--- Tabla Hash con Dirección Abierta ---")
        print("1. Insertar elemento")
        print("2. Buscar elemento")
        print("3. Eliminar elemento")
        print("4. Mostrar tabla completa")
        print("5. Salir")

        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            clave = int(input("Ingresa la clave (entero): "))
            valor = input("Ingresa el valor: ")
            try:
                tabla.insertar(clave, valor)
                print("Elemento insertado.")
            except Exception as e:
                print(e)
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
            for i, elemento in enumerate(tabla.tabla):
                print(f"Índice {i}: {elemento}")
        elif opcion == 5:
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

menu_direccion_abierta()
