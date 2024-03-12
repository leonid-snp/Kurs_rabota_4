from src.vacancies_hh import VacanciesHH
from src.save_json import WorkJSON


hh = VacanciesHH()

save_json = WorkJSON()
save_json.add_vacancies(hh.get_vacancies())
save_json.del_vacancies()
