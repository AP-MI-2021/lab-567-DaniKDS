from Domain.carte import creaza_carte, get_id
from Logic.crud import create
from Logic.undo_redo import do_undo, do_redo


def test_undo():
    #1.lista initiala goala
    carti = []
    undo_list = []
    redo_list = []

    #2.adaugam un obiect

    carti = create(carti, 1, 'book1', 'gen1', 90, 'none', undo_list,redo_list)

    #3.adaugam inca un obiect

    carti = create(carti, 2, 'book2', 'gen2', 45.4, 'silver', undo_list, redo_list)

    #4.adaugam inca un obiect

    carti = create(carti, 3, 'book3', 'gen3', 133, 'gold', undo_list, redo_list)

    assert len(carti) ==3

    #5.undo scoate ultimul obiect adaugat
    carti = do_undo(undo_list, redo_list, carti)
    gasit = 0
    for carte in carti:
        if get_id(carte) == 1:
            gasit = gasit + 1
        elif get_id(carte) == 2:
            gasit = gasit + 1
    assert gasit == 2

    #6.	inca un undo scoate penultimul obiect adaugat
    carti = do_undo(undo_list, redo_list, carti)
    assert len(carti) == 1
    gasit = 0
    for carte in carti:
        if get_id(carte) == 1:
            gasit = 1
    assert gasit == 1

    #7.inca un undo scoate si primul element adaugat
    carti = do_undo(undo_list, redo_list, carti)
    assert carti ==[]

    #8.inca un undo nu face nimic
    assert do_undo(undo_list, redo_list, carti) is None

    #9.adaugam trei obiecte
    carti = create(carti, 4, 'boo4', 'ge4', 300, 'gold', undo_list, redo_list)
    carti = create(carti, 5, 'boo5', 'ge5', 80, 'none', undo_list, redo_list)
    carti = create(carti, 6, 'booo6', 'ge6', 10.9, 'silver', undo_list, redo_list)

    #10.redo nu face nimic
    carti_noi = do_redo(undo_list, redo_list, carti)
    assert carti_noi is None

    #11.doua undo-uri scot ultimele 2 obiecte
    carti = do_undo(undo_list, redo_list, carti)
    carti = do_undo(undo_list, redo_list, carti)
    assert len(carti) == 1
    gasit = 0
    for carte in carti:
        if get_id(carte) == 4:
            gasit = 1
    assert gasit == 1

    # 12.redo anuleaza ultimul undo, daca ultima operatie e undo

    carti = do_redo(undo_list, redo_list, carti)
    assert len(carti) == 2
    gasit = 0
    for carte in carti:
        if get_id(carte) == 4:
            gasit = gasit + 1
        elif get_id(carte) == 5:
            gasit = gasit + 1
    assert gasit == 2

    #13.redo anuleaza si primul undo

    carti = do_redo(undo_list, redo_list, carti)
    gasit = 0
    for carte in carti:
        if get_id(carte) == 4:
            gasit = gasit + 1
        elif get_id(carte) == 5:
            gasit = gasit + 1
        elif get_id(carte) == 6:
            gasit = gasit + 1
    assert gasit == 3

    #14.doua undo-uri scot ultimele 2 obiecte
    carti = do_undo(undo_list, redo_list, carti)
    carti = do_undo(undo_list, redo_list, carti)
    assert len(carti) == 1
    gasit = 0
    for carte in carti:
        if get_id(carte) == 4:
            gasit = gasit + 1
    assert gasit == 1

    #15.adaugam un obiect
    carti = create(carti, 7, 'booo7', 'gen7', 121.77, 'silver', undo_list, redo_list)
    assert len(carti) == 2

    #16.redo nu face nimic, deoarece ultima operatie nu este un undo
    assert  do_redo(undo_list, redo_list, carti) == None

    gasit = 0
    for carte in carti:
        if get_id(carte) == 4:
            gasit = gasit + 1
        elif get_id(carte) == 7:
            gasit = gasit + 1
    assert gasit == 2


    #17.undo anuleaza adaugarea lui o4
    carti = do_undo(undo_list, redo_list, carti)
    assert len(carti) == 1
    gasit = 0
    for carte in carti:
        if get_id(carte) == 4:
            gasit = gasit + 1
    assert gasit == 1

    #18.undo anuleaza adaugarea lui o1 - practic se continua sirul de undo de la pct 14
    carti = do_undo(undo_list, redo_list, carti)
    assert len(carti) == 0
    assert carti == []

    #19.se anuleaza ultimele 2 undo-uri
    carti = do_redo(undo_list, redo_list, carti)
    carti = do_redo(undo_list, redo_list, carti)
    gasit = 0
    for carte in carti:
        if get_id(carte) == 4:
            gasit = gasit + 1
        elif get_id(carte) == 7:
            gasit = gasit + 1
    assert gasit == 2

    #20.redo nu face nimic
    assert do_redo(undo_list, redo_list, carti) is None



