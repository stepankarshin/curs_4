class Vacancy:
    name: str
    url: str
    salary_currency: str
    salary_from: int | None = None
    salary_to: int | None = None

    def __init__(self, name, url, salary_currency, salary_from = None, salary_to = None):
        self.name = name
        self.url = url
        self.salary_currency = salary_currency

        self.salary_from = salary_from
        self.is_real(self.salary_from)

        self.salary_to = salary_to
        self.is_real(self.salary_to)

        self.pre_init(name, url, salary_from, salary_to)

        if self.salary_to is not None and self.salary_from is not None:
            if self.salary_to < self.salary_from:
                raise ValueError("Максимум зарплаты должен быть больше минимума!")

    @staticmethod
    def is_real(salary: int | None) -> None:
        if salary is not None and salary < 0:
            raise ValueError("Зарплата должна быть положительным числом!")

    @staticmethod
    def pre_init(name: str, url: str, salary_from: int | None, salary_to: int | None):
        if not name:
            raise Exception("У вакансии должно быть название!")
        elif not url:
            raise Exception("У вакансии должна быть ссылка!")
        elif not salary_from and not salary_to:
            raise Exception("У вакансии нет зарплаты(((")

    def __lt__(self, other: 'Vacancy'):

        if self.salary_from and other.salary_from:
            return self.salary_from < other.salary_from

        if self.salary_to and other.salary_to:
            return self.salary_to < other.salary_to

        self_salary = self.salary_from or self.salary_to
        other_salary = other.salary_from or other.salary_to
        return self_salary < other_salary


    def __eq__(self, other: 'Vacancy'):

        if self.salary_from and other.salary_from:
            return self.salary_from == other.salary_from

        if self.salary_to and other.salary_to:
            return self.salary_to == other.salary_to

        self_salary = self.salary_from or self.salary_to
        other_salary = other.salary_from or other.salary_to
        return self_salary == other_salary


    def __gt__(self, other: 'Vacancy'):

        if self.salary_from and other.salary_from:
            return self.salary_from > other.salary_from

        if self.salary_to and other.salary_to:
            return self.salary_to > other.salary_to

        self_salary = self.salary_from or self.salary_to
        other_salary = other.salary_from or other.salary_to
        return self_salary > other_salary
