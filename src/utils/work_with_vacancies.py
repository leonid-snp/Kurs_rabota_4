def filter_vacancies(list_classes: list[object, ...], word: str) -> list[object, ...]:
    """
    Функция фильтрует список объектов по полученным словам из списка,
    если все слова из списка есть в объекте,
    добавляет объект в отфильтрованный список
    и возвращает отфильтрованный список объектов

    :param list_classes: (list[object, ...]) список объектов
    :param word: (str)
    :return: (list[object, ...]) отфильтрованный список объектов
    """
    list_filtered_classes = []
    for el in list_classes:
        if word in el.name.lower():
            list_filtered_classes.append(el)

    return list_filtered_classes


def get_vacancies_by_salary(list_classes: list[object, ...], salary_range: str)\
        -> list[object, ...] | str:
    """
    Функция сортирует список объектов по указанному диапазону зарплат,
    в случае если указанный диапазон не найден, возвращается сообщение пользователю
    о том что нужно указать другой диапазон

    :param list_classes: (list[object, ...) список объектов
    :param salary_range: (str) строковое отображение диапазона зарплат
    :return: (list[object, ...]) список отфильтрованных объектов по переданной зарплате
    """
    list_filtered_classes = []
    if salary_range:
        salary_from, salary_to, currency = salary_range.lower().split("-")
        for el in list_classes:
            if el.salary_from >= int(salary_from) and el.salary_to <= int(salary_to) and el.currency == currency:
                list_filtered_classes.append(el)
    else:
        return list_classes

    if len(list_filtered_classes) < 1:
        return f"По данному диапазону зарплат не найдено ни одного совпадения"
    else:
        return list_filtered_classes


def sort_vacancies(list_classes: list[object, ...] | object) -> list[object, ...] | object:
    """
    Функция сортирует список объектов по зарплате
    от большего к меньшему

    :param list_classes: (list[object, ...] | object) список объектов или объект
    :return: (list[object, ...] | object) список отсортированных объектов или объект
    """
    sorted_list = sorted(list_classes, reverse=True)
    return sorted_list


def get_top_vacancies(list_classes: list[object, ...] | object, top_n: str) -> list[object, ...] | object:
    """
    Функция сортирует список объектов по полученным параметрам
    в данном случае по количеству элементов которые нужно вернуть

    :param list_classes: (list[object, ...]) список объектов
    :param top_n: (str) количество объектов которые нужно вернуть
    :return: (list[object, ...] | object) список объектов
    """
    if top_n:
        return list_classes[:int(top_n)]
    else:
        return list_classes


def print_vacancies(list_classes: list[object, ...] | object) -> None:
    """
    Функция печатает список объектов

    :param list_classes: (list[object, ...]) список объектов
    """
    for elem in list_classes:
        print(elem)
