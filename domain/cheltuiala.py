from datetime import datetime

tipuri_permise = ["intretinere", "canal", "alte cheltuieli"]

def creeaza_cheltuiala(id, nr_ap, suma, data, tipul):
    """
        Creeaza o noua cheltuiala.
        :param id: id-ul cheltuielii - nr. intreg
        :param nr_apartament: nr. apartamentului cheltuielii - nr. intreg
        :param suma: suma cheltuita - nr. intreg
        :param data: data la care se adauga cheltuiala
        :param tipul: tipul cheltuielii ca string
        :return: o cheltuiala
    """
    if tipul not in tipuri_permise:
        raise ValueError(f"tipurile permise sunt:{tipuri_permise[0]}, {tipuri_permise[1]}, {tipuri_permise[2]}")
    cheltuiala = [id, nr_ap, suma, data, tipul]
    return cheltuiala


def getId(cheltuiala):
        """
        da id-ul unei cheltuieli
        :param cheltuiala: un dictionar de tip cheltuiala
        :return: id-ul cheltuielii
        """
        return cheltuiala[0]


def get_nr_ap(cheltuiala):
        """
        da numar apartamentului unei cheltuieli
        :param cheltuiala: un dictionar de tip cheltuiala
        :return: numarul apartamentului cheltuielii
        """
        return cheltuiala[1]


def get_suma(cheltuiala):
        """
        da suma unei cheltuieli
        :param cheltuiala: un dictionar de tip cheltuiala
        :return: valoarea sumei cheltuielii
        """
        return cheltuiala[2]


def get_data(cheltuiala):
    """
    da data unei chetuieli
    :param cheltuiala: un dictionar de tip cheltuiala
    :return: data cheltuielii
    """
    return cheltuiala[3]


def get_tipul(cheltuiala):
        """
        da tipul de cheltuiala
        :param cheltuiala: un dictionar de tip cheltuiala
        :return: tipul de cheltuiala
        """
        return cheltuiala[4]


def get_month(cheltuiala):
    list = get_data(cheltuiala).split(".")
    return list[1] + " " + list[2]

def to_string_cheltuiala(cheltuiala):
        """
        returneaza un dictionar cheltuiala
        :param cheltuiala: un dictionat de tip cheltuiala
        :return: cheltuiala sub forma de string
        """
        return "id: {}, nr_ap: {}, suma: {}, data: {}, tipul: {}".format(
            getId(cheltuiala),
            get_nr_ap(cheltuiala),
            get_suma(cheltuiala),
            get_data(cheltuiala),
            get_tipul(cheltuiala)
        )