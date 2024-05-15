from abc import ABC, abstractmethod


class Vacansy_service(ABC):
    """Абстрактный класс для подключения к API сервиса с вакансиями"""

    @abstractmethod
    def get_data(self, params):
        pass


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
