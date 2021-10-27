
def creaza_carte(id:int, titlu, gen , pret:float, tip_reducere:str):
    """
    Creeaza o carte
    :param id: id-ul cartii,care este unic
    :param titlu: titlul cartii,nenul
    :param gen: genul cartii,nenul
    :param pret: pretul cartii
    :param tip_reducere: tipul de reducere al cartii
    :return:o carte
    """

    return {
        'id_carte':id,
        'titlu_carte':titlu,
        'gen_carte':gen,
        'pret_carte':pret,
        'reducere_carte':tip_reducere
    }


def get_id(carte):
    '''
    Getter pentru id-ul cartii.
    :param carte:carte
    :return:id-ul cartii.
    '''
    return carte['id_carte']


def get_titlu(carte):
    '''
    Getter pentru titlul cartii.
    :param carte:carte
    :return:id-ul cartii.
    '''
    return carte['titlu_carte']


def get_gen_carte(carte):
    '''
    Getter pentru genul cartii.
    :param carte:carte
    :return:id-ul cartii.
    '''
    return carte['gen_carte']


def get_pret_carte(carte):
    '''
    Getter pentru pretul cartii.
    :param carte:carte
    :return:id-ul cartii.
    '''
    return carte['pret_carte']


def get_reducere_carte(carte):
    '''
    Getter pentru tipul de reducere al cartii.
    :param carte:carte
    :return:id-ul cartii.
    '''
    return carte['reducere_carte']

def get_str_carte(carte):
    return  f'Cartea are id-ul:  {get_id(carte)} , titlu: {get_titlu(carte)} , genul : {get_gen_carte(carte)} , pret: {get_pret_carte(carte)}, tip reducere : {get_reducere_carte(carte)}.'

