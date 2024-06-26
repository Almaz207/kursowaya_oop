from abc import ABC, abstractmethod


class VacansyService(ABC):
    """Абстрактный класс для подключения к API сервиса с вакансиями"""

    # @abstractmethod
    # def __get_data(self, queri, salary, top):
    #     pass

    @abstractmethod
    def convert_vacansy(self, queri, salary, top):
        pass


class FailFiller(ABC):

    # @abstractmethod
    # def filling_file(self):
    #     pass

    @abstractmethod
    def filtr_vacancy(self):
        pass

    @abstractmethod
    def delet_data(self, number):
        pass
