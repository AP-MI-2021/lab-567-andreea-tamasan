import copy

from domain.cheltuiala import creeaza_cheltuiala, getId, get_nr_ap, get_suma, get_tipul, get_data
from Logic.CRUD import create, read, update, delete
from UserInterface.UserInterface import undo, redo
from Logic.Functionalitati import handle_value_date, handle_max_for_type, sort_for_sum, montly_sum_for_each_ap


def get_data():
        return [
                creeaza_cheltuiala(1, 1, 150, "12.05.2019", "alte cheltuieli"),
                creeaza_cheltuiala(2, 2, 300, "05.10.2011", "intretinere"),
                creeaza_cheltuiala(3, 3, 750, "11.06.1990", "intretinere"),
                creeaza_cheltuiala(4, 4, 500, "08.08.1999", "canal"),
                creeaza_cheltuiala(5, 5, 100, "10.01.2021", "intretinere"),
        ]


def test_create():
        list_cheltuieli = get_data()
        undoList = []
        redoList = []
        cheltuiala_noua = (6,6, 500, "17.10.2018", "intretinere")
        cheltuiala_nou = creeaza_cheltuiala(*cheltuiala_noua)
        list_cheltuieli_noi = create(list_cheltuieli, *cheltuiala_noua, undoList, redoList)

        assert len(list_cheltuieli_noi) == len(list_cheltuieli) + 1
        assert cheltuiala_nou in list_cheltuieli_noi


def test_read():
    list_cheltuieli = get_data()
    nr_ap = list_cheltuieli[2]
    cautare_cheltuiala = read(list_cheltuieli, get_nr_ap(nr_ap))
    for x in range(len(cautare_cheltuiala)-1):
            assert get_nr_ap(cautare_cheltuiala(x) == get_nr_ap(nr_ap))


def test_update():
        list_cheltuieli = get_data()
        undoList = []
        redoList = []
        cheltuiala_de_schimbat = (2,2, 250, "01.01.2020","intretinere")
        cheltuiala_noua = creeaza_cheltuiala(*cheltuiala_de_schimbat)
        new_list_cheltuieli = update(list_cheltuieli, cheltuiala_noua, undoList , redoList)
        assert len(new_list_cheltuieli) == len(list_cheltuieli)
        assert cheltuiala_noua not in list_cheltuieli
        assert cheltuiala_noua in new_list_cheltuieli


def test_delete():
        list_cheltuieli = get_data()
        undoList = []
        redoList = []
        nr_ap = 4
        cheltuiala_noua = None
        for c in [x for x in list_cheltuieli if nr_ap == get_nr_ap(x)]:
                cheltuiala_noua = c
        new_list_cheltuieli = delete(list_cheltuieli, nr_ap, undoList, redoList)
        assert len(new_list_cheltuieli) == len(list_cheltuieli) - 1
        assert cheltuiala_noua not in new_list_cheltuieli
        assert cheltuiala_noua in list_cheltuieli


def test_handle_delete_all():
        list_cheltuieli = get_data()
        undoList = []
        redoList = []
        nr_ap = 3
        cheltuiala_noua = None
        for c in [x for x in list_cheltuieli if nr_ap == get_nr_ap(x)]:
                cheltuiala_noua = c
        new_list_cheltuieli = delete(list_cheltuieli, nr_ap, undoList,redoList)
        assert len(new_list_cheltuieli) == len(list_cheltuieli) - 1
        assert cheltuiala_noua not in new_list_cheltuieli
        assert cheltuiala_noua in list_cheltuieli

def test_handle_value_date():
        list_cheltuieli = get_data()
        undoList = []
        redoList = []
        data = "05.10.2011"
        valoare = 150
        cheltuiala_noua = list_cheltuieli
        handle_value_date(list_cheltuieli,data,valoare, undoList, redoList)
        assert len(cheltuiala_noua) == len(list_cheltuieli)

def test_handle_max_for_type():
        list_cheltuieli = get_data()
        rezultat = handle_max_for_type(list_cheltuieli)
        assert len(rezultat) == 3
        assert rezultat["canal"] == 500.00
        assert rezultat["alte cheltuieli"] == 150.00
        assert rezultat["intretinere"] == 750.00

