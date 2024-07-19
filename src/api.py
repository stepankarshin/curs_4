from abc import ABC, abstractmethod
from src.entities import Vacancy
import requests


class BaseVacancies(ABC):

    @abstractmethod
    def get_vacancies(self, text: str) -> list[dict]:
        pass


class HHVacancies(BaseVacancies):

    def get_vacancies(self, text: str) -> list[Vacancy]:

        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': text,
            'only_with_salary': True
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        vacancies = data['items']
        return [
            Vacancy(
                name=item['name'],
                url=item['alternate_url'],
                salary_currency=item['salary']['currency'],
                salary_from=item['salary']['from'],
                salary_to=item['salary']['to']
            )
            for item in vacancies
        ]

