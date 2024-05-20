from abc import ABC, abstractmethod


class VacansyService(ABC):
    """Абстрактный класс для подключения к API сервиса с вакансиями"""

    @abstractmethod
    def __get_data(self, parametr):
        pass

    @abstractmethod
    def _convert_vacansy(self, params):
        pass


class FailFiller(ABC):

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
