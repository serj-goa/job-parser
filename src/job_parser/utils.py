from classes import HH, Superjob


def create_vacancies_objects(vacancies_data):

    obj_vacancies = []

    for cls, vacancies_lst in vacancies_data:

        for vacancies in vacancies_lst:

            cls_obj = cls()
            cls_obj.get_request(vacancies)

            obj_vacancies.append(cls_obj)

    return obj_vacancies


def save_vacancies(obj_vacancies: list) -> None:
    with open('vacancies.txt', 'w', encoding='utf-8') as fd:
        for vacancy in obj_vacancies:
            fd.write(f'{vacancy}\n\n')


def show_result(obj_vacancies: list) -> None:
    print()

    for obj in obj_vacancies[:100]:
        print(obj, end='\n\n')
