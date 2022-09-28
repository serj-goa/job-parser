from classes import HH, Superjob
from parse_superjob import get_parse_superjob

from requests import get


def create_vacancies_ojects(vacancies_data):

    obj_vacancies = []

    for cls, vacancies_lst in vacancies_data:

        for vacancies in vacancies_lst:

            cls_obj = cls()
            cls_obj.get_request(vacancies)

            obj_vacancies.append(cls_obj)

    return obj_vacancies


def get_vacancies_by_api(text):

    all_vacancies = []

    for i in range(1, 7):

        params = {
            'text': text,
            'per_page': 100,
            'page': i
        }

        vacancies_items = get('https://api.hh.ru/vacancies', params=params).json()['items']

        for data in vacancies_items:
            vacancies_info = {
                'name': data['name'],
                'url': data['alternate_url'],
                'salary': data['salary'],
                'snippet': data['snippet']
            }
            all_vacancies.append(vacancies_info)

    return all_vacancies


def show_result(obj_vacancies: []) -> None:

    for obj in obj_vacancies[:100]:

        print(obj.name)
        print(obj.salary)
        print(obj.snippet)
        print(obj.url)
        print()


def main() -> None:

    print('Введите поисковый запрос')
    search_pattern = input('>>> ').strip()
    hh_vacancies = get_vacancies_by_api(text=search_pattern)
    sj_vacancies = get_parse_superjob(text=search_pattern)

    all_parse_vacancies = [sj_vacancies, hh_vacancies]
    all_cls = [Superjob, HH]

    vacancies_data = zip(all_cls, all_parse_vacancies)

    obj_vacancies = create_vacancies_ojects(vacancies_data)

    show_result(obj_vacancies)


if __name__ == '__main__':
    main()
