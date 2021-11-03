from copy import deepcopy

from Domain.carte import get_str_carte
from Logic.crud import create, delete


def handle_add(carti, tokens):
    try:
        if len(tokens)!=6:
            raise ValueError("Numar invalid de parametrii")
        id_carte = int(tokens[1])
        titlu = tokens[2]
        gen = tokens[3]
        pret = float(tokens[4])
        tip_reducere = tokens[5]

        return create(carti, id_carte, titlu, gen, pret, tip_reducere)
    except ValueError as ve:
        print("EROARE",ve)

def handle_show_all(carti):
    for carte in carti:
        print(get_str_carte(carte))

def handle_delete(carti, tokens):
    try:
        if len(tokens)!=2:
            raise ValueError("Numar invalid de parametrii")
        id_carte = int(tokens[1])
        new_carti = delete(carti, id_carte)
        print('Stergerea a fost efectuata cu succes.')

    except ValueError as ve:
        print("EROARE",ve)
    return new_carti



def run_command(carti):
    print("Comenzile disponibile sunt:")
    print("add <id_carte> <titlu> <gen> <pret> <tip_reducere>")
    print("delete <id_carte>")
    print("showall")
    print("exit")

    while True:

        inp = input("command> ")
        commands_before_split = inp.replace(",","")
        commands = commands_before_split.split(";")
        for command in commands:

            tokens = command.split()

            if tokens[0] == "add":
                carti = handle_add(carti,tokens)
            elif tokens[0] == "showall":
                handle_show_all(carti)
            elif tokens[0] == "delete":
                carti = handle_delete(carti,tokens)
            elif tokens[0] == "exit":
                return
            else:
                print("Invalid command!")
