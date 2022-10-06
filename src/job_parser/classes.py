from abc import ABC, abstractmethod
from fake_useragent import UserAgent
from requests import get


class Engine(ABC):
    @abstractmethod
    def get_request(self, values):
        pass


class HH(Engine):
    """
    Works with requests for HadHunter.
    """
    def __init__(self, user_text, url_api):
        self.user_text = user_text
        self.per_page = 100
        self.url_api = url_api

    def get_request(self, page_number):

        params = {
            'text': self.user_text,
            'per_page': self.per_page,
            'page': page_number
        }

        return get(self.url_api, params=params)


class Superjob(Engine):
    """
    Works with requests for Superjob.
    """
    def __init__(self, user_text, url):
        self.user_text = user_text
        self.url = url

    def get_request(self, page_number):

        user_agent = UserAgent()

        return get(
            url=f'{self.url}keywords={self.user_text}&page={page_number}',
            headers={'user-agent': user_agent.random}
        )


class Vacancy:
    """
    Keeps a vacancy card.
    """
    def __init__(self):
        self.name = None
        self.salary = None
        self.snippet = None
        self.url = None

    def __repr__(self):
        return f'{self.name}\n{self.salary}\n{self.snippet}\n{self.url}'

    def create_vacancy(self, values):

        self.name = values['name']
        self.salary = values['salary']
        self.snippet = values['snippet']
        self.url = values['url']
