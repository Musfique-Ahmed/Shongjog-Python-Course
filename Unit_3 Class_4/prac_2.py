from abc import ABC, abstractmethod

class Applience(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Fan(Applience):
    def turn_on(self):
        print("The fan has turned on!")

class Tv(Applience):
    def turn_on(self):
        print("The Tv has turned on!")

fan  = Fan()
tv = Tv()

fan.turn_on()
tv.turn_on()