from Domain.carte import get_titlu, get_id, creaza_carte, get_pret_carte, get_reducere_carte


def modify_gen(lista_carti, titlu, gen):
    """
    Modifica genul unei carti dupa un anume titlu dat de ultilizator
    :param lista_carti: lista de carti
    :param titlu: titlul dat al cartii respective
    :param gen: genul care urmeaza sa fie schimbat
    :return: noul gen pentru titlul dat
    """
    if titlu_apartine_lista(lista_carti,titlu) is None:
        raise ValueError('Titlul nu apare in lista')

    new_carti = []
    for carte in lista_carti:
        if get_titlu(carte) == titlu:
            carte_noua = creaza_carte(
                get_id(carte),
                get_titlu(carte),
                gen,
                get_pret_carte(carte),
                get_reducere_carte(carte)
            )
            new_carti.append(carte_noua)
        else:
            new_carti.append(carte)
    return new_carti

def titlu_apartine_lista(lista_carti , titlu):
    """
    Verifica daca titlul dat se gaseste in lista de carti
    :param lista_carti:lista de carti
    :param titlu: titlul care va fi verificat
    :return: -id-ul vanzarii daca titlul exista in lista
             - None daca nu exista in lista
    """
    carte_id = None
    for carte in lista_carti:
        if get_titlu(carte) == titlu:
            carte_id = get_id(carte)
    if carte_id:
        return carte_id
    return None