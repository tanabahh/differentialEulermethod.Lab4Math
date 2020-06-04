class EulerMethod:
    def __init__(self, x0, y0, accuracy, xn, function):
        self.x = x0
        self.y = y0
        self.accuracy = accuracy
        self.n = int((xn - x0)/accuracy)
        self.function = function

    def solve_with_euler_method(self):
        array_with_dots = [[self.x, self.y]]
        for i in range(self.n):
            self.x += self.accuracy
            self.y += self.accuracy*self.function(self.x, self.y)
            array_with_dots.append([self.x, self.y])
        return array_with_dots
