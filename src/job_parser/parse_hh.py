from classes import HH


def get_vacancies_by_api(text):

    hh = HH(user_text=text, url_api='https://api.hh.ru/vacancies')
    all_vacancies = []

    for i in range(1, 7):

        vacancies_items = hh.get_request(page_number=i).json()['items']

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
