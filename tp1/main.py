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


def validate_c(value: str) -> bool:
    pass


if __name__ == "__main__":
    print(validate_b("-0222"))
