import abc


class Strategy(abc.ABC):
    name: str

    @abc.abstractmethod
    def pick(self, player):
        pass

    def to_string(self):
        return self.name
