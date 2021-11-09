from Domain.carte import get_gen_carte, get_titlu


def get_number_titles_for_gen(lista_carti):
    """
    Aceasta functie va afisa numarul de titluri distincte pentru fiecare gen .
    :param lista_carti:lista initiala de carti
    :return: va returna in dictionarul result1 numarul de carti cu titluri distinte pentru fiecare cheia a dictionarului care reprezinta genul de carte.
    """
    result1 = {} #aici retin numarul de titluri pentru fiecare gen
    result2 = {}#aici retin fiecare titlu pentru un anume gen
    for carte in lista_carti:

        gen = get_gen_carte(carte)
        titlu = get_titlu(carte)

        if gen in result1:
            if titlu not in result2[gen]:
                result1[gen] = result1[gen] + 1
                titluri = result2[gen] + titlu
                result2[gen] = titluri
        else:
            result1[gen] = 1
            result2[gen] = titlu

    return result1
