from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def get_request(self, values):
        pass


class HH(Engine):
    def __init__(self):
        self._name = None
        self._salary = None
        self._snippet = None
        self._url = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value['from'] if value else 'ЗП не указана'

    @property
    def snippet(self):
        return self._snippet

    @snippet.setter
    def snippet(self, value):

        snippet = value['requirement']

        if snippet is None:
            snippet = 'нет данных'

        else:
            snippet = snippet.replace('<highlighttext>', '').replace('</highlighttext>', '')

        self._snippet = snippet

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def get_request(self, values):

        self.name = values['name']
        self.salary = values['salary']
        self.snippet = values['snippet']
        self.url = values['url']


class Superjob(Engine):
    def __init__(self):
        self._name = None
        self._salary = None
        self._snippet = None
        self._url = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):

        # value = value.replace('до\\xa0', '').replace('\\xa0', '')

        self._salary = value

    @property
    def snippet(self):
        return self._snippet

    @snippet.setter
    def snippet(self, value):
        self._snippet = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def get_request(self, values):

        self.name = values['name']
        self.salary = values['salary']
        self.snippet = values['snippet']
        self.url = values['url']
