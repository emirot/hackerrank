__author__ = 'nolanemirot'


class MinimumStack():

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.first = True
        self.min_val = None

    def add_to_stack(self, value):
        if self.first:
            self.min_val = value
            self.first = False

        if value < self.min_val:
            self.min_val = value

        self.min_stack.insert(0, self.min_val)
        self.stack.insert(0, value)


    def pop_from_stack(self):
        self.min_stack.pop(0)
        self.stack.pop(0)

    def get_min_val(self):
        return self.min_stack[0]


    def print_stack(self):
        print("stack",self.stack)
        print("min stack",self.min_stack)



if __name__ == '__main__':
    min_stack = MinimumStack()
    min_stack.add_to_stack(12)
    min_stack.add_to_stack(16)
    min_stack.add_to_stack(20)
    min_stack.add_to_stack(17)
    min_stack.add_to_stack(11)

    min_stack.print_stack()
    min_stack.pop_from_stack()
    min_stack.print_stack()