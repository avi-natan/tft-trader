# passive object
import numpy as np


class Board:
    def __init__(self):
        self.bench = np.array([None, None, None, None, None, None, None, None, None])
        self.field = np.array([None, None, None, None, None, None, None,
                               None, None, None, None, None, None, None,
                               None, None, None, None, None, None, None])

    def to_string(self):
        string_rep = """\n      Field:  {}""".format(self.field)
        string_rep += """\n      Bench:  {}\n""".format(self.bench)
        return string_rep