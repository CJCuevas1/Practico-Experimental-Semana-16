class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    if valor < raiz.valor:
        raiz.izquierda = insertar(raiz.izquierda, valor)
    else:
        raiz.derecha = insertar(raiz.derecha, valor)
    return raiz

def mostrar(nodo):
    if nodo:
        print(nodo.valor)
        mostrar(nodo.izquierda)
        mostrar(nodo.derecha)

def mostrar_arbol():
    print("\nÁrbol actual en preorden:")
    mostrar(raiz)

raiz = None

while True:
    print("\n===== MENÚ ÁRBOL BINARIO =====")
    print("1. Insertar nodo")
    print("2. Mostrar árbol")
    print("3. Recorrer árbol")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        valor = int(input("Ingresa valor: "))
        raiz = insertar(raiz, valor)
        print("Nodo insertado correctamente")

    elif opcion == "2":
        if raiz is None:
            print("Árbol vacío")
        else:
            print("Árbol cargado correctamente")

    elif opcion == "3":
        if raiz is None:
            print("Árbol vacío")
        else:
            mostrar_arbol()

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")