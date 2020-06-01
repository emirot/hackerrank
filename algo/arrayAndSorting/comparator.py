from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):

        pass
        # return "{} {}".format(self.name, str(self.score))
        
    def comparator(a, b):

        if a.score > b.score:
            return -1
        elif b.score > a.score:
            return 1
        elif b.score == a.score:
            if b.name < a.name:
                return 1
            else:
                return -1
        return -1
