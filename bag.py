try:
    # rdrand is a drop in replacement for random
    # that uses real randomness from the cpu
    # faster, and more random...
    from rdrand import Random
except ImportError:
    from random import Random
try:
    from _thread import get_ident
except ImportError:
    try:
        from thread import get_ident
    except ImportError:
        from dummy_thread import get_ident

RAND = Random()


def recursive_repr(fillvalue='...'):
    """Decorator to make a repr function return fillvalue for a recursive call

       Backport from python3
    """

    def decorating_function(user_function):
        repr_running = set()

        def wrapper(self):
            key = id(self), get_ident()
            if key in repr_running:
                return fillvalue
            repr_running.add(key)
            try:
                result = user_function(self)
            finally:
                repr_running.discard(key)
            return result

        return wrapper

    return decorating_function


class Bag(object):
    """
        A Bag is an unordered list.
        add puts something in
        pop removes and returns a random element.
    """

    def __init__(self, *args):
        """Intializes bad with all the initial args"""
        self.__bag = list(args)

    def pop(self):
        """remove and return an element of the ba"""
        rv = RAND.choice(self.__bag)
        self.__bag.remove(rv)
        return rv

    def add(self, element):
        """add an element to the bag"""
        self.__bag.append(element)
        return self

    def __add__(self, other):
        """+ will return the concatenation of 2 bags"""
        new_bag = Bag()
        new_bag.__bag = self.__bag + other.__bag
        return new_bag

    def __contains__(self, item):
        return item in self.__bag

    def __iter__(self):
        """Iterating over a bag empties it"""
        def iterover():
            while len(self) > 0:
                yield self.pop()

        """
            non destructive
        def iterover():
            temp = self.__bag[:]
            r.shuffle(temp)
            for i in temp:
                yield i
        """

        return iterover()

    def __len__(self):
        return len(self.__bag)

    @recursive_repr()
    def __repr__(self):
        """As a special side bonus, this function works with any container"""
        cl = str(self.__class__)[8:-2]
        ar = str(tuple(self.__bag))
        if ar.endswith(',)'):
            ar = ar[:-2] + ')'
        return cl + ar
