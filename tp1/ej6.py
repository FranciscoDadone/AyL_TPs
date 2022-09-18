import re


def validate_a(value: str) -> bool:
    """
    Números enteros pares (ej. 20, -344, -02, 2, 0, 00344).
    """
    return re.search(r"[-+0]?(\d[02468])+$", value) is not None


def validate_b(value: str) -> bool:
    """
    Números enteros pares sin ceros no significativos (no puede generar -02).
    """
    return re.search(r"(^[-+]?)([1-9]\d{0,}[02468]$|(^[1-9]+[02468]$|^[2468]$))", value) is not None


def validate_c(value: str) -> bool:
    """
    Nombre de variables en Python, un identificador comienza con una letra minúscula o un
    guión bajo (_) seguido de cero o más letras minúsculas, guión bajo o dígitos (0 a 9).
    """
    return re.search(r"^[a-z_].*$", value) is not None


def validate_d(value: str) -> bool:
    """
    {a^nbc^m / n,m ∈| N* ^ n>0 ^ m>0 } , con Σ = {a, b, c}.
    """
    return re.search(r"^[a]*[b][c]*$", value) is not None


def validate_e(value: str) -> bool:
    """
    Direcciones IPv4 (ej. 10.0.1.2, 192.168.1.1, 127.0.0.1, etc.).
    """
    return re.search(r"^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$", value) is not None


def validate_f(value: str) -> bool:
    """
    Direcciones IPv4 con puerto (ej. 127.0.0.1:8080, 127.0.0.1:4200, 127.0.0.1:80).
    """
    return re.search(r"^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?):[1-9]\d*$", value) is not None


def validate_g(value: str) -> bool:
    """
    Números de tarjeta de crédito Visa (Begin with a 4 and have 13 or 16 digits).
    """
    return re.search(r"[4]\d{12}$|[4]\d{15}$", value) is not None


# if __name__ == "__main__":
#     print(validate_b("-0222"))
