from Domain.carte import creaza_carte, get_id


def create(lista_carti, id_carte:int, titlu, gen ,pret:float, tip_reducere:str):
    '''
    Cream o lista de carti.
    :param lista_carti:lista de carti
    :param id_carte:id-ul cartii de tip int
    :param titlu:titlul cartii
    :param gen:genul cartii
    :param pret:pretul cartii de tip float
    :param tip_reducere:tipul de reducere al cartii de tip string
    :return:returneaza o lista de carti formata din lista_carti + o noua carte adaugata
    '''

    if read(lista_carti, id_carte) is not None:
        raise ValueError(f'Exista deja o carte cu id-ul {id_carte}')

    carte = creaza_carte(id_carte, titlu, gen, pret, tip_reducere)
    return lista_carti + [carte]


def read( lista_carti ,id_carte:int=None):
    '''
    Citeste o carte din "baza de date"
    :param lista_carti:lista de carti
    :param id_carte:id-ul de carte dorit
    :return:- cartea cu id-ul id_carte exista in lista de carti
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

def update(lista_carti, new_carte):
    '''
    Actualizeaza o carte.
    :param lista_carti:lista de carti
    :param new_carte:noua carte pe care o adaugam in lista new_carti
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
    return new_carti


def delete(lista_carti , id_carte):
    '''
    Stergem o carte din lista.
    :param lista_carti:lista de carti
    :param id_carte:id-ul cartii
    :return:o lista de carti fara cartea cu id-ul dat
    '''

    if read(lista_carti, id_carte) is None:
        raise ValueError(f'Nu xista o carte cu id-ul {id_carte} pe care sa o stergem.')

    new_carti = []
    for carte in lista_carti:
        if get_id(carte) != id_carte:
            new_carti.append(carte)

    return new_carti





