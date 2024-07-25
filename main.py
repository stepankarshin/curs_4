from src.api import HHVacancies
from src.entities import Vacancy
from src.connectors import JsonConnector
from src.client_selection import client_selection
from src.utils import clear_json_file
import json


api_client = HHVacancies()
path = './vacancies.json'
connector = JsonConnector(path)

def main():
    print("Категорически вас приветствую!")
    text = input("Какая вакансия вас интересует? ")
    print("Получаем вакансии...")
    vacancies = api_client.get_vacancies(text)
    print("Вакансии получены!\nСохраняем в файл...")
    for vac in vacancies:
        connector.add_vacancy(vac)
    client_selection(connector)
    clear_json_file(path)





if __name__ == "__main__":
    main()

