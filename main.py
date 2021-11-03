from Logic.crud import create
from Tests.tests import test_create, test_crud
from UserInterface.console import run_ui
from UserInterface.command_line_console import run_command


def main():

    carti = []

    carti = create(carti, 1, "Mara", "drama", 110.78, "silver")
    carti = create(carti, 2, "Ion", "comedie", 99.9, "gold")
    carti = create(carti, 3, "Rascoala", "nuvela", 193, "none")
    carti = create(carti, 4, "Lupta", "romanta", 45, "silver")
    carti = create(carti, 5, "Husky", "idila", 33.5, "none")
    carti = create(carti, 6, "Fire", "roman", 2400, "silver")
    carti = create(carti, 7, "Fox", "poezie", 18, "gold")

    print("1.Interfata cu meniu")
    print("2.Interfata cu comanda")
    var= input("Introduceti optiunea: ")
    if var == '1':
        carti = run_ui(carti)
    elif var == '2':
        carti = run_command(carti)
    else:
        print('Optiune invalida!')



if __name__ == '__main__':
    test_crud()
    main()