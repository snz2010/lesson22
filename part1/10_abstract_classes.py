# Создайте абстрактный класс автомобиля Transport c абстрактными методами
# - start_engine - stop_engine - move - stop

# Унаследуйте от него три класса Boat, Car, Electroscooter
# для каждого из требуемых методов через print укажите какое-либо действие.

# Создайте класс Person у которого будет один единственный метод use_transport.
# В данный метод в качестве параметра должен передаваться объект реализующий интерфейс Transport
# Метод для этого объекта должен запускать двигатель, двигаться куда-то, тормозить и глушить двигатель.

from abc import ABC, abstractmethod


# интерфейс:класс Transport, должен быть унаследован от ABC
class Transport(ABC):
    # все методы Transport должны быть помечены декоратором @abstractmethod
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Классы Boat, Car, Electroscooter должны быть унаследованы от Transport
class Boat(Transport):
    def start_engine(self):
        print('Катер затарахтел')

    def stop_engine(self):
        print('Катер заглох')

    def move(self):
        print('Катер набирает скорость')

    def stop(self):
        print('Катер остановился')


class Car(Transport):
    def start_engine(self):
        print('Машина пустила мотор')

    def stop_engine(self):
        print('Машина заглушила двигатель')

    def move(self):
        print('Машина едет к цели')

    def stop(self):
        print('Машина остановилась')


class Electroscooter(Transport):
    def start_engine(self):
        print('Е-скутер включил свет')

    def stop_engine(self):
        print('Е-скутер выключил свет')

    def move(self):
        print('Е-скутер беззвучно мчит вперед')

    def stop(self):
        print('Е-скутер успешно остановился')


class Person:

    def use_transport(self, transport: Transport):
        transport.start_engine()
        transport.move()
        transport.stop()
        transport.stop_engine()


if __name__ == '__main__':
    boat = Boat()
    car = Car()
    es = Electroscooter()
    # экземпляр класса Person должен поочередно взаимодействовать с объектами Boat, Car, Electroscooter
    person = Person()
    person.use_transport(boat)
    print('=+' * 10)
    person.use_transport(car)
    print('+=' * 10)
    person.use_transport(es)
