from Domain.cheltuiala import to_string_cheltuiala, creeaza_cheltuiala, get_nr_ap
from Logic.CRUD import create, read, update, delete


def show_menu():
    print("1. Deschideti CRUD.")
    """print("2. Stergerea tutror cheltuielilor pentru un apartament dat.")"""
    print("x. Iesire")

def show_CRUD_menu():
    print("1. Adaugare cheltuieli")
    print("2. Modificare cheltuieli")
    print("3. Stergere cheltuieli")
    print("a. Afisare toate cheltuielile")
    print("r. Revenire")

def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(to_string_cheltuiala(cheltuiala))

def handle_add(cheltuieli):
    id = int(input("Introduceti id-ul cheltuielii: "))
    numar_ap = int(input("Dati numarul apartamentului: "))
    suma = int(input("Dati suma cheltuielii: "))
    data = input("Dati data cheltuielii: ")
    tipul = input("Dati tipul cheltuielii: ")
    return create(cheltuieli, id, numar_ap, suma, data, tipul)

def handle_cheltuieli_ap(cheltuieli, nr_ap):
    """cheltuieli_ap = read(cheltuieli, nr_ap)
    for x in cheltuieli_ap:
        print(to_string_cheltuiala(x))
    for cheltuiala in cheltuieli:
        if get_nr_ap(cheltuiala) == nr_ap:
            print(cheltuiala)"""

def handle_update(cheltuiala):
    id = int(input("Introduceti id-ul cheltuielii: "))
    numar_ap = int(input("Dati numarul apartamentului: "))
    suma = int(input("Dati suma cheltuielii: "))
    data = input("Dati data cheltuielii: ")
    tipul = input("Dati tipul cheltuielii: ")
    new_cheltuiala = creeaza_cheltuiala(id, numar_ap, suma, data, tipul)
    return update(cheltuiala, new_cheltuiala)

def handle_delete(cheltuiala):
    numar_ap = int(input("Dati numarul apartamentului care doriti sa il stergeti: "))
    handle_cheltuieli_ap(cheltuiala, numar_ap)
    return delete(cheltuiala, numar_ap)


def handle_CRUD(cheltuieli):
    while True:
        show_CRUD_menu()
        optiune = input("Dati optiune: ")
        if optiune == "1":
            cheltuieli = handle_add(cheltuieli)
        elif optiune == "2":
            cheltuieli = handle_update(cheltuieli)
        elif optiune == "3":
            cheltuieli = handle_delete(cheltuieli)
        elif optiune == "a":
            handle_show_all(cheltuieli)
        elif optiune == "r":
            break
        else:
            print("Optiune gresita! Va rog reincercati!")
    return cheltuieli


def handle_delete_all(cheltuieli):
    nr_ap = int(input("Introduceti numarul apartamentului pentru care doriti sa stergeti toate cheltuielile: "))
    for x in cheltuieli:
        if nr_ap == get_nr_ap(x):
            cheltuieli = delete(cheltuieli, get_nr_ap(x))

def run_UI(cheltuieli):
    while True:
        show_menu()
        optiune = input("Dati optiune: ")
        if optiune == "1":
            cheltuieli = handle_CRUD(cheltuieli)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Va rog reincercati!")
    return cheltuieli