from parse_hh import get_vacancies_by_api
from parse_superjob import get_parse_superjob
from utils import create_vacancies_objects, save_vacancies, show_result


def main() -> None:

    print('Введите поисковый запрос')
    search_pattern = input('>>> ').strip()

    hh_vacancies: list = get_vacancies_by_api(text=search_pattern)
    sj_vacancies: list = get_parse_superjob(text=search_pattern)

    all_parse_vacancies = sj_vacancies + hh_vacancies

    obj_vacancies = create_vacancies_objects(all_parse_vacancies)

    show_result(obj_vacancies)
    save_vacancies(obj_vacancies)


if __name__ == '__main__':
    main()
