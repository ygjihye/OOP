import TrafficCondition as tc


class Updates(tc.TrafficCondition):
    def __init__(self, recentnews):
        self.__recentnews = recentnews

    def get_recentnews(self):
        return self.__recentnews

    def set_recentnews(self, recentnews):
        self.__recentnews = recentnews
