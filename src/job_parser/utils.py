from classes import HH, Superjob


def create_vacancies_ojects(vacancies_data):

    obj_vacancies = []

    for cls, vacancies_lst in vacancies_data:

        for vacancies in vacancies_lst:

            cls_obj = cls()
            cls_obj.get_request(vacancies)

            obj_vacancies.append(cls_obj)

    return obj_vacancies


def show_result(obj_vacancies: []) -> None:
    print()

    for obj in obj_vacancies[:100]:
        print(obj, end='\n\n')
