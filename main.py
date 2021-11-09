from Logic.crud import create
from Tests.test_discount import test_discount
from Tests.test_min_price_for_gen import test_get_min_price_for_gen
from Tests.test_modifygen import organizare_teste
from Tests.test_ordonare_crescator_dupa_pret import test_ordonare_crecator_dupa_pret
from Tests.tests import test_create, test_crud
from UserInterface.console import run_ui
from UserInterface.command_line_console import run_command


def main():

    carti = []
    undo_list = []
    redo_list = []

    carti = create(carti, 1, "Mara", "poezie", 110.78, "silver" , undo_list , redo_list)
    carti = create(carti, 2, "Ion", "roman", 99.9, "gold", undo_list , redo_list)
    carti = create(carti, 3, "Rascoala", "nuvela", 193, "none", undo_list , redo_list)
    carti = create(carti, 4, "Lupta", "roman", 45, "silver", undo_list , redo_list)
    carti = create(carti, 5, "Husky", "poezie", 33.5, "none", undo_list , redo_list)
    carti = create(carti, 6, "Fire", "roman", 2400, "silver", undo_list , redo_list)
    carti = create(carti, 7, "Fox", "poezie", 18, "gold", undo_list , redo_list)

    print("1.Interfata cu meniu")
    print("2.Interfata cu comanda")

    var= input("Introduceti optiunea: ")
    if var == '1':
        carti = run_ui(carti,undo_list,redo_list)
    elif var == '2':
        carti = run_command(carti)
    else:
        print('Optiune invalida!')


if __name__ == '__main__':
    test_crud()
    test_discount()
    organizare_teste()
    test_ordonare_crecator_dupa_pret()
    main()