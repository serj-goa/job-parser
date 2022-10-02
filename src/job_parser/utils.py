from classes import HH, Superjob

from typing import List


def create_vacancies_objects(vacancies_data: zip) -> List[HH | Superjob]:
    """
    Creates a list of objects for each vacancy.
    :param vacancies_data: list
    :return: List[HH | Superjob]
    """

    obj_vacancies = []

    for cls, vacancies_lst in vacancies_data:

        for vacancies in vacancies_lst:

            cls_obj = cls()
            cls_obj.get_request(vacancies)

            obj_vacancies.append(cls_obj)

    return obj_vacancies


def show_result(obj_vacancies: List[HH | Superjob]) -> None:
    """
    Displays the results of parsing vacancies to the user's screen.
    :param obj_vacancies: List[HH | Superjob]
    :return: None
    """
    print()

    for obj in obj_vacancies[:100]:
        print(obj, end='\n\n')
