def add_to_class(Class):  # @save
    def wrapper(obj):
        setattr(Class, obj.__name__, obj)
    return wrapper


class A:
    def __init__(self):
        self.b = 1


a = A()


@add_to_class(A)
def do(self):
    print('Class attribute "b" is', self.b)
