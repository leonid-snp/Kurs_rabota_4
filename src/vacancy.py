import json
from abc import ABC, abstractmethod

import requests


class AbstractJobService(ABC):
    @abstractmethod
    def connect_to_api(self):
        pass

    @abstractmethod
    def get_jobs(self, params):
        pass


class HhJobService(AbstractJobService):
    """
    Класс реализует подключение к сервисам поиска вакансий

    :param url: (str) ссылка на API сервиса
    """
    def __init__(self, url: str) -> None:
        self.url = url

    def connect_to_api(self) -> int:
        """
        Функция реализует подключение к сервису hh.ru
        возвращает статус подключения к сервису

        :return: (int) статус подключения
        """
        response = requests.get(self.url)
        return response.status_code

    def get_jobs(self, params=None) -> str:
        """
        Функция возвращает вакансии сервиса hh.ru
        если параметр "params" не передан
        по умолчанию будет None

        :param params: (dict) параметры поиска вакансии (default None)
        :return: (str) файл json
        """
        response = requests.get(self.url)
        return json.dumps(response.json(), indent=4)
