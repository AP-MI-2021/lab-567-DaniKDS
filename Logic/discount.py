from Domain.carte import get_reducere_carte, get_pret_carte, creaza_carte, get_id, get_titlu, get_gen_carte


def discount_function(lista_carti):
    """
    O functie care va face un discount de `5%` pentru toate reducerile silver și `10%` pentru toate reducerile gold.
    :param lista_carti: lista actuala de carti
    :return: lista noua afisata dupa dicountul facut pentru cartile mentionate.
    """
    result = []

    for carte in lista_carti:
        if get_reducere_carte(carte) == "silver" :
            pret_nou = get_pret_carte(carte)-(5/100)*get_pret_carte(carte)

            result.append(creaza_carte(
                get_id(carte),
                get_titlu(carte),
                get_gen_carte(carte),
                pret_nou,
                get_reducere_carte(carte)
            ))
        elif get_reducere_carte(carte) == "gold" :
            pret_nou = get_pret_carte(carte)-(10/100)*get_pret_carte(carte)

            result.append(creaza_carte(
                get_id(carte),
                get_titlu(carte),
                get_gen_carte(carte),
                pret_nou,
                get_reducere_carte(carte)
            ))
        else:
            result.append(carte)

    return result




