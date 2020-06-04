import math


class Interpolation:
    def __init__(self, a, b, array_with_dots):
        self.count_of_dots = len(array_with_dots)
        self.array_with_dots = []
        self.a = a
        self.b = b
        self.array_with_dots = array_with_dots

    def lagrange(self, x):
        y = 0
        for i in range(self.count_of_dots):
            L = 1
            for j in range(self.count_of_dots):
                if j != i:
                    L *= (x-self.array_with_dots[j][0])/(self.array_with_dots[i][0] - self.array_with_dots[j][0])
            y += L*self.array_with_dots[i][1]
        return y

    def get_dots_for_function(self):
        i = self.a
        array_with_answer = []
        while i <= self.b:
            array_with_answer.append([i, self.lagrange(i)])
            i += 0.1
        return array_with_answer

