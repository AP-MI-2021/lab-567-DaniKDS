def do_undo(undo_list:list, redo_list:list,current_list):
    """
    Aceasta functie va face o operatie de tip undo.
    :param undo_list:o lista ce retine lista de carti inainte de modificare
    :param redo_list:o lista ce retine lista de czrti dupa modificare
    :param current_list:lista de carti initiala
    :return:
    """
    if undo_list:
        top_undo = undo_list.pop()
        redo_list.append(current_list)
        return top_undo

    return None


def do_redo(undo_list:list , redo_list:list,current_list):
    """
    Aceasta functie va face o operatie de tip redo.
    :param undo_list:o lista ce retine lista de carti inainte de modificare
    :param redo_list:o lista ce retine lista de czrti dupa modificare
    :param current_list:lista de carti initiala
    :return:
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo

    return None

