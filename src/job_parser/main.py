from classes import HH, Superjob

from requests import get


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

    for obj in obj_vacancies[:5]:

        print(obj.name)
        print(obj.salary)
        print(obj.snippet)
        print(obj.url)
        print()


def main() -> None:

    print('Введите поисковый запрос')
    search_pattern = input('>>> ').strip()
    hh_vacancies = get_vacancies_by_api(text=search_pattern)

    obj_vacancies = []

    for vacancies in hh_vacancies:

        hh = HH()
        hh.get_request(vacancies)

        obj_vacancies.append(hh)


    show_result(obj_vacancies)


if __name__ == '__main__':
    main()


"""
'name' - название вакансии (str)
'alternate_url' - ссылка на вакансию (str)
'salary' - зарплата (dict) - salary['from']
'snippet' - описание (dict)
"""
