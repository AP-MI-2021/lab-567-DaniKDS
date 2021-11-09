from Domain.carte import creaza_carte, get_id
from Logic.ordonare_vanzari_crescator_pret import ordonare_crecator_dupa_pret


def get_data():
    return [
        creaza_carte(1, 'book1', 'g1', 11, 'silver'),
        creaza_carte(2, 'book2', 'g1', 73, 'none'),
        creaza_carte(3, 'book3', 'g6', 98.3, 'none'),
        creaza_carte(4, 'book4', 'g2', 33.4, 'silver'),
        creaza_carte(5, 'book5', 'g6', 33.5, 'silver'),
        creaza_carte(6, 'book6', 'g5', 33.6, 'none'),
        creaza_carte(7, 'book7', 'g1', 11111, 'gold'),
    ]


def test_ordonare_crecator_dupa_pret():
    carti = get_data()
    carti = ordonare_crecator_dupa_pret(carti)
    assert len(carti) == 7
    assert get_id(carti[0]) == 1
    assert get_id(carti[1]) == 4
    assert get_id(carti[2]) == 5
    assert get_id(carti[3]) == 6
    assert get_id(carti[4]) == 2
    assert get_id(carti[5]) == 3
    assert get_id(carti[6]) == 7
