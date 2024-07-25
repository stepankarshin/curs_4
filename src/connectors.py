from abc import ABC, abstractmethod
from src.entities import Vacancy
from pathlib import Path
import json


class Connector(ABC):
    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @staticmethod
    def _dict_to_class(data: dict) -> Vacancy:
        return Vacancy(**data)


class JsonConnector(Connector):

    def __init__(self, file_path: str | Path, encoding: str = 'utf-8', file_name: str = 'vacancies') -> None:
        self.__path = file_path
        self.encoding = encoding
        self.file_name = file_name

    def get_vacancies(self) -> list[Vacancy]:
        vacancies = []
        PATH = Path(self.__path)
        with open(self.__path, 'r', encoding=self.encoding) as file:
            if PATH.stat().st_size == 0:
                return []
            for item in json.load(file):
                vacancy = self._dict_to_class(item)
                vacancies.append(vacancy)
        return vacancies

    def add_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
            data = [vars(vac) for vac in vacancies]
            with open(self.__path, 'w', encoding=self.encoding) as file:
                file.write(json.dumps(data))

    def remove_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies()
        if vacancy in vacancies:
            vacancies.remove(vacancy)
            data = [vars(vac) for vac in vacancies]
            with open(self.__path, 'w', encoding=self.encoding) as file:
                json.dump(data, file)

