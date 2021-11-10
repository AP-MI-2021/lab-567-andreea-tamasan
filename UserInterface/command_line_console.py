from Logic.CRUD import create,delete,update
from domain.cheltuiala import to_string_cheltuiala, get_nr_ap, creeaza_cheltuiala
from Logic.Functionalitati import handle_delete_all


def print_menu_new():
    print("add. Adaugare obiect id,numar_apartament,suma,data,tipul :canal, alta cheltuiala,intretinere")
    print("delete. Stergere obiect :numar_apartamen")
    print("showall. Afisare toate obiectele")
    print("exit")

def run_update(parametri, list, undoList, redoList):
    """
    Modifica o cheltuiala existenta.
    :param params: detaliile cheltuielii.
    :param cheltuieli: lista cu cheltuieli.
    return: lista noua dupa modificare.
    """
    try:
        id = parametri[0]
        nr_ap = parametri[1]
        suma = parametri[2]
        data = parametri[3]
        tipul = parametri[4]
        new_list = creeaza_cheltuiala(id, nr_ap, suma, data, tipul)
        return update(list, new_list, undoList,redoList)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return list


def command_line_console(list):
    while True:
        print_menu_new()
        undoList = []
        redoList = []
        optiune = input("Dati comanda separate prin elementele prin ,")
        optiune = optiune.split(",")
        if optiune[0] == "add":
            try:
                id = int(optiune[1])
            except ValueError as ve:
                print("Eroare: {}".format(ve))
                return list
            try:
                nr_ap = int(optiune[2])
            except ValueError as ve:
                print("Eroare: {}".format(ve))
                return list
            try:
                suma = optiune[3]
            except ValueError as ve:
                print("Eroare: {}".format(ve))
                return list
            try:
                    data = str(optiune[4])
            except ValueError as ve:
                    print("Eroare: {}".format(ve))
                    return list
            try:
                    tipul = str(optiune[5])
            except ValueError as ve:
                    print("Eroare: {}".format(ve))
                    return list
            try:
                list = create( list,id,nr_ap,suma,data,tipul,undoList,redoList)
            except ValueError as ve:
                    print("Eroare: {}".format(ve))
                    return list
        elif optiune[0] == "delete":
             try:
                nr_ap = int(optiune[1])
             except ValueError as ve:
                print("Eroare: {}".format(ve))
                return list
             list = handle_delete_all(list, nr_ap,undoList,redoList)
        elif optiune[0] == "update":
            list = run_update(optiune[1:],list,undoList, redoList)
        elif optiune[0] == "showall":
                for x in list:
                    print(to_string_cheltuiala(x))
        elif optiune[0] == "undo":
            if len(undoList) > 0:
                redoList.append(list)
                list = undoList.pop()
            else:
                print(" Nu se poate efectua undo. ")
        elif optiune[0] == "redo":
            if len(redoList) > 0:
                undoList.append(list)
                list = redoList.pop()
            else:
                print(" Nu se poate efctua redo. ")
        elif optiune[0] == "exit":
                    return list
        else:
                    print("Optiune gresita, va rog reincercati!")



