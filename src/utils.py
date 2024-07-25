from src.entities import Vacancy
import json


def vac_maker(items: list[dict]) -> list[Vacancy]:
    lst = []
    for item in items:
        lst.append(Vacancy(
                name=item['name'],
                url=item['alternate_url'],
                salary_currency=item['salary']['currency'],
                salary_from=item['salary']['from'],
                salary_to=item['salary']['to']
            ))
    return lst


def clear_json_file(path: str):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(json.dumps([]))
