from Domain.cheltuiala import get_nr_ap, get_data, get_suma, get_tipul
from Logic.CRUD import delete

def handle_delete_all(cheltuieli, nr_ap):
    """
    Sterge cheltuiala a carei nr. de apartament este egal cu el dat .
    :cheltuieli: lista de cheltuieli
    :nr_ap: numar apartament
    return: o lista noua din care lipsesc cheltuielile a caror nr. de apartamnt este egal cu cel dat
    """
    for x in cheltuieli:
        if nr_ap == get_nr_ap(x):
            cheltuieli = delete(cheltuieli, get_nr_ap(x))
    return cheltuieli


def handle_value_date(cheltuieli, data, valoare):
    """
    Aduna la cheltuiala dintr-o anumita data.
    :cheltuieli: lista de cheltuieli
    :data: data la care dorim sa adunam valoarea
    :valoarea: nr. pe care dorim sa il adunam cheltuielii
    return: lista initiala la care s-a adaugat o valoare sumei cheltuielii
    """
    for x in cheltuieli:
        if data == get_data(x):
            x[2] += valoare
    return cheltuieli

def handle_max_for_type(cheltuieli):
    """
    Calculeaza maximul sumei pentru fiecare tip de cheltuial
    :cheltuieli: lista de cheltuieli
    return: maximul pentru fiecare tip de cheltuila
    """
    rezultat = {}
    for x in cheltuieli:
        tip = get_tipul(x)
        suma = get_suma(x)
        if tip in rezultat:
            if suma > rezultat[tip]:
                rezultat[tip] = suma
        else:
            rezultat[tip] = suma
    return rezultat



