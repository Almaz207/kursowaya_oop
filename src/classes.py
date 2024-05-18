import requests
import json
from src.abstract_classes import Vacansy_service, Fail_Filler

vacancy_list = []


class Vacansy():
    """Класс конструктор вакансии. Атрибуты : ID, название вакансии, зарплата, описание и ссылка на саму ваакансию"""
    def __init__(self, id, name, salary, responsibility, url_to_vacansy):
        self.id = id
        self.name = name
        self.salary = salary
        self.responsibility = responsibility
        self.url_to_vacansy = url_to_vacansy

    def __str__(self):
        return f'''НАЗВАНИЕ: {self.name}
ЗАРПЛАТА: {self.salary}
ТРЕБОВАНИЯ:{self.responsibility}
ССЫЛКА:{self.url_to_vacansy}
ID: {self.id}'''

    def __repr__(self):
        return f'''НАЗВАНИЕ: {self.name}
ЗАРПЛАТА: {self.salary}
ТРЕБОВАНИЯ:{self.responsibility}
ССЫЛКА:{self.url_to_vacansy}
# ID: {self.id}\n'''


class HH_integration(Vacansy_service):
    """Класс для подключения к API Hed Hunter и получения списка вакансий"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"


    def convert_vacansy(self, data):
        """Метод отсортировывает только необходимые данные: Название, Зарплату, Описание, Ссылкa на вакансию
        и добавляет экземпляр класса в список вакансий"""
        for item in data['items']:
            vacancy_list.append(Vacansy(id=item['id'],
                                        name=item['name'],
                                        salary=item['salary']['from'],
                                        responsibility=item['snippet']['responsibility'],
                                        url_to_vacansy=item['alternate_url']))


class Rewriter_to_file(Fail_Filler):
    """Класс для обработки вакансии"""

    def __init__(self, list_vacancy):
        self.list_vacancy = list_vacancy

    def filling_file(self):
        dictionary_vacancy = {}
        with open('vacancy.json', 'w', encoding='utf-8') as file:
            for element in self.list_vacancy:
                body_vacancy = {'Название вакансии': element.name, 'Зарплата': element.salary,
                                'Описание': element.responsibility, 'Ссылка': element.url_to_vacansy}
                dictionary_vacancy[element.id] = body_vacancy
            json.dump(dictionary_vacancy, file, ensure_ascii=False)
        return dictionary_vacancy
