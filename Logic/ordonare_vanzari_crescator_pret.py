from Domain.carte import get_pret_carte


def get_pret_for_sortare(carte):
    return get_pret_carte(carte)

def ordonare_crecator_dupa_pret(lista_carti):
    """
    Functie care va ordona crescator lista de carti dupa pret
    :param lista_carti: lista de carti initiala
    :return: lista nou ordonata ,crescator dupa pret
    """

    return sorted(lista_carti,key=get_pret_for_sortare)