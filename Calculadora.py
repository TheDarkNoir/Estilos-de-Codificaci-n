"""Calculadora básica con menú y validación de entradas.

Lista de estilo:
- funciones y variables descriptivas
- 4 espacios de sangría
- docstrings claras
- manejo de errores con try/except
- pruebas al final
"""


def suma(a, b):
    """Retorna la suma de dos números.

    Parámetros:
    - a (int|float): primer sumando
    - b (int|float): segundo sumando
    Retorna:
    - int|float: resultado de a + b
    """
    return a + b


def resta(a, b):
    """Retorna la resta de dos números.

    Parámetros:
    - a (int|float): minuendo
    - b (int|float): sustraendo
    Retorna:
    - int|float: resultado de a - b
    """
    return a - b


def multiplica(a, b):
    """Retorna el producto de dos números.

    Parámetros:
    - a (int|float): primer factor
    - b (int|float): segundo factor
    Retorna:
    - int|float: resultado de a * b
    """
    return a * b


def divide(a, b):
    """Retorna la división de a entre b.

    Maneja división por cero devolviendo None.
    """
    if b == 0:
        return None
    return a / b


def pedir_numero(prompt_text):
    """Pide un número al usuario y valida int/float."""
    while True:
        texto = input(prompt_text).strip()
        try:
            if "." in texto:
                return float(texto)
            return int(texto)
        except ValueError:
            print("Entrada inválida: introduce un número válido.")


def calculadora():
    """Función principal con menú interactivo."""
    while True:
        print("\n--- Menú Calculadora ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "5":
            print("Saliendo. ¡Hasta pronto!")
            break

        if opcion not in {"1", "2", "3", "4"}:
            print("Opción no válida, intenta nuevamente.")
            continue

        a = pedir_numero("Ingresa el primer número: ")
        b = pedir_numero("Ingresa el segundo número: ")

        if opcion == "1":
            resultado = suma(a, b)
            print(f"Resultado: {a} + {b} = {resultado}")
        elif opcion == "2":
            resultado = resta(a, b)
            print(f"Resultado: {a} - {b} = {resultado}")
        elif opcion == "3":
            resultado = multiplica(a, b)
            print(f"Resultado: {a} * {b} = {resultado}")
        elif opcion == "4":
            resultado = divide(a, b)
            if resultado is None:
                print("Error: división por cero no permitida.")
            else:
                print(f"Resultado: {a} / {b} = {resultado}")


if __name__ == "__main__":
    # Pruebas simples de funcionalidad (2-3 ejemplos)
    assert suma(2, 3) == 5
    assert resta(5, 2) == 3
    assert multiplica(4, 3) == 12
    assert divide(8, 2) == 4.0
    assert divide(8, 0) is None

    calculadora()
