from src.classes import HHIntegration, Vacansy, vacancy_list, RewriterToFile


# , dictionary_vacancy


def utitle():
    queri = input("Введите поисковый запрос: ")
    top = int(input("Введите количество вакансий для вывода в топ N: "))
    salary = int(input("Введите размер Зарплатной вилки: "))

    HHIntegration().convert_vacansy(queri, salary, top)

    print(RewriterToFile(vacancy_list).filling_file())


if __name__ == "__main__":
    utitle()
