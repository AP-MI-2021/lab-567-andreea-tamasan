from Tests.Teste import test_all, get_data
from UserInterface.UserInterface import run_UI


def main():
    cheltuieli = get_data()
    cheltuieli = run_UI(cheltuieli)

if __name__=='__main__':
        test_all()
        main()
