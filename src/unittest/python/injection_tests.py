import dependency_injector.providers as providers
import dependency_injector.containers as containers


class Engine(object):

    def go(self):
        return "I'm going."


class Car(object):

    def __init__(self, engine: Engine):
        self.engine = engine

    def go(self):
        print(self.engine.go())


class Injector(containers.DeclarativeContainer):

    engine = providers.Factory(Engine)

    car = providers.Factory(Car, engine)


my_car: Car = Injector.car()

my_car.go()
