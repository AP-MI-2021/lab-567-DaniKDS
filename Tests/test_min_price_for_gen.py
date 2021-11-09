from Domain.carte import creaza_carte
from Logic.min_price_for_gen import get_min_price_for_gen


def get_data():
    return [
        creaza_carte(1, 'book1', 'g1', 111, 'silver'),
        creaza_carte(2, 'book2', 'g1', 20, 'none'),
        creaza_carte(3, 'book3', 'g7', 8, 'gold'),
        creaza_carte(4, 'book4', 'g2', 34, 'silver'),
        creaza_carte(5, 'book5', 'g7', 29.6, 'none'),
        creaza_carte(6, 'book5', 'g3', 23.02, 'none'),
        creaza_carte(7, 'book5', 'g7', 99999.33, 'none'),
    ]

def test_get_min_price_for_gen():
    carti = get_data()
    result = get_min_price_for_gen(carti)
    assert result['g1'] == 20
    assert result['g2'] == 34
    assert result['g3'] == 20
    assert result['g7'] == 8