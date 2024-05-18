import requests
from abc import ABC, abstractmethod


class Vacansy_service(ABC):
    """Абстрактный класс для подключения к API сервиса с вакансиями"""


    def get_data(self, params):
        """Метод позволяет получать данные с саййта HH через API"""
        response = requests.get(url=self.url, params=params)
        return self.convert_vacansy(response.json())


class Fail_Filler(ABC):

    @abstractmethod
    def filling_file(self):
        pass

    # @abstractmethod
    # def edit_data(self):
    #     pass
    #
    # @abstractmethod
    # def delit_data(self):
    #     pass
