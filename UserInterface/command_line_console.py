from Logic.CRUD import create,delete
from Domain.cheltuiala import to_string_cheltuiala, get_nr_ap
from Logic.Functionalitati import handle_delete_all


def print_menu_new():
    print("add. Adaugare obiect id,numar_apartament,suma,data,tipul :canal, alta cheltuiala,intretinere")
    print("delete. Stergere obiect :numar_apartamen")
    print("showall. Afisare toate obiectele")
    print("exit")


def command_line_console(list):
    while True:
        print_menu_new()
        optiune = input("Dati comanda separate prin elementele prin ,")
        optiune = optiune.split(",")
        if optiune[0] == "add":
                id = optiune[1]
                nr_ap = optiune[2]
                suma = optiune[3]
                data = optiune[4]
                tipul = optiune[5]
                list = create( list,id,nr_ap,suma,data,tipul)
        elif optiune[0] == "delete":
                nr_ap = int(optiune[1])
                list = handle_delete_all(list, nr_ap)
        elif optiune[0] == "showall":
                for x in list:
                    print(to_string_cheltuiala(x))
        elif optiune[0] == "exit":
                    return list
        else:
                    print("Optiune gresita, va rog reincercati!")



