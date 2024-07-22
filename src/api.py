from abc import ABC, abstractmethod
from src.entities import Vacancy
from src.utils import vac_maker
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
        return vac_maker(vacancies)
