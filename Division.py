def divide(a, b):
    """Retorna la división de a entre b.

    Maneja división por cero devolviendo None.
    """
    if b == 0:
        return None
    return a / b