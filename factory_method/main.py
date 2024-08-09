from abc import ABC, abstractmethod


# Интерфейс/Суперкласс
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


# Подкласс
class Truck(Transport):
    def deliver(self):
        return "Delivering by land in a box."


# Подкласс
class Ship(Transport):
    def deliver(self):
        return "Delivering by sea in a container."


# Базовый класс создателя (Фабрика)
class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        return transport.deliver()


# Возвращает truck()
class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()


# Возвращает ship()
class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


def client_code(logistics: Logistics):
    print(logistics.plan_delivery())


# Пример использования
if __name__ == "__main__":
    print("App: Launched with the RoadLogistics.")
    client_code(RoadLogistics())

    print("\nApp: Launched with the SeaLogistics.")
    client_code(SeaLogistics())
