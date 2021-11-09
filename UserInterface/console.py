from unittest import result

from Domain.carte import get_str_carte, get_titlu, get_gen_carte, get_pret_carte, get_reducere_carte, creaza_carte
from Logic.crud import create, read, update, delete
from Logic.discount import discount_function
from Logic.min_price_for_gen import get_min_price_for_gen
from Logic.modifygen import modify_gen
from Logic.ordonare_vanzari_crescator_pret import ordonare_crecator_dupa_pret
from Logic.show_number_titles_for_all_gen import get_number_titles_for_gen
from Logic.undo_redo import do_undo, do_redo


def show_menu():
    print('1. CRUD')
    print('2. Aplicarea unui discount de `5%` pentru toate reducerile silver și `10%` pentru toate reducerile gold. ')
    print('3.Modificarea genului pentru un titlu dat.')
    print('4.Determinarea prețului minim pentru fiecare gen.')
    print('5.Ordonarea vânzărilor crescător după preț.')
    print('6.Afișarea numărului de titluri distincte pentru fiecare gen.')
    print('u.Undo')
    print('r.Redo')
    print('x. Exit')

def handle_add(carti, undo_list, redo_list):
    try:
        id_carte = int(input('Dati id-ul cartii: '))
        titlu = input('Dati titlul cartii: ')
        gen = input('Dati genul cartii: ')
        pret = float(input('Dati pretul cartii: '))
        tip_reducere = str(input('Dati tipul de reducere al cartii: '))
        return create(carti, id_carte, titlu, gen, pret, tip_reducere, undo_list, redo_list)
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

def handle_update(carti, undo_list, redo_list):
    try:
        id_carte = int(input('Dati id-ul cartii care se actualizeaza: '))
        titlu = input('Dati noul titlu al cartii: ')
        gen = input('Dati noul gen al cartii: ')
        pret = float(input('Dati noul pret al cartii: '))
        tip = input('Dati noul tipul de reducere client al cartii: ')
        return update(carti, creaza_carte(id_carte, titlu, gen, pret, tip,undo_list,redo_list))
    except ValueError as ve:
        print('Eroare:', ve)

    return carti

def handle_delete(carti, undo_list, redo_list):

    try:
        id_carte = int(input('Dati id-ul cartii care se va sterge: '))
        carti = delete(carti, id_carte, undo_list, redo_list)
        print('Stergerea a fost efectuata cu succes.')
        return carti
    except ValueError as ve:
        print("EROARE",ve)
    return carti


def handle_crud(carti, undo_list, redo_list):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii carte')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            carti = handle_add(carti, undo_list, redo_list)
        elif optiune == '2':
            carti = handle_update(carti, undo_list, redo_list)
        elif optiune == '3':
            carti = handle_delete(carti, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(carti)
        elif optiune == 'd':
            handle_show_details(carti)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return carti



def handle_discount(carti ,undo_list, redo_list):

    carti  = discount_function(carti,undo_list,redo_list)
    print("A fost facut discountul cerut de utilizator!")
    undo_list.append(carti)
    redo_list.clear()
    return carti


def handle_modify_gen(carti, undo_list, redo_list):
    try:
        titlu = input('Dati titlul pentru modificare: ')
        genul = input('Dati noul gen: ')
        carti = modify_gen(carti, titlu, genul,undo_list,redo_list)
        print('Modificarea genului a fost efectuata cu succes!')
        undo_list.append(carti)
        redo_list.clear()
        return carti
    except ValueError as ve:
        print('Eroare: ', ve)
    return carti


def handle_min_price_gen(carti):
    result = get_min_price_for_gen(carti)
    for gen in result:
        print(f' {gen} , {get_str_carte(result[gen])}')


def handle_sorted_for_price(carti):
    carti = ordonare_crecator_dupa_pret(carti)
    handle_show_all(carti)


def handle_show_number_distinct_title(carti):
    res = get_number_titles_for_gen(carti)
    for gen in res:
        print(f' Numarul de titluri distincte pentru genul {gen} este {res[gen]}')


def handle_undo(carti, undo_list, redo_list):
    undo_result = do_undo(undo_list,redo_list,carti)
    if undo_result is not None:
        return undo_result
    return carti


def handle_redo(carti, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list,carti)
    if redo_result is not None:
        return redo_result
    return carti


def run_ui(carti, undo_list, redo_list):

    while True:

        print("---------------------------------------------------------------------------")
        handle_show_all(carti)
        show_menu()

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            carti = handle_crud(carti, undo_list, redo_list )
        elif optiune == '2':
            carti = handle_discount(carti ,undo_list, redo_list )
        elif optiune == '3':
            carti = handle_modify_gen(carti,undo_list, redo_list )
        elif optiune == '4':
            handle_min_price_gen(carti)
        elif optiune == '5':
            handle_sorted_for_price(carti)
        elif optiune == '6':
            handle_show_number_distinct_title(carti)
        elif optiune == 'u':
            carti = handle_undo(carti ,undo_list ,redo_list)
        elif optiune == 'r':
            carti = handle_redo(carti, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return carti