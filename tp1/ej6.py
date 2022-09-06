import re

"""
Números enteros pares (ej. 20, -344, -02, 2, 0, 00344).
"""


def validate_a(value: str) -> bool:
    return re.search(r"[-+0]?(\d[02468])+$", value) is not None


"""
Números enteros pares sin ceros no significativos (no puede generar -02).
"""


def validate_b(value: str) -> bool:
    return re.search(r"(^[-+]?)([1-9]\d{0,}[02468]$|(^[1-9]+[02468]$|^[2468]$))", value) is not None


"""
Nombre de variables en Python, un identificador comienza con una letra minúscula o un
guión bajo (_) seguido de cero o más letras minúsculas, guión bajo o dígitos (0 a 9).
"""


def validate_c(value: str) -> bool:
    return re.search(r"^[a-z_].*$", value) is not None


"""
{a^nbc^m / n,m ∈| N* ^ n>0 ^ m>0 } , con Σ = {a, b, c}.
"""


def validate_d(value: str) -> bool:
    return re.search(r"^[a]*[b][c]*$", value) is not None


"""
Direcciones IPv4 (ej. 10.0.1.2, 192.168.1.1, 127.0.0.1, etc.).
"""


def validate_e(value: str) -> bool:
    return re.search(r"^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$", value) is not None


"""
Direcciones IPv4 con puerto (ej. 127.0.0.1:8080, 127.0.0.1:4200, 127.0.0.1:80).
"""


def validate_f(value: str) -> bool:
    return re.search(r"^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?):[1-9]\d*$", value) is not None


"""
Números de tarjeta de crédito Visa (Begin with a 4 and have 13 or 16 digits).
"""


def validate_g(value: str) -> bool:
    return re.search(r"[4]\d{12}$|[4]\d{15}$", value) is not None


if __name__ == "__main__":
    print(validate_b("-0222"))
