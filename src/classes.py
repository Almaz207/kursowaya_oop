import requests
import json
import os
from src.abstract_classes import VacansyService, FailFiller

vacancy_list = []


class Vacansy:
    """Класс конструктор вакансии. Атрибуты : ID, название вакансии, зарплата, описание и ссылка на саму ваакансию"""

    def __init__(self, id, name, salary_from, salary_to, responsibility, url_to_vacansy):
        self.id = id
        self.name = name
        self.salary_from = self._validate_salary(salary_from)
        self.salary_to = self._validate_salary(salary_to)
        self.responsibility = responsibility
        self.url_to_vacansy = url_to_vacansy

    @staticmethod
    def _validate_salary(salary):
        """Метод для валидации данных, если значение зарплаты указано(salary!=None), то возвращается указанное значение,
         если зарплата не указана, то возвращается 0 """

        return salary if salary != None else 0

    def __eq__(self, other):
        """Определяет наличие ключевых слов в описании вакансии"""

        for key in other:
            if key in self.responsibility:
                return True
        return False

    def __lt__(self, other):
        """Определяет, меньше ли минимальная зарплата текущей вакансии, чем у другой"""

        self_salary_from = self.salary_from if type(self.salary_from) is int else 0
        other_salary_from = other.salary_from if type(other.salary_from) is int else 0
        return self_salary_from < other_salary_from

    def __le__(self, other: str):
        """Определяет, меньше или равна максимальная зарплата текущей вакансии, чем у другой"""

        if self.salary_to is not int:
            return True
        return self.salary_to <= int(other)

    def __ge__(self, other: str) -> bool:
        """Определяет, больше или равна минимальная зарплата текущей вакансии, чем у другой"""

        if self.salary_from is not int:
            return True
        return self.salary_from >= int(other)

    def __str__(self):

        return f'''НАЗВАНИЕ: {self.name}
ЗАРПЛАТА: {self.salary_from} - {self.salary_to}
ТРЕБОВАНИЯ: {self.responsibility}
ССЫЛКА: {self.url_to_vacansy}
ID: {self.id}'''

    def __repr__(self):

        return f'''НАЗВАНИЕ: {self.name}
ЗАРПЛАТА: {self.salary_from} - {self.salary_to}
ТРЕБОВАНИЯ: {self.responsibility}
ССЫЛКА: {self.url_to_vacansy}
# ID: {self.id}\n'''


class HHIntegration(VacansyService):
    """Класс для подключения к API Hed Hunter и получения списка вакансий"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"

    def __get_data(self, queri, salary, top):
        """Метод позволяет получать данные с сайта через API"""
        parametr = {
            'page': 0,
            'text': queri,
            'area': '113',
            'salary': salary,
            'vacancy_search_order': 'salary_asc',
            'only_with_salary': True,
            'per_page': top
        }

        response = requests.get(url=self.__url, params=parametr)
        response.raise_for_status()
        return response.json()

    def convert_vacansy(self, queri, salary, top):
        """Метод отсортировывает только необходимые данные: Название, Зарплату, Описание, Ссылкa на вакансию
        и добавляет экземпляр класса в список вакансий"""
        data = self.__get_data(queri, salary, top)
        for item in data['items']:
            vacancy_list.append(Vacansy(id=item['id'],
                                        name=item['name'],
                                        salary_from=item['salary']['from'],
                                        salary_to=item['salary']['to'],
                                        responsibility=item['snippet']['responsibility'],
                                        url_to_vacansy=item['alternate_url']))


class RewriterToFile(FailFiller):
    """Класс для обработки вакансии"""

    def __init__(self, list_vacancy, file_name):
        self.list_vacancy = list_vacancy
        self.__file_name = file_name

    def filtr_vacancy(self):
        self.list_vacancy.sort(key=lambda vacancy: vacancy.salary_from, revers=False)

    def delet_data(self, number):
        for vacancy in vacancy_list:
            if vacancy.id == number:
                vacancy_list.remove(vacancy)
            return self.save_data()

    def save_data(self):
        dictionary_vacancy = {}
        os.makedirs('data', exist_ok=True)
        with open(self.__file_name, 'w', encoding='utf-8') as file:
            for element in self.list_vacancy:
                body_vacancy = {'Название вакансии': element.name, 'Зарплата от': element.salary_from,
                                'Зарплата до': element.salary_to,
                                'Описание': element.responsibility, 'Ссылка': element.url_to_vacansy}
                dictionary_vacancy[element.id] = body_vacancy
            json.dump(dictionary_vacancy, file, ensure_ascii=False)
            return dictionary_vacancy

    def load_data(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
