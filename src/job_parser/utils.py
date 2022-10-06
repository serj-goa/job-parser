from classes import Vacancy


def create_vacancies_objects(vacancies_data):

    obj_vacancies = []

    for vacancies in vacancies_data:

        vacancy = Vacancy()
        vacancy.create_vacancy(vacancies)

        obj_vacancies.append(vacancy)

    return obj_vacancies


def save_vacancies(obj_vacancies: list) -> None:
    with open('vacancies.txt', 'w', encoding='utf-8') as fd:
        for vacancy in obj_vacancies:
            fd.write(f'{vacancy}\n\n')


def show_result(obj_vacancies: list) -> None:
    print()

    for obj in obj_vacancies[:100]:
        print(obj, end='\n\n')
