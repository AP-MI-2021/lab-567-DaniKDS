from Domain.carte import get_str_carte, get_titlu, get_gen_carte, get_pret_carte, get_reducere_carte, creaza_carte
from Logic.crud import create, read, update, delete


def show_menu():
    print('1. CRUD')
    print('x. Exit')

def handle_add(carti):

    id_carte = int(input('Dati id-ul cartii: '))
    titlu = input('Dati titlul cartii: ')
    gen = input('Dati genul cartii: ')
    pret = float(input('Dati pretul cartii: '))
    tip_reducere = str(input('Dati tipul de reducere al cartii: '))

    return create(carti, id_carte, titlu, gen, pret, tip_reducere)


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

    id_carte = int(input('Dati id-ul prajiturii care se actualizeaza: '))
    titlu = input('Dati titlul cartii: ')
    gen = input('Dati genul cartii: ')
    pret = float(input('Dati pretul cartii: '))
    tip_reducere = str(input('Dati tipul de reducere al cartii: '))

    return update(carti, creaza_carte(id_carte, titlu, gen, pret, tip_reducere))


def handle_delete(carti):
    id_carte = int(input('Dati id-ul cartii care se va sterge: '))
    carti = delete(carti, id_carte)
    print('Stergerea a fost efectuata cu succes.')
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



def run_ui(carti):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            carti = handle_crud(carti)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return carti