from src.api import HHVacancies
from src.entities import Vacancy
from src.connectors import JsonConnector
from src.client_selection import client_selection


api_client = HHVacancies()
connector = JsonConnector('./vacancies.json')

def main():
    print("Категорически вас приветствую!")
    text = input("Какая вакансия вас интересует? ")
    print("Получаем вакансии...")
    vacancies = api_client.get_vacancies(text)
    print("Вакансии получены!\nСохраняем в файл...")
    for vac in vacancies:
        connector.add_vacancy(vac)
    client_selection(connector)




if __name__ == "__main__":
    main()

