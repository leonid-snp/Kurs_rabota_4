import json

from src.work_with_file import WorkWithFile


class WorkJSON(WorkWithFile):
    """
    Класс для работы с JSON файлом
    """
    def add_vacancies(self, file: list[dict, ...]) -> None:
        """
        Функция принимает файл JSON и записывает в новый файл уже отфильтрованные данные

        :param file: (list) файл JSON
        """
        list_vacancies = []
        for el in file:
            vacancies = {
                "name": el.get("name"),
                "salary": el.get("salary"),
                "requirement": el.get("snippet").get("requirement"),
                "url": el.get("alternate_url")
            }
            list_vacancies.append(vacancies)

        with open("./data/hh_vacancies.json", "w") as f:
            json.dump(list_vacancies, f, ensure_ascii=False, indent=4)

    def print_vacancies(self) -> None:
        """
        Функция печатает файл JSON который есть в файле
        """
        with open("./data/hh_vacancies.json") as f:
            f = json.dumps(json.load(f), ensure_ascii=False, indent=4)
            print(f)

    def del_vacancies(self) -> None:
        """
        Функция удаляет содержимое файла JSON
        :return:
        """
        with open("./data/hh_vacancies.json", "w") as f:
            pass
