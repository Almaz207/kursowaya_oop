from src.classes import HHIntegration, Vacansy, vacancy_list, RewriterToFile
import os

# , dictionary_vacancy


def utitle():
    queri = input("Введите поисковый запрос: ")
    top = int(input("Введите количество вакансий для вывода в топ N: "))
    salary = int(input("Введите размер Зарплатной вилки: "))
    users_file_name = input("Введите название файла для сохранения данных: ")
    file_name = os.path.join("data", users_file_name + ".json")

    HHIntegration().convert_vacansy(queri, salary, top)

    print(RewriterToFile(vacancy_list, file_name).save_data())


if __name__ == "__main__":
    utitle()
