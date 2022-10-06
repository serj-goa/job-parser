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

            salary = sanitize_salary(data['salary'])
            snippet = sanitize_snippet(data['snippet'])

            vacancies_info = {
                'name': data['name'],
                'url': data['alternate_url'],
                'salary': salary,
                'snippet': snippet
            }
            all_vacancies.append(vacancies_info)

    return all_vacancies


def sanitize_salary(data: dict or None) -> int:

    if data is None:
        salary = 0

    else:
        salary = data['from'] if data else 0

    return salary


def sanitize_snippet(data: dict or None) -> int:

    snippet = data['requirement']

    if snippet is None:
        snippet = 'нет данных'

    else:
        snippet = snippet.replace('<highlighttext>', '').replace('</highlighttext>', '')

    return snippet
