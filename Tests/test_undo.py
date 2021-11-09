from Domain.carte import creaza_carte, get_id
from Logic.crud import create
from Logic.undo_redo import do_undo, do_redo


def test_undo():
    #1.lista initiala goala
    obiecte = []
    undo_list = []
    redo_list = []

    #2.adaugam un obiect
    obiecte = create(obiecte, 1, 'book1', 'gen1', 90, 'none', undo_list,redo_list)

    #3.adaugam inca un obiect
    obiecte = create(obiecte, 2, 'book2', 'gen2', 45.4, 'silver', undo_list, redo_list)

    #4.adaugam inca un obiect
    obiecte = create(obiecte, 3, 'book3', 'gen3', 133, 'gold', undo_list, redo_list)

    #5.undo scoate ultimul obiect adaugat
    obiecte = do_undo(undo_list, redo_list, obiecte)

    #6.	inca un undo scoate penultimul obiect adaugat
    obiecte = do_undo(undo_list, redo_list, obiecte)
    assert len(obiecte) == 1

    #7.inca un undo scoate si primul element adaugat
    obiecte = do_undo(undo_list, redo_list, obiecte)
    assert len(obiecte) == 0

    #8.inca un undo nu face nimic
    assert do_undo(undo_list, redo_list, obiecte) is None
    assert len(obiecte) == 0

    #9.adaugam trei obiecte
    obiecte = create(obiecte, 1, 'boo1', 'ge1', 300, 'gold', undo_list, redo_list)
    obiecte = create(obiecte, 2, 'boo2', 'ge2', 80, 'none', undo_list, redo_list)
    obiecte = create(obiecte, 3, 'booo3', 'ge3', 10.9, 'silver', undo_list, redo_list)

    #10.redo nu face nimic
    obiecte = do_redo(undo_list, redo_list, obiecte)
    assert do_redo(undo_list, redo_list, obiecte) is None

    #11.doua undo-uri scot ultimele 2 obiecte
    obiecte = do_undo(undo_list, redo_list, obiecte)
    obiecte = do_undo(undo_list, redo_list, obiecte)
    assert len(obiecte) == 1

    # 12.redo anuleaza ultimul undo, daca ultima operatie e undo
    obiecte = do_redo(undo_list, redo_list, obiecte)
    assert len(obiecte) == 2

    #13.redo anuleaza si primul undo
    obiecte = do_redo(undo_list, redo_list, obiecte)
    assert do_redo(undo_list, redo_list, obiecte) is None

    #14.doua undo-uri scot ultimele 2 obiecte
    obiecte = do_undo(undo_list, redo_list, obiecte)
    obiecte = do_undo(undo_list, redo_list, obiecte)
    assert len(obiecte) == 1

    #15.adaugam un obiect
    obiecte = create(obiecte, 4, 'booo4', 'gen4', 121.77, 'silver', undo_list, redo_list)
    assert len(obiecte) == 2

    #16.redo nu face nimic, deoarece ultima operatie nu este un undo
    obiecte = do_redo(undo_list, redo_list, obiecte)

    #17.undo anuleaza adaugarea lui o4
    obiecte = do_undo(undo_list, redo_list, obiecte)
    assert len(obiecte) == 1

    #18.undo anuleaza adaugarea lui o1 - practic se continua sirul de undo de la pct 14
    obiecte = do_undo(undo_list, redo_list, obiecte)
    assert len(obiecte) == 0

    #19.se anuleaza ultimele 2 undo-uri
    obiecte = do_redo(undo_list, redo_list, obiecte)
    obiecte = do_redo(undo_list, redo_list, obiecte)

    #20.redo nu face nimic
    assert do_redo(undo_list, redo_list, obiecte) is None