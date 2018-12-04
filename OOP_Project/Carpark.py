class Carpark:
    def __init__(self, location, openinghours, pricing, lotsavail):
        self.__location = location
        self.__openinghours = openinghours
        self.__pricing = pricing
        self.__lotsavail = lotsavail

    def get_location(self):
        return self.__location

    def get_openinghours(self):
        return self.__openinghours

    def get_pricing(self):
        return self.__pricing

    def get_lotsavail(self):
        return self.__lotsavail

    def set_location(self, location):
        self.__location = location

    def set_openinghours(self, openinghours):
        self.__openinghours = openinghours

    def set_pricing(self, pricing):
        self.__pricing = pricing

    def set_lotsavail(self, lotsavail):
        self.__lotsavail = lotsavail
