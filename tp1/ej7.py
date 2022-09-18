import csv
import re


def convert(input_file_path: str, output_file_path: str) -> None:
    """
    Ejercicio 7: Programar una función Python que procese el contenido de un archivo .csv con las
    columnas [id, first_name, last_name, email, gender, avatar, job_title,
    language, ssn].
    En el nuevo archivo de salida .csv:
    1. se cambiará el orden las columnas first_name y last_name y se elimina gender
    quedando: [id, last_name, first_name, email, avatar, job_title,
    language, ssn]
    2. y se modificara el dominio en las direcciones de correo, sustituyendo el dominio actual
    (parte derecha luego del símbolo @) por @ing.unlpam.edu.ar
    :param input_file_path:
    :param output_file_path:
    :return:
    """
    out = []
    with open(input_file_path, 'r') as file1:
        csvreader = csv.reader(file1)
        for row in csvreader:
            out.append([
                row[0],
                row[2],
                row[1],
                re.sub(r"@.*", '@ing.unlpam.edu.ar', row[3]),
                row[5],
                row[6],
                row[7],
                row[8]])
    with open(output_file_path, 'w') as file2:
        csvwriter = csv.writer(file2)
        csvwriter.writerows(out)


# if __name__ == "__main__":
#     convert("MOCK_DATA.csv", "out.csv")
