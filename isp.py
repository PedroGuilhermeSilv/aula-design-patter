## Exemplo ruim

from abc import ABC, abstractmethod


class MultiFunctionDevice(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

    @abstractmethod
    def scan_document(self, document):
        pass

    @abstractmethod
    def fax_document(self, document):
        pass


## Exemplo bom


class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass


class MultiFunctionDevice(Printer):
    def print_document(self, document):
        return super().print_document(document)

