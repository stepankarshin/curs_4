import pytest
from src.entities import Vacancy

def test_vacancy_salary_from_failed():
    with pytest.raises(ValueError, match='Зарплата должна быть положительным числом!'):
        Vacancy('test', 'test', 'RUR', -1, 0)

def test_vacancy_salary_to_failed():
    with pytest.raises(ValueError, match='Зарплата должна быть положительным числом!'):
        Vacancy('test', 'test', 'RUR', 0, -1)

def test_vacancy_salary_real_values_failed():
    with pytest.raises(ValueError, match='Максимум зарплаты должен быть больше минимума!'):
        Vacancy('test', 'test', 'RUR', 10, 2)

def test_vacancy_compare_salary_from():
    v1 = Vacancy('test', 'test', 'RUR', 10)
    v2 = Vacancy('test', 'test', 'RUR', 52)
    v3 = Vacancy('test', 'test', 'RUR', 52)
    assert v1 < v2
    assert v2 == v3
    assert v3 > v1

def test_vacancy_compare_salary_to():
    v1 = Vacancy('test', 'test', 'RUR', salary_to=34)
    v2 = Vacancy('test', 'test', 'RUR', salary_to=69)
    v3 = Vacancy('test', 'test', 'RUR', salary_to=69)
    assert v1 < v2
    assert v2 == v3
    assert v3 > v1

def test_vacancy_compare_salary_mixed():
    v1 = Vacancy('test', 'test', 'RUR', salary_to=34)
    v2 = Vacancy('test', 'test', 'RUR', 69)
    v3 = Vacancy('test', 'test', 'RUR', salary_to=69)
    v4 = Vacancy('test', 'test', 'RUR', 34)
    assert v1 < v2
    assert v2 == v3
    assert v3 > v4
