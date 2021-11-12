from Domain.carte import creaza_carte, get_id


def create(lista_carti, id_carte: int, titlu, gen ,pret:float, tip_reducere:str, undo_list:list, redo_list:list):
    '''
    Cream o lista de carti.
    :param lista_carti:lista de carti
    :param id_carte:id-ul cartii de tip int
    :param titlu:titlul cartii
    :param gen:genul cartii
    :param pret:pretul cartii de tip float
    :param tip_reducere:tipul de reducere al cartii de tip string
    :param undo_list:lista de undo
    :param redo_list:lista de redo
    :return:returneaza o lista de carti formata din lista_carti + o noua carte adaugata
    '''

    if read(lista_carti, id_carte) is not None:#adica avem o carte care deja exista
        raise ValueError(f'Exista deja o carte cu id-ul {id_carte}')

    carte = creaza_carte(id_carte, titlu, gen, pret, tip_reducere)
    undo_list.append(lista_carti)
    redo_list.clear()

    return lista_carti + [carte]


def read( lista_carti ,id_carte:int=None):
    '''
    Citeste o carte din "baza de date"
    :param lista_carti:lista de carti
    :param id_carte:id-ul de carte dorit
    :return:- cartea cu id-ul id_carte care exista in lista de carti
            -lista de carti daca id_carte=None
            -None daca nu exista o carte cu id_carte
    '''

    if not id_carte:
        return lista_carti

    carte_cu_id = None
    for carte in lista_carti:
        if get_id(carte) == id_carte:
            carte_cu_id = carte

    if carte_cu_id:
        return carte_cu_id
    return None

def update(lista_carti, new_carte, undo_list, redo_list):
    '''
    Actualizeaza o carte.
    :param lista_carti:lista de carti
    :param new_carte:noua carte pe care o adaugam in lista new_carti
    :param undo_list:lista de undo
    :param redo_list:lista de redo
    :return:noua lista cu cartea actualizata
    '''
    if read(lista_carti, get_id(new_carte)) is None:
        raise ValueError(f'Nu exista o vanzare cu id-ul {get_id(new_carte)} pe care sa o actualizam')
    new_carti = []
    for carte in lista_carti:
        if get_id(carte) != get_id(new_carte):
            new_carti.append(carte)
        else:
            new_carti.append(new_carte)

    undo_list.append(lista_carti)
    redo_list.clear()
    return new_carti


def delete(lista_carti , id_carte, undo_list, redo_list):
    '''
    Stergem o carte din lista.
    :param lista_carti:lista de carti
    :param id_carte:id-ul cartii
    :param undo_list:lista de undo
    :param redo_list:lista de redo
    :return:o lista de carti fara cartea cu id-ul dat
    '''

    if read(lista_carti, id_carte) is None:
        raise ValueError(f'Nu xista o carte cu id-ul {id_carte} pe care sa o stergem.')

    new_carti = []
    for carte in lista_carti:
        if get_id(carte) != id_carte:
            new_carti.append(carte)

    undo_list.append(lista_carti)
    redo_list.clear()
    return new_carti





