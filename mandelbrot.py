
class mandelbrot(object):

    def __init__(self, iterations=50, cache=False):
        self.iterations = iterations
        self._cache = cache

    def calc_point(self, coordinate):
        pass

    def cache(self, coordinate, iterations, value):
        pass