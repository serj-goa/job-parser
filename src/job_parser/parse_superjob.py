from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests import get
from typing import List


user_agent = UserAgent()


def get_page_count(kw: str) -> int:
    """
    Gets the number of pages of jobs found.
    :param kw: str
    :return: int
    """

    data = get(
        url=f'https://russia.superjob.ru/vacancy/search/?keywords={kw}&page=1',
        headers={'user-agent': user_agent.random}
    )

    if data.status_code != 200:
        print('Your have a problem! (data.status_code)')

    soup = BeautifulSoup(data.content, 'lxml')

    try:
        page_count = int(soup.find('div', attrs={'class': '_8zbxf _9mI07 _1R63t _1D2vG _3YVWE b6N4- _19n5p'}).find_all('a', recursive=False)[-2].find('span').find('span').find('span').text)

    except AttributeError:
        page_count = 1

    except Exception as error:
        print(f'Your have a problem! (page_count = int())\n{error}')

    return page_count


def get_parse_superjob(text: str) -> List[dict]:
    """
    Gets the user's keyword, a list of dictionaries for each vacancy.
    :param text: str
    :return: List[dict]
    """

    page_count = get_page_count(kw=text)
    all_requests = get_requests(kw=text, page_count=page_count)
    vacancies_data = get_vacancies_data(links=all_requests)

    return vacancies_data


def get_requests(kw: str, page_count: int) -> list:
    """
    Gets all pages with found vacancies.
    :param kw: str
    :param page_count: int
    :return: list
    """
    all_requests = []

    for page in range(1, page_count + 1):

        try:
            data = get(
                url=f'https://russia.superjob.ru/vacancy/search/?keywords={kw}&page={page}',
                headers={'user-agent': user_agent.random}
            )

        except Exception as error:
            print(f'for page in range() error\n{error}')

        if data.status_code != 200:
            continue

        all_requests.append(data)

    return all_requests


def get_vacancies_data(links: List) -> List[dict]:
    """
    Gets data on vacancies.
    :param links: List
    :return: List[dict]
    """

    all_vacancies = []

    for link in links:
        soup = BeautifulSoup(link.text, 'lxml')

        vacancies = soup.find_all('span', attrs={'class': '_9fIP1 _249GZ _1jb_5 QLdOc'})
        salaries = soup.find_all('span', attrs={'class': '_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi'})
        snippets = soup.find_all('div', attrs={'class': '_2d_Of _2J-3z _3B5DQ'})

        for i in range(len(vacancies)):

            vacancie_info = {
                'name': vacancies[i].text,
                'url': f'https://russia.superjob.ru{vacancies[i].a["href"]}',
                'salary': salaries[i].text,
                'snippet': snippets[i].text
            }

            all_vacancies.append(vacancie_info)

    return all_vacancies
