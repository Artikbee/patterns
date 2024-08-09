"""
Задача 1: Реализуйте паттерн "Фабричный метод" для создания различных видов документов (PDF, Word).
Создайте базовый класс Document, от которого будут наследоваться классы PDFDocument и WordDocument.
Затем создайте базовый класс DocumentCreator, от которого будут наследоваться конкретные
классы PDFCreator и WordCreator.
Фабричный метод должен создавать нужный тип документа в зависимости от ситуации.
"""
from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class WordDocument(Document):
    def create(self):
        return "WordDocument created"

    def delete(self):
        return "WordDocument deleted"


class PDFDocument(Document):
    def create(self):
        return "PDFDocument created"

    def delete(self):
        return "PDFDocument deleted"


class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self):
        pass

    def start_work(self):
        document = self.create_document()
        return document.create()

    def end_work(self):
        document = self.create_document()
        return document.delete()


class WordCreator(DocumentCreator):
    def create_document(self):
        return WordDocument()


class PDFCreator(DocumentCreator):
    def create_document(self):
        return PDFDocument()


def client_code(creator: DocumentCreator):
    print(creator.start_work())
    print(creator.end_work())


client_code(WordCreator())
client_code(PDFCreator())
