
class mandelbrot(object):

    def __init__(self, iterations=50, cache=False):
        self.iterations = iterations
        self.cache = cache

    def calc_point(self, coordinate):
        z, iterinit = cache_retr(coordinate)
        # I sense that my future is full of grey hair and edge cases
        c = complex(coordinate)
        for iteration in xrange(iterinit, self.iterations):
            z = z**2 + c
            if z.real > 2: break

        self.cache_point(coordinate, iteration, z) #inb4 edge cases
        if iteration == self.iterations and z.real < 2:
            result = True
        else:
            result = False

        return result, iteration


    def cache_point(self, coordinate, iterations, value):
        pass


    # Properties

    @property
    def iterations(self):
        return self._iterations

    @iterations.setter
    def iterations(self, other):
        if not isinstance(other, int):
            raise TypeError
        self._iterations = other

    @property
    def cache(self):
        return self._cache

    @cache.setter
    def cache(self, other):
        if not isinstance(other, bool):
            raise TypeError
        self._cache = other