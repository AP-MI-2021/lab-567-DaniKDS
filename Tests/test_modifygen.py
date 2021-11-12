from Domain.carte import creaza_carte, get_gen_carte
from Logic.modifygen import modify_gen, titlu_apartine_lista


def get_data():
    return [
        creaza_carte(1, 'cart1', 'gen1', 80, 'silver'),
        creaza_carte(2, 'cart2', 'gen2', 34, 'none'),
        creaza_carte(3, 'cart3', 'gen3', 88, 'gold'),
        creaza_carte(4, 'cart4', 'gen4', 58, 'gold'),
        creaza_carte(5, 'cart5', 'gen5', 84, 'gold'),
        creaza_carte(6, 'cart6', 'gen6', 22.3, 'gold')

    ]

def test_modify_gen():

    carti = get_data()
    carti = modify_gen(carti, 'cart1', 'g1',[],[])
    carti = modify_gen(carti, 'cart2', 'g2',[],[])
    assert get_gen_carte(carti[0]) == 'g1'
    assert get_gen_carte(carti[1]) == 'g2'
    try:
        _ = modify_gen(carti, 'ccc55' , 'genullll3444',[],[])
        assert False
    except ValueError:
        assert True  # sau pass

def test_titlu_apartine_lista():
    carti = get_data()
    assert titlu_apartine_lista(carti, 'cart1') == 1
    assert titlu_apartine_lista(carti, 'cart4') == 4
    assert titlu_apartine_lista(carti, 'carte100000') is None

def organizare_teste():
    test_modify_gen()
    test_titlu_apartine_lista()