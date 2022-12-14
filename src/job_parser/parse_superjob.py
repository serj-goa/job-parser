from classes import Superjob

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from re import sub


user_agent = UserAgent()


def get_page_count(kw: str) -> int:
    """
    Gets the number of pages for all found vacancies.
    :param kw: str
    :return: int
    """

    sj = Superjob(user_text=kw, url='https://russia.superjob.ru/vacancy/search/?')
    data = sj.get_request(page_number=1)

    if data.status_code != 200:
        print('Your have a problem!')

    soup = BeautifulSoup(data.content, 'lxml')

    try:
        page_count = int(
            soup.find('div', attrs={'class': '_8zbxf _9mI07 _1R63t _1D2vG _3YVWE b6N4- _19n5p'})
            .find_all('a', recursive=False)[-2].find('span').find('span').find('span').text)

    except AttributeError:
        page_count = 1

    except Exception as error:
        print(f'Your have a problem!\n{error}')

    return page_count


def get_parse_superjob(text: str) -> list:
    """
    Gets a list of all jobs for the specified keyword.
    :param text: str
    :return: list
    """

    page_count = get_page_count(kw=text)
    all_requests = get_requests(kw=text, page_count=page_count)
    vacancies_data = get_vacancies_data(links=all_requests)

    return vacancies_data


def get_requests(kw, page_count) -> list:
    """
    Gets a list of all pages with found vacancies.
    :param kw: str
    :param page_count: int
    :return: list
    """

    all_requests = []
    sj = Superjob(user_text=kw, url='https://russia.superjob.ru/vacancy/search/?')

    for page in range(1, page_count + 1):

        try:
            data = sj.get_request(page_number=page)

        except Exception as error:
            print(f'for page in range() error\n{error}')

        if data.status_code != 200:
            continue

        all_requests.append(data)

    return all_requests


def get_vacancies_data(links: list) -> list:
    """
    Gets data on vacancies.
    :param links: list
    :return: list
    """

    all_vacancies = []

    for link in links:
        soup = BeautifulSoup(link.text, 'lxml')

        vacancies = soup.find_all('span', attrs={'class': '_9fIP1 _249GZ _1jb_5 QLdOc'})
        salaries = soup.find_all('span', attrs={'class': '_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi'})
        snippets = soup.find_all('div', attrs={'class': '_2d_Of _2J-3z _3B5DQ'})

        for i in range(len(vacancies)):

            salary = sanitize_salary(salaries[i].text)

            vacancy_info = {
                'name': vacancies[i].text,
                'url': f'https://russia.superjob.ru{vacancies[i].a["href"]}',
                'salary': salary,
                'snippet': snippets[i].text
            }

            all_vacancies.append(vacancy_info)

    return all_vacancies


def sanitize_salary(salary: str) -> int:
    """
    Clears data from a field salary.
    param data: str
    :return: int
    """
    salary = sub(r"??????|??|??????|??????|??????.", "", salary)

    if salary == "???? ????????????????????????????":
        salary = '0'
    elif '???' in salary:
        salary = sub(r"???\d+", "", salary)

    return int(salary)
