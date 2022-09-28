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
