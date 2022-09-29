import sys
import json
import xmltodict
import time


def main(argv):
    with open(argv[0], 'r') as file:
        if ".jff" in argv[0]:
            j = parse_jff(file)
        else:
            j = json.load(file)
            # Hacer la comprobación del lenguaje.
            # Solo en formato JSON ya que JFlap no exporta ningún atributo con el lenguaje.
            for qs in j['Delta']:
                for i in j['Delta'][qs]:
                    if j['Delta'][qs][i]['e'] not in j['Gamma']:
                        print('La trama no pertenece al lenguaje')
                        return

        arg = argv[1] if len(argv) > 1 else ""
        solve(j, arg)


def solve(json_data, trama: str):
    end = json_data['F']
    start = json_data['q0']
    empty = json_data['B']
    q = start
    index = 0
    center = 0
    last_print = ""
    last_index = 0

    if len(trama) == 0:
        trama = empty

    _print(trama, 0)
    while q not in end:
        for i in json_data['Delta'][q]:
            s = trama[index]
            if json_data['Delta'][q][i]['e'] == s:
                if "w" in dict(json_data['Delta'][q][i]).keys():
                    trama = trama[:index] + json_data['Delta'][q][i]['w'] + trama[index + 1:]
                if str(json_data['Delta'][q][i]['m']).lower() == 'r':
                    index += 1
                if str(json_data['Delta'][q][i]['m']).lower() == 'l':
                    index -= 1
                q = json_data['Delta'][q][i]['q']
            if (index + 1) == 0:
                trama = empty + trama
                center += 1
                index = 0
            elif (index + 1) > len(trama):
                trama += empty
            if last_print != trama or last_index != index:
                print('Index: ', index)
                _print(trama, index)
                last_index = index
                last_print = trama
                time.sleep(1)
            if q in end:
                print('OK')


def _print(trama, index):
    print(trama)
    print(" " * index + "^")
    time.sleep(1)


def parse_jff(file):
    """
    Parsea el .jff (XML) a formato JSON.
    :param file:
    :return json:
    """
    xml = xmltodict.parse(file.read())

    j = {
        "Q": [],
        "Sigma": [],
        "Gamma": [],
        "Delta": {},
        "B": "#",
        "q0": "",
        "F": []
    }
    for block in xml['structure']['automaton']['block']:
        if block['@name'] not in j['Q']:
            j['Q'].append(block['@name'])
        if 'initial' in block:
            j['q0'] = block['@name']
        if 'final' in block:
            j['F'].append(block['@name'])

    for transition in xml['structure']['automaton']['transition']:
        if not 'q' + transition['from'] in j['Delta']:
            j['Delta']['q' + transition['from']] = {}
        new_key = 0
        for key in dict(j['Delta']['q' + transition['from']]).keys():
            if new_key < int(key) + 1:
                new_key = int(key) + 1
        j['Delta']['q' + transition['from']][str(new_key)] = {
            "q": "q" + transition['to'],
            "e": transition['read'] if transition['read'] is not None else "#",
            "w": transition['write'] if transition['write'] is not None else "#",
            "m": transition['move']
        }
    return j


if __name__ == "__main__":
    main(sys.argv[1:])
