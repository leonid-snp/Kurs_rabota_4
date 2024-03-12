import json
import requests

from src.work_with_api_service import WorkWithAPIService


class VacanciesHH(WorkWithAPIService):
    """
    Класс реализует подключение к сервисам поиска вакансий
    """

    def connect_to_api(self) -> int:
        """
        Функция реализует подключение к сервису hh.ru
        возвращает статус подключения к сервису

        :return: (int) статус подключения
        """
        response = requests.get("https://api.hh.ru/vacancies")
        return response.status_code

    def get_vacancies(self) -> list:
        """
        Функция возвращает вакансии сервиса hh.ru
        если параметр "params" не передан
        по умолчанию будет None

        :return: (str) файл json
        """
        response = requests.get("https://api.hh.ru/vacancies", params={
            "text": "python developer",
            "area": 1,
            "per_page": 2
        })
        return response.json().get("items")
