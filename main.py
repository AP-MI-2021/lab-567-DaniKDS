from Logic.crud import create
from Tests.tests import test_create, test_crud
from UserInterface.console import run_ui


def main():
    carti = []

    carti = create(carti, 1, "Mara", "drama", 10, "silver")
    carti = create(carti, 13, "Ion", "comedie", 99, "none")

    carti = run_ui(carti)

if __name__ == '__main__':
    test_crud()
    main()