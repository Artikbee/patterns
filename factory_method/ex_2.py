"""
Создайте паттерн "Фабричный метод" для управления различными видами уведомлений (email, SMS).
Базовый класс Notification должен содержать метод send, а классы-наследники EmailNotification и SMSNotification должны
реализовать этот метод. Создайте классы-фабрики для каждого типа уведомлений,
которые будут возвращать соответствующий объект уведомления.
"""
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, data):
        pass


class EmailNotification(Notification):
    def send(self, data):
        email = data['email']
        message = data['message']
        return f'{email} {message}'


class SMSNotification(Notification):
    def send(self, data):
        number = data['number']
        message = data['message']
        return f'{number} {message}'


class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self):
        pass

    def send_notification(self, data):
        notification = self.create_notification()
        return notification.send(data)


class EmailNotificationCreator(NotificationCreator):
    def create_notification(self):
        return EmailNotification()


class SMSNotificationCreator(NotificationCreator):
    def create_notification(self):
        return SMSNotification()


def client_code(creator: NotificationCreator, data):
    print(creator.send_notification(data))


data_email = {'email': 'abc@abc.ru', 'message': 'hello world'}
data_number = {'number': '4546', 'message': 'hello world'}

client_code(EmailNotificationCreator(), data_email)
client_code(SMSNotificationCreator(), data_number)
