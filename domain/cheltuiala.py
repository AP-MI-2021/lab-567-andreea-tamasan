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
    return {
        "id": int(id),
        "nr_ap": int(nr_ap),
        "suma": float(suma),
        "data": str(data),
        "tipul": str(tipul),
    }


def getId(cheltuiala):
        """
        da id-ul unei cheltuieli
        :param cheltuiala: un dictionar de tip cheltuiala
        :return: id-ul cheltuielii
        """
        return cheltuiala["id"]


def get_nr_ap(cheltuiala):
        """
        da numar apartamentului unei cheltuieli
        :param cheltuiala: un dictionar de tip cheltuiala
        :return: numarul apartamentului cheltuielii
        """
        return cheltuiala["nr_ap"]


def get_suma(cheltuiala):
        """
        da suma unei cheltuieli
        :param cheltuiala: un dictionar de tip cheltuiala
        :return: valoarea sumei cheltuielii
        """
        return cheltuiala["suma"]


def get_data(cheltuiala):
    """
    da data unei chetuieli
    :param cheltuiala: un dictionar de tip cheltuiala
    :return: data cheltuielii
    """
    return cheltuiala["data"]


def get_tipul(cheltuiala):
        """
        da tipul de cheltuiala
        :param cheltuiala: un dictionar de tip cheltuiala
        :return: tipul de cheltuiala
        """
        return cheltuiala["tipul"]


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