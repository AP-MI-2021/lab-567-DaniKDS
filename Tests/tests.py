

from Domain.carte import creaza_carte, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
    creaza_carte(1, "Carte 1", "psihologic", 63.70, "silver"),
    creaza_carte(2, "Carte 2", "thriller", 52.50, "gold"),
    creaza_carte(3, "Carte 3", "informativ", 49, "none"),
    creaza_carte(4, "Carte 4", "romantic", 45.90, "gold"),
    creaza_carte(5, "Carte 5", "comedie", 53.80, "none")
    ]

def test_create():

    carti = get_data()

    params = (66, "Carte 5", "comedie", 53.80, "none", [], [])
    p_new = creaza_carte(*params[:-2])
    new_carti = create(carti, *params)
    assert len(new_carti) == len(carti) + 1
    assert p_new in new_carti

    params2=(66, "Carte 6", "crazy", 58.80, "gold", [], [])

    try:
        _ = create(new_carti,*params2)
        assert False
    except ValueError:
        assert True #sau pass

def test_read():
    carte = get_data()
    some_p = carte[2]
    assert read(carte, get_id(some_p)) == some_p
    assert read(carte, None) == carte

def test_update():

    vanzari = get_data()
    v_updated = creaza_carte(1, 'cartenoua', 'gen nou', 9.2, 'none')
    updated = update(vanzari, v_updated, [] ,[])
    assert v_updated in updated
    assert v_updated not in vanzari
    assert len(updated) == len(vanzari)

    try:
        params2 = (7, 'cartenasoa', 'gen vechi', 98, 'gold', [], [])
        v_updated = creaza_carte(*params2[:-2])
        _ = update(vanzari, v_updated, [], [])
        assert False
    except ValueError:
        assert True  # sau pass


def test_delete():

    carti = get_data()
    to_delete = 3
    p_deleted = read(carti, to_delete)
    deleted = delete(carti, to_delete, [], [])
    assert p_deleted not in deleted
    assert p_deleted in carti
    assert len(deleted) == len(carti) - 1

def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()


