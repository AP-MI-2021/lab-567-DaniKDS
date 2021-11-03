from Logic.crud import create
from Tests.tests import test_create, test_crud
from UserInterface.console import run_ui


def main():

    carti = []

    carti = create(carti, 1, "Mara", "drama", 110.78, "silver")
    carti = create(carti, 2, "Ion", "comedie", 99.9, "gold")
    carti = create(carti, 3, "Rascoala", "nuvela", 193, "none")
    carti = create(carti, 4, "Lupta", "romanta", 45, "silver")
    carti = create(carti, 5, "Husky", "idila", 33.5, "none")
    carti = create(carti, 6, "Fire", "roman", 2400, "silver")
    carti = create(carti, 7, "Fox", "poezie", 18, "gold")

    carti = run_ui(carti)

if __name__ == '__main__':
    test_crud()
    main()