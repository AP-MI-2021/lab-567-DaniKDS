from Domain.carte import creaza_carte, get_pret_carte, get_gen_carte
from Logic.crud import create, update, read, delete
from Logic.discount import discount_function
from Logic.modifygen import modify_gen
from Logic.undo_redo import do_undo, do_redo


def test_undo_redo_update():

    carti = []
    undo_list = []
    redo_list = []

    carti = create(carti, 1, 'ana', 'legenda', 34.5, 'none', undo_list, redo_list)
    carti = create(carti, 2, 'oocaa', 'romantic', 90, 'silver', undo_list, redo_list)
    carti = create(carti, 3, 'mouse', 'densene', 99, 'gold', undo_list, redo_list)
    c_updated = creaza_carte(1, 'cartenou', 'gen33', 34.33, 'gold')

    updated = update(carti, c_updated, undo_list, redo_list)
    if len(undo_list) > 0:
        updated = do_undo(undo_list, redo_list, updated)
    assert c_updated not in updated
    if len(redo_list) > 0:
        updated = do_redo(undo_list, redo_list, updated)
    assert c_updated in updated

def test_undo_redo_delete():

    carti = []
    undo_list = []
    redo_list = []

    carti = create(carti, 1, 'ana', 'legenda', 34.5, 'none', undo_list, redo_list)
    carti = create(carti, 2, 'oocaa', 'romantic', 90, 'silver', undo_list, redo_list)
    carti = create(carti, 3, 'mouse', 'densene', 99, 'gold', undo_list, redo_list)
    delete_carti = 3
    c_deleted = read(carti, delete_carti)
    deleted = delete(carti, delete_carti, undo_list, redo_list)
    if len(undo_list) > 0:
        deleted = do_undo(undo_list, redo_list, deleted)
    assert c_deleted in deleted
    if len(redo_list) > 0:
        deleted = do_redo(undo_list, redo_list, deleted)
    assert c_deleted not in deleted

def test_undo_redo_discount():

    carti = []
    undo_list = []
    redo_list = []

    carti = create(carti, 1, 'ana', 'legenda', 34.5, 'none', undo_list, redo_list)
    carti = create(carti, 2, 'oocaa', 'romantic', 90, 'silver', undo_list, redo_list)
    carti = create(carti, 3, 'mouse', 'densene', 99, 'gold', undo_list, redo_list)
    carti = discount_function(carti, undo_list, redo_list)

    if len(undo_list) > 0:
        carti = do_undo(undo_list, redo_list, carti)
    assert get_pret_carte(carti[0]) == 34.5
    assert get_pret_carte(carti[1]) == 90
    assert get_pret_carte(carti[2]) == 99
    if len(redo_list) > 0:
        carti = do_redo(undo_list, redo_list, carti)
    assert get_pret_carte(carti[0]) == 34.5
    assert get_pret_carte(carti[1]) == 85.5
    assert get_pret_carte(carti[2]) == 89.1

def test_undo_redo_modifygen():

    carti = []
    undo_list = []
    redo_list = []

    carti = create(carti, 1, 'ana', 'legenda', 34.5, 'none', undo_list, redo_list)
    carti = create(carti, 2, 'oocaa', 'romantic', 90, 'silver', undo_list, redo_list)
    carti = create(carti, 3, 'mouse', 'densene', 99, 'gold', undo_list, redo_list)
    carti = modify_gen(carti, 'ana', 'iubire', undo_list, redo_list)

    if len(undo_list) > 0:
        carti = do_undo(undo_list, redo_list, carti)
    assert get_gen_carte(carti[0]) == 'legenda'
    if len(redo_list) > 0:
        carti = do_redo(undo_list, redo_list, carti)
    assert get_gen_carte(carti[0]) == 'iubire'
