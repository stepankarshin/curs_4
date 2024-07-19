from src.connectors import Connector, JsonConnector


def client_selection(connector: Connector):
    flag = True

    while flag == True:
        command = input("Что предпримите в погоне за мечтой???\n"
                        "0. Сдаться и выйти\n"
                        "1. Найти будущее место работы\n")
        if command == '0':
            return 'Очень жаль(((...'
        elif command == '1':
            count = int(input("Сколько вакансий хотите увидеть? "))
            vacancies = connector.get_vacancies()
            flag = False
            for vac in vacancies[:count]:
                print(vac.name, vac.url, vac.salary_currency, vac.salary_from, vac.salary_to)
        else:
            print("Такого действия пока нет, напомню вопрос:")
