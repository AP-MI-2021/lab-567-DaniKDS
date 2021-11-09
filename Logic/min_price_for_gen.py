from Domain.carte import get_pret_carte, get_gen_carte


def get_min_price_for_gen(lista_carti):
    """
    Functie care va determina pretul minim pentru fiecare gen de carte.
    :param lista_carti:lista de carti initiala
    :return:un dictionar in care cheia este genul
            si valoarea este pretul minim genului respectiv
    """
    result ={} #carte[x] = carte cu pretul minim pentru genul x
    for carte in lista_carti:

        pret = get_pret_carte(carte)
        gen = get_gen_carte(carte)

        if gen not in result:
            result[gen] = carte
        else:
            if pret < get_pret_carte(result[gen]):
                result[gen] = carte
    return result


