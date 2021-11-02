from Domain.cheltuiala import to_string_cheltuiala, creeaza_cheltuiala, get_nr_ap
from Logic.CRUD import create, read, update, delete
from Logic.Functionalitati import handle_delete_all, handle_value_date,handle_max_for_type


def show_menu():
    print("1. Deschideti CRUD.")
    print("2. Stergerea tuturor cheltuielilor pentru un apartament dat.")
    print("3. Adunarea unei valori la toate cheltuielile dintr-o data data.")
    print("4. Determinarea celei mai mari cheltuieli pentru fiecare tip. ")
    print("a. Afisare toate cheltuielile.")
    print("x. Iesire")

def show_CRUD_menu():
    print("1. Adaugare cheltuieli")
    print("2. Modificare cheltuieli")
    print("3. Stergere cheltuieli")
    print("a. Afisare toate cheltuielile")
    print("r. Revenire")

def handle_show_all(cheltuieli):
    for x in cheltuieli:
        print(to_string_cheltuiala(x))

def handle_add(cheltuieli):
    try:
        id = int(input("Introduceti id-ul cheltuielii: "))
        numar_ap = int(input("Dati numarul apartamentului: "))
        suma = int(input("Dati suma cheltuielii: "))
        data = input("Dati data cheltuielii: ")
        tipul = input("Dati tipul cheltuielii: ")
        return create(cheltuieli, id, numar_ap, suma, data, tipul)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuieli


def handle_update(cheltuiala):
    try:
        id = int(input("Introduceti id-ul cheltuielii: "))
        numar_ap = int(input("Dati numarul apartamentului: "))
        suma = int(input("Dati suma cheltuielii: "))
        data = input("Dati data cheltuielii: ")
        tipul = input("Dati tipul cheltuielii: ")
        new_cheltuiala = creeaza_cheltuiala(id, numar_ap, suma, data, tipul)
        return update(cheltuiala, new_cheltuiala)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuiala

def handle_cheltuieli_ap(cheltuiala, numar_ap):
    cheltuieli_ap = read(cheltuiala, numar_ap)
    for x in cheltuieli_ap:
        print(to_string_cheltuiala(x))

def handle_delete(cheltuiala):
    try:
        numar_ap = int(input("Dati numarul apartamentului care doriti sa il stergeti: "))
        handle_cheltuieli_ap(cheltuiala, numar_ap)
        return delete(cheltuiala, numar_ap)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return cheltuiala


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


def run_UI(cheltuieli):
    while True:
        show_menu()
        optiune = input("Dati optiune: ")
        if optiune == "1":
            cheltuieli = handle_CRUD(cheltuieli)
        elif optiune == "2":
            try:
                nr_ap = int(input("Introduceti numarul apartamentului pentru care doriti sa stergeti toate cheltuielile:"))
                cheltuieli = handle_delete_all(cheltuieli, nr_ap)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
                return cheltuieli
        elif optiune == "3":
            try:
                data = input("Introduceti data pentru care doriti sa adunati valoarea:")
                valoare = int(input("Dati valoarea care doriti sa o adaugati: "))
                cheltuieli = handle_value_date(cheltuieli, data, valoare)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
                return cheltuieli
        elif optiune == "4":
            rezultat = handle_max_for_type(cheltuieli)
            for tip in rezultat:
                print("Pentru cheltuiala de tip {} suma maxima este: {}".format(tip,rezultat[tip]))
        elif optiune == "a":
            handle_show_all(cheltuieli)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Va rog reincercati!")
    return cheltuieli