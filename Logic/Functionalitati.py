from domain.cheltuiala import get_nr_ap, get_data, get_suma, get_tipul, get_month
from Logic.CRUD import delete

def handle_delete_all(cheltuieli, nr_ap, undoList, redoList):
    """
    Sterge cheltuiala a carei nr. de apartament este egal cu el dat .
    :cheltuieli: lista de cheltuieli
    :nr_ap: numar apartament
    return: o lista noua din care lipsesc cheltuielile a caror nr. de apartamnt este egal cu cel dat
    """
    for x in cheltuieli:
        if nr_ap == get_nr_ap(x):
            cheltuieli = delete(cheltuieli, get_nr_ap(x),undoList,redoList)
    return cheltuieli


def handle_value_date(cheltuieli, data, valoare, undoList, redoList):
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
    undoList.append(cheltuieli)
    redoList.clear()
    return cheltuieli

def handle_max_for_type(cheltuieli):
    """
    Calculeaza maximul sumei pentru fiecare tip de cheltuiala
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


def sort_for_sum(cheltuieli):
    """
    Sorteaza lista descrescator in functie de suma.
    :cheltuieli: lista de cheltuieli
    return: lista de cheltuieli sortata
    """
    return sorted(cheltuieli, key=get_suma, reverse=True)


def montly_sum_for_each_ap(cheltuieli):
    """
    Calculeaza suma lunara pentru fiecare apartament.
    :cheltuieli: o lista de cheltuieli
    return: un dictionar cu sumele lunare pentru fiecare apartament
    """
    sum = {}
    for cheltuiala in cheltuieli:
        luna = get_month(cheltuiala)
        nr_ap = get_nr_ap(cheltuiala)
        if luna not in sum:
            sum[luna] = {}
        if nr_ap in sum[luna]:
            sum[luna][nr_ap] += get_suma(cheltuiala)
        else:
            sum[luna][nr_ap] = get_suma(cheltuiala)
    return sum


