import abc


class Strategy(abc.ABC):
    name: str

    @abc.abstractmethod
    def plan(self, player):
        pass

    def to_string(self):
        return self.name
