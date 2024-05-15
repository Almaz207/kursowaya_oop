from src.classes import HH_integration  # ,Converter_Vacansy
from pprint import pprint
from src.classes import Vacansy, vacancy_list, Rewriter_to_file\
#, dictionary_vacancy





def utitle():
    # queri = input("Введите поисковый запрос: ")
    # top = int(input("Введите количество вакансий для вывода в топ N: "))
    # salary= int(input("Введите желаемую зарплату: "))

    queri = "Python"
    top = 25
    salary = 600000

    params = {
        'page': 0,
        'text': queri,
        'area': '113',
        'salary': salary,
        'vacancy_search_order': 'salary_asc',
        'only_with_salary': True,
        'per_page': top
    }

    HH_integration().get_data(params)

    print(Rewriter_to_file(vacancy_list).filling_file())


if __name__ =="__main__":
    utitle()
