from src.vacancies_hh import VacanciesHH
from src.vacancy import Vacancy
from src.work_json import WorkJSON
from src.work_with_vacancies import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, \
    print_vacancies


def user_interaction():
    print("Добро пожаловать на платформу HeadHunter")
    search_query = input("Введите поисковой запрос: ")
    top_n = input("Введите количество вакансий для вывода в топ N: ")
    filter_word = input("Введите ключевое слово для фильтрации вакансий: ").lower()
    salary_range = input("Введите диапазон зарплат и валюту через \"-\" : ")

    hh_api = VacanciesHH()

    hh_vacancies = hh_api.get_vacancies(search_query)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    save_json = WorkJSON()
    save_json.add_vacancies(vacancies_list)
    save_json.del_vacancies()

    filtered_vacancies = filter_vacancies(vacancies_list, filter_word)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)

    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