def test_sort_for_sum():
        cheltuieli = get_data()
        rezultat = sort_for_sum(cheltuieli)
        assert getId(rezultat[0]) == 3
        assert getId(rezultat[1]) == 4
        assert getId(rezultat[2]) == 2
        assert getId(rezultat[3]) == 1
        assert getId(rezultat[4]) == 5
        assert sort_for_sum(cheltuieli) == sorted(cheltuieli, key=get_suma, reverse = True)


def test_montly_sum_for_each_ap():
        cheltuieli = get_data()
        cheltuieli.append(creeaza_cheltuiala(77, 15, 300, "11.05.2021", "canal"))
        sum = montly_sum_for_each_ap(cheltuieli)
        assert sum["05 2021"][15] == 300

def test_undo_redo():
        cheltuieli = []
        undoList = []
        redoList = []
        cheltuieli = create(cheltuieli, 10, 7, 300, "05.02.2019", "alte cheltuieli", undoList,redoList)
        cheltuieli = create(cheltuieli, 11, 8, 550, "15.01.2020", "intretinere", undoList, redoList)
        cheltuieli = create(cheltuieli, 12, 9, 350, "01.12.2020", "canal", undoList,redoList)
        cheltuieli = undo(cheltuieli, undoList, redoList)
        assert len(cheltuieli) == 2
        assert getId(cheltuieli[0]) == 10
        assert getId(cheltuieli[1]) == 11
        cheltuieli = undo(cheltuieli,undoList,redoList)
        assert len(cheltuieli) == 1
        assert getId(cheltuieli[0]) == 10
        cheltuieli = undo(cheltuieli,undoList,redoList)
        assert cheltuieli == []
        cheltuieli = undo(cheltuieli, undoList, redoList)
        assert cheltuieli == []
        cheltuieli = create(cheltuieli, 10, 10, 300, "05.02.2019", "alte cheltuieli", undoList, redoList)
        cheltuieli = create(cheltuieli, 11, 11, 550, "15.01.2020", "canal", undoList, redoList)
        cheltuieli = create(cheltuieli, 12, 12, 350, "01.12.2020", "canal", undoList, redoList)
        cheltuieli_test = cheltuieli
        cheltuieli = redo(cheltuieli, redoList, undoList)
        assert cheltuieli_test == cheltuieli
        cheltuieli = undo(cheltuieli, undoList, redoList)
        assert len(cheltuieli) == 2
        assert getId(cheltuieli[0]) == 10
        assert getId(cheltuieli[1]) == 11
        cheltuieli = undo(cheltuieli, undoList, redoList)
        assert len(cheltuieli) == 1
        assert getId(cheltuieli[0]) == 10
        cheltuieli = create(cheltuieli, 14, 150, 220, "20.03.2002", "alte cheltuieli", undoList, redoList)
        cheltuieli_test = cheltuieli
        cheltuieli = redo(cheltuieli, redoList, undoList)
        assert cheltuieli_test == cheltuieli
        cheltuieli = undo(cheltuieli, undoList, redoList)
        assert len(cheltuieli) == 1
        assert getId(cheltuieli[0]) == 10
        cheltuieli = undo(cheltuieli, undoList, redoList)
        assert cheltuieli == []
        cheltuieli = redo(cheltuieli, redoList, undoList)
        assert len(cheltuieli) == 1
        assert getId(cheltuieli[0]) == 10
        cheltuieli = redo(cheltuieli, redoList, undoList)
        assert len(cheltuieli) == 2
        assert getId(cheltuieli[0]) == 10
        assert getId(cheltuieli[1]) == 14
        cheltuieli_test = copy.deepcopy(cheltuieli)
        cheltuieli = redo(cheltuieli, redoList, undoList)
        assert cheltuieli_test == cheltuieli


def test_all():
        test_create()
        test_read()
        test_update()
        test_delete()
        test_handle_delete_all()
        test_handle_value_date()
        test_handle_max_for_type()
        test_sort_for_sum()
        test_montly_sum_for_each_ap()
        test_undo_redo()

