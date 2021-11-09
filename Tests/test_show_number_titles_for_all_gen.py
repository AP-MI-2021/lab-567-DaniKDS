from Domain.carte import creaza_carte
from Logic.show_number_titles_for_all_gen import get_number_titles_for_gen


def get_data():
    return [
        creaza_carte(1, 'book1', 'g3', 60, 'silver'),
        creaza_carte(2, 'book2', 'g2', 20, 'none'),
        creaza_carte(3, 'book3', 'g3', 12, 'gold'),
        creaza_carte(4, 'book4', 'g4', 34, 'silver'),
        creaza_carte(5, 'book5', 'g2', 34, 'silver'),
    ]


def test_get_number_titles_for_gen():
    carti = get_data()
    rezultat = get_number_titles_for_gen(carti)
    assert rezultat['g1'] == 0
    assert rezultat['g2'] == 2
    assert rezultat['g4'] == 1
    assert rezultat['g3'] == 2
