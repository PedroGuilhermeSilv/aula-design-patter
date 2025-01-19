## Exemplo ruim


class MySQLDatabase:
    def connect(self):
        print("Conectando ao MySQL.")


class Application:
    def __init__(self):
        self.db = MySQLDatabase()

    def start(self):
        self.db.connect()


## Exemplo Bom

from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self): ...


class MySQLDatabase(Database):
    def connect(self):
        print("Conectando ao MySQL.")


class Application:
    def __init__(self, db: Database):
        self.db = db

    def start(self):
        self.db.connect()
