from classes import HH, Superjob
from parse_hh import get_vacancies_by_api
from parse_superjob import get_parse_superjob
from utils import create_vacancies_objects, show_result

from typing import List


def main() -> None:

    print('Введите поисковый запрос')
    search_pattern = input('>>> ').strip()

    hh_vacancies: List[dict] = get_vacancies_by_api(text=search_pattern)
    sj_vacancies: List[dict] = get_parse_superjob(text=search_pattern)

    all_parse_vacancies = [sj_vacancies, hh_vacancies]
    all_cls = [Superjob, HH]

    vacancies_data = zip(all_cls, all_parse_vacancies)  # List[Tuple[HH | Superjob, List]]

    obj_vacancies: List[HH | Superjob] = create_vacancies_objects(vacancies_data)

    show_result(obj_vacancies)


if __name__ == '__main__':
    main()
