from domain.cheltuiala import creeaza_cheltuiala, getId, get_nr_ap


def create(list_cheltuieli, id, nr_ap, suma, data, tipul, undoList, redoList):
    """
    Creeaza o cheltuiala.
    :param list_cheltuieli:lista initiala de cheltuieli
    :param id:id-ul listei
    :param nr_ap: nr. apartament
    :param suma: suma cheltuielii
    :param data: data cheltuielii
    :param tipul: tipul cheltuielii
    :return: o lista in care s-a adaugat o noua cheltuiala
    """
    cheltuiala = creeaza_cheltuiala(id, nr_ap, suma, data, tipul)
    rezultat = list_cheltuieli + [cheltuiala]
    undoList.append(list_cheltuieli)
    redoList.clear()
    return rezultat


def read(list_cheltuieli, nr_ap):
    """
    Verifica daca o cheltuiala cu un id dat se afla in lista de cheltuieli.
    :param list_cheltuieli: lista de cheltuieli
    :param nr_ap: nr. apartament al cheltuielii
    :return: cheltuiala cu nr. apartamentului sau toate daca nr. apartamentului nu este gasit
    """
    cheltuiala_cautata = []
    for cheltuiala in list_cheltuieli:
        if get_nr_ap(cheltuiala) == nr_ap:
            cheltuiala_cautata.append(cheltuiala)
    return cheltuiala_cautata


def update(list_cheltuieli, new_cheltuiala, undoList, redoList):
    """
    Modifica o cheltuiala cu un id dat.
    :param list_cheltuieli: lista de cheltuieli
    :param new_cheltuiala: o cheltuiala cu un id dat
    :return: lista noua obtinuta in urma modificarii
    """
    new_list_cheltuieli = []
    for cheltuiala in list_cheltuieli:
        if get_nr_ap(cheltuiala) != get_nr_ap(new_cheltuiala):
            new_list_cheltuieli.append(cheltuiala)
        elif get_nr_ap(cheltuiala) == get_nr_ap(new_cheltuiala) and getId(cheltuiala) != getId(new_cheltuiala):
            new_list_cheltuieli.append(cheltuiala)
        else:
            new_list_cheltuieli.append(new_cheltuiala)
    undoList.append(list_cheltuieli)
    redoList.clear()
    return new_list_cheltuieli


def delete(list_cheltuieli, nr_ap, undoList, redoList):
    """
    Sterge o cheltuiala a unui apartament.
    :param list_cheltuieli: lista de cheltuieli
    :param nr_ap: nr. apartamentului caruia dorim sa ii stergem cheltuiala
    :return: o lista din care s-a sters respectiva cheltuiala
    """
    new_list_cheltuieli = []
    for cheltuiala in list_cheltuieli:
        if get_nr_ap(cheltuiala) != nr_ap:
            new_list_cheltuieli.append(cheltuiala)
    undoList.append(list_cheltuieli)
    redoList.clear()
    return new_list_cheltuieli