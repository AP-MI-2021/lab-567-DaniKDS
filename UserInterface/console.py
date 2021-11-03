from Domain.carte import get_str_carte, get_titlu, get_gen_carte, get_pret_carte, get_reducere_carte, creaza_carte
from Logic.crud import create, read, update, delete
from Logic.discount import discount_function
from Logic.modifygen import modify_gen


def show_menu():
    print('1. CRUD')
    print('2. Aplicarea unui discount de `5%` pentru toate reducerile silver și `10%` pentru toate reducerile gold. ')
    print('3.Modificarea genului pentru un titlu dat.')
    print('4.Determinarea prețului minim pentru fiecare gen.')
    print('5.Ordonarea vânzărilor crescător după preț.')
    print('6.Afișarea numărului de titluri distincte pentru fiecare gen.')
    print('7.Undo.')
    print('x. Exit')

def handle_add(carti):
    try:

        id_carte = int(input('Dati id-ul cartii: '))
        titlu = input('Dati titlul cartii: ')
        gen = input('Dati genul cartii: ')
        pret = float(input('Dati pretul cartii: '))
        tip_reducere = str(input('Dati tipul de reducere al cartii: '))
        return create(carti, id_carte, titlu, gen, pret, tip_reducere)
    except ValueError as ve:
        print("EROARE",ve)

def handle_show_all(carti):
    for carte in carti:
        print(get_str_carte(carte))

def handle_show_details(carti):

    id_carte = int(input('Dati id-ul cartii pentru care doriti detalii: '))
    carte = read(carti, id_carte)

    print(f'titlu: {get_titlu(carte)}')
    print(f'gen: {get_gen_carte(carte)}')
    print(f'Pret: {get_pret_carte(carte)}')
    print(f'tip_de_reducere: {get_reducere_carte(carte)}')

def handle_update(carti):
    try:
        id_carte = int(input('Dati id-ul cartii care se actualizeaza: '))
        titlu = input('Dati noul titlu al cartii: ')
        gen = input('Dati noul gen al cartii: ')
        pret = float(input('Dati noul pret al cartii: '))
        tip = input('Dati noul tipul de reducere client al cartii: ')
        return update(carti, creaza_carte(id_carte, titlu, gen, pret, tip))
    except ValueError as ve:
        print('Eroare:', ve)

    return carti

def handle_delete(carti):

    try:
        id_carte = int(input('Dati id-ul cartii care se va sterge: '))
        carti = delete(carti, id_carte)
        print('Stergerea a fost efectuata cu succes.')
        return carti
    except ValueError as ve:
        print("EROARE",ve)
    return carti


def handle_crud(carti):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii carte')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            carti = handle_add(carti)
        elif optiune == '2':
            carti = handle_update(carti)
        elif optiune == '3':
            carti = handle_delete(carti)
        elif optiune == 'a':
            handle_show_all(carti)
        elif optiune == 'd':
            handle_show_details(carti)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return carti



def handle_discount(carti):

    carti  = discount_function(carti)
    print("A fost facut discountul cerut de utilizator!")
    return carti


def handle_modify_gen(carti):
    try:
        titlu = input('Dati titlul pentru modificare: ')
        genul = input('Dati noul gen: ')
        carti = modify_gen(carti, titlu, genul)
        print('Modificarea genului a fost efectuata cu succes!')
        return carti
    except ValueError as ve:
        print('Eroare: ', ve)
    return carti


def run_ui(carti):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            carti = handle_crud(carti)
        elif optiune == '2':
            carti = handle_discount(carti)
        elif optiune == '3':
            carti = handle_modify_gen(carti)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return carti