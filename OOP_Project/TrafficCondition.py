import time;

class TrafficCondition:
    def __init__(self, location, mylocation, updated):
        self.__location = location
        self.__mylocation = mylocation
        self.__updated = updated


    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_mylocation(self):
        return self.__location

    def set_mylocation(self, mylocation):
        self.__mylocation = mylocation

    def get_updated(self):
        return self.__updated

    def set_updated(self, updated):
        self.__updated = updated




updated = time.asctime( time.localtime(time.time()) )
print(updated)
