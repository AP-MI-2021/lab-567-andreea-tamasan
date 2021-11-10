from domain.cheltuiala import to_string_cheltuiala, creeaza_cheltuiala, get_nr_ap
from Logic.CRUD import create, read, update, delete
from Logic.Functionalitati import handle_delete_all, handle_value_date, handle_max_for_type, montly_sum_for_each_ap, \
    sort_for_sum
from UserInterface.command_line_console import command_line_console


def show_menu():
    print("1. Adaugare cheltuieli.")
    print("2. Modificare cheltuieli")
    print("3. Stergere cheltuieli")
    print("4. Stergerea tuturor cheltuielilor pentru un apartament dat.")
    print("5. Adunarea unei valori la toate cheltuielile dintr-o data data.")
    print("6. Determinarea celei mai mari cheltuieli pentru fiecare tip. ")
    print("7. Interfata noua")
    print("8. Ordonarea cheltuielilor descrescator dupa suma.")
    print("9. Afisarea sumelor lunare pentru fiecare apartament.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare toate cheltuielile.")
    print("x. Iesire")


def handle_show_all(cheltuieli):
    for x in cheltuieli:
        print(to_string_cheltuiala(x))

def handle_add(cheltuieli, undoList, redoList):
    """
    Adauga o cheltuiala in lista de cheltuieli.
    :param cheltuieli: lista de cheltuieli.
    return: lista noua de cheltuieli.
    """
    try:
        id = int(input("Introduceti id-ul cheltuielii: "))
        numar_ap = int(input("Dati numarul apartamentului: "))
        suma = int(input("Dati suma cheltuielii: "))
        data = input("Dati data cheltuielii: ")
        tipul = input("Dati tipul cheltuielii: ")
        return create(cheltuieli, id, numar_ap, suma, data, tipul,undoList, redoList)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


def handle_update(cheltuiala, undoList, redoList):
    """
    Modifica o cheltuiala.
    :param cheltuieli: lista de cheltuieli.
    :return: lista de cheltuieli dupa ce a fost modificata.
    """
    try:
        id = int(input("Introduceti id-ul cheltuielii: "))
        numar_ap = int(input("Dati numarul apartamentului: "))
        suma = int(input("Dati suma cheltuielii: "))
        data = input("Dati data cheltuielii de forma DD.MM.YYYY: ")
        tipul = input("Dati tipul cheltuielii: ")
        new_cheltuiala = creeaza_cheltuiala(id, numar_ap, suma, data, tipul)
        rezultat = update(cheltuiala, new_cheltuiala,undoList,redoList)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuiala

def handle_cheltuieli_ap(cheltuiala, numar_ap):
    cheltuieli_ap = read(cheltuiala, numar_ap)
    for x in cheltuieli_ap:
        print(to_string_cheltuiala(x))

def handle_delete(cheltuiala, undoList, redoList):
    """
    Sterge o cheltuiala dupa numarul de apartament.
    :param cheltuieli: lista cu cheltuieli.
    return: lista cu cheltuieli dupa stergerea cheltuielii
    """
    try:
        numar_ap = int(input("Dati numarul apartamentului care doriti sa il stergeti: "))
        handle_cheltuieli_ap(cheltuiala, numar_ap)
        return delete(cheltuiala, numar_ap, undoList, redoList)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuiala



def m_undo(cheltuieli, undoList, redoList):
    """
    Functia care face undo.
    :param cheltuieli: lista de cheltuieli
    :param undoList: istoricul listelor, inainte de fiecare modificare
    :param redoList: istoricul listelor, dupa operatia de undo
    return: in caz ca exista operatii de undo, returneaza lista dupa undo,
            in caz contrar, returneaza lista nemodificata
    """
    if undoList:
        redoList.append(cheltuieli)
        return undoList.pop()
    return cheltuieli

def m_redo(cheltuieli, redoList, undoList):
    """
    Functie de redo.
    :param cheltuieli: lista de cheltuieli.
    :param redoList: istoricul listelor, dupa operatia de undo.
    :param undoList: istoricul listelor, inainte de fiecare modificare.
    return: in caz ca exista operatii de redo, returneaza lista dupa redo,
            in caz contrar, returneaza lista nemodificata
    """
    if redoList:
        top_redo = redoList.pop()
        undoList.append(cheltuieli)
        return top_redo
    return cheltuieli

def undo(cheltuieli, redoList, undoList):
    undoList = m_undo(cheltuieli, redoList, undoList)
    if undoList is not None:
        return undoList
    return cheltuieli

def redo(cheltuieli, redoList, undoList):
    redoList= m_redo(cheltuieli, redoList, undoList)
    if redoList is not None:
        return redoList
    return cheltuieli


def handle_montly_sum_for_each_ap(cheltuieli):
    """
    Calculeaza suma maxima din o anumita luna.
    :cheltuieli: lista de cheltuieli
    return: cheltuielile in functie de luna
    """
    sums = montly_sum_for_each_ap(cheltuieli)
    for sum in montly_sum_for_each_ap(cheltuieli):
        print(f'Pentru luna si anul {sum} suma este: ')
        for nr_ap in sums[sum]:
            print(f'* pentru apartamentul {nr_ap} suma este {sums[sum][nr_ap]}')


def handle_sort_for_sum(cheltuieli):
    handle_show_all(sort_for_sum(cheltuieli))

def run_UI(cheltuieli):
    while True:
        undoList = []
        redoList = []
        show_menu()
        optiune = input("Dati optiune: ")
        if optiune == "1":
            cheltuieli = handle_add(cheltuieli, undoList, redoList)
        elif optiune == "2":
            cheltuieli = handle_update(cheltuieli,undoList, redoList)
        elif optiune == "3":
            cheltuieli = handle_delete(cheltuieli,undoList, redoList)
        elif optiune == "4":
            try:
                nr_ap = int(input("Introduceti numarul apartamentului pentru care doriti sa stergeti toate cheltuielile:"))
                cheltuieli = handle_delete_all(cheltuieli, nr_ap,undoList, redoList)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
                return cheltuieli
        elif optiune == "5":
            try:
                data = input("Introduceti data pentru care doriti sa adunati valoarea:")
                valoare = int(input("Dati valoarea care doriti sa o adaugati: "))
                cheltuieli = handle_value_date(cheltuieli, data, valoare,undoList, redoList)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
                return cheltuieli
        elif optiune == "6":
            rezultat = handle_max_for_type(cheltuieli)
            for tip in rezultat:
                print("Pentru cheltuiala de tip {} suma maxima este: {}".format(tip,rezultat[tip]))
        elif optiune == "7":
            command_line_console(cheltuieli)
        elif optiune == "8":
            handle_sort_for_sum(cheltuieli)
        elif optiune ==  "9":
            handle_montly_sum_for_each_ap(cheltuieli)
        elif optiune == "u":
            cheltuieli = undo(cheltuieli, undoList, redoList)
        elif optiune == "r":
            cheltuieli = redo(cheltuieli, undoList, redoList)
        elif optiune == "a":
            handle_show_all(cheltuieli)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Va rog reincercati!")
    return cheltuieli