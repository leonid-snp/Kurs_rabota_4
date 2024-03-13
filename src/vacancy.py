from src.currency_handler import get_currency_transfer


class Vacancy:
    def __init__(self, name, city, salary_from, salary_to, currency, requirements, link):
        self.name = name
        self.city = city

        if salary_from:
            self.salary_from = salary_from
        else:
            self.salary_from = 0

        if salary_to:
            self.salary_to = salary_to
        else:
            self.salary_to = 0

        self.currency = currency
        self.requirements = requirements
        self.link = link

    def __repr__(self):
        return (f"Название вакансии: {self.name}\n"
                f"Город: {self.city}\n"
                f"Заработная плата: {self.salary_from}-{self.salary_to} {self.currency}\n"
                f"Ссылка на вакансию: {self.link}\n\n")

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict, ...]) -> list[object, ...]:
        list_vacancies = []
        for el in vacancies:
            if el.get("salary"):
                list_vacancies.append(cls(el.get("name"),
                                          el.get("area").get("name"),
                                          el.get("salary").get("from"),
                                          el.get("salary").get("to"),
                                          get_currency_transfer(el.get("salary").get("currency")),
                                          el.get("snippet").get("requirement"),
                                          el.get("alternate_url")
                                          ))

            else:
                list_vacancies.append(cls(el.get("name"),
                                          el.get("area").get("name"),
                                          0,
                                          0,
                                          None,
                                          el.get("snippet").get("requirement"),
                                          el.get("alternate_url")
                                          ))

        return list_vacancies
