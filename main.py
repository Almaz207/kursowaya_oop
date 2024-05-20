from src.classes import HHIntegration, Vacansy, vacancy_list, RewriterToFile


# , dictionary_vacancy


def utitle():
    queri = input("Введите поисковый запрос: ")
    top = int(input("Введите количество вакансий для вывода в топ N: "))
    salary = int(input("Введите размер Зарплатной вилки: "))

    params = {
        'page': 0,
        'text': queri,
        'area': '113',
        'salary': salary,
        'vacancy_search_order': 'salary_asc',
        'only_with_salary': True,
        'per_page': top
    }

    HHIntegration()._convert_vacansy(params)

    print(RewriterToFile(vacancy_list).filling_file())


if __name__ == "__main__":
    utitle()
