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

    def get_vacancies(self, param: str) -> list:
        """
        Функция возвращает вакансии сервиса hh.ru
        если параметр "params" не передан
        по умолчанию будет None

        :param param: (str) Параметры поиска вакансий
        :return: (str) файл json
        """
        response = requests.get("https://api.hh.ru/vacancies", params={
            "text": param,
        })
        return response.json().get("items")
