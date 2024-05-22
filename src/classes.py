import requests
import json
from src.abstract_classes import VacansyService, FailFiller

vacancy_list = []


class Vacansy:
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
ТРЕБОВАНИЯ: {self.responsibility}
ССЫЛКА: {self.url_to_vacansy}
ID: {self.id}'''

    def __repr__(self):
        return f'''НАЗВАНИЕ: {self.name}
ЗАРПЛАТА: {self.salary}
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
        # if response.raise_for_status():
        #     print('Внимание: у данного пользователя отсутствуют права администратора.')
        return response.json()

    def convert_vacansy(self, queri, salary, top):
        """Метод отсортировывает только необходимые данные: Название, Зарплату, Описание, Ссылкa на вакансию
        и добавляет экземпляр класса в список вакансий"""
        # data = HHIntegration().__get_data(queri, salary, top)
        data = self.__get_data(queri, salary, top)
        for item in data['items']:
            vacancy_list.append(Vacansy(id=item['id'],
                                        name=item['name'],
                                        salary=item['salary']['from'],
                                        responsibility=item['snippet']['responsibility'],
                                        url_to_vacansy=item['alternate_url']))


class RewriterToFile(FailFiller):
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

    def edit_data(self):
        pass

    def delit_data(self):
        pass

    def _save_data(self,data):
        dictionary_vacancy = {}
        with open('vacancy.json', 'w', encoding='utf-8') as file:
            for element in self.list_vacancy:
                body_vacancy = {'Название вакансии': element.name, 'Зарплата': element.salary,
                                'Описание': element.responsibility, 'Ссылка': element.url_to_vacansy}
                dictionary_vacancy[element.id] = body_vacancy
            json.dump(dictionary_vacancy, file, ensure_ascii=False)