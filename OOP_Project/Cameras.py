import TrafficCondition as tc


class Cameras(tc.TrafficCondition):
    def __init__(self, recentfootage):
        self.__recentfootage = recentfootage

    def get_recentfootage(self):
        return self.__recentfootage

    def set_recentfootage(self, recentfootage):
        self.__recentfootage = recentfootage
