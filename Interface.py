from tkinter import *
import tkinter.ttk as ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Functions import *
from Interpolation import *
from Method import *
import matplotlib.pyplot as plt

MaxCountOfDots = 250

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


class Root(Tk):
    def __init__(self):
        self.method = None
        super(Root, self).__init__()
        self.title("Лаборатоная работа 5")
        self.minsize(640, 400)
        nb = ttk.Notebook(self)
        self.answer_label = Label(self, text="Здесь появится ответ")
        self.answer_label.pack()
        validation = (self.register(self.on_validate), '%P')
        nb.pack(fill='both', expand='yes')
        child = ttk.Frame(self)
        method_label = Label(child, text="Метод Эйлера")
        method_label.pack()
        equation_label = Label(child, text="Выберите уравнение:")
        equation_label.pack()
        self.var = IntVar()
        self.var.set(0)
        equation1 = Radiobutton(child, text="sinx", variable=self.var, value=0)
        equation1.pack()
        equation2 = Radiobutton(child, text="5/(x^2+2)", variable=self.var, value=1)
        equation2.pack()
        equation3 = Radiobutton(child, text="sin(x) - y", variable=self.var, value=2)
        equation3.pack()
        equation4 = Radiobutton(child, text="x^2 + 2y", variable=self.var, value=3)
        equation4.pack()
        self.x0 = StringVar()
        x0_label = Label(child, text="Введите x0:")
        x0_label.pack()
        x0_entry = ttk.Entry(child, textvariable=self.x0, validate="key",  validatecommand=validation)
        x0_entry.pack()
        self.xn = StringVar()
        xn_label = Label(child, text="Введите xn:")
        xn_label.pack()
        xn_entry = ttk.Entry(child, textvariable=self.xn, validate="key",  validatecommand=validation)
        xn_entry.pack()
        self.y0 = StringVar()
        y0_label = Label(child, text="Введите y0:")
        y0_label.pack()
        y0_entry = ttk.Entry(child, textvariable=self.y0, validate="key",  validatecommand=validation)
        y0_entry.pack()
        self.accuracy = StringVar()
        accuracy_label = Label(child, text="Введите точность:")
        accuracy_label.pack()
        accuracy_entry = ttk.Entry(child, textvariable=self.accuracy, validate="key",  validatecommand=validation)
        accuracy_entry.pack()
        button = Button(child, text="Посчитать", command=self.do)
        button.pack()
        nb.add(child, text='Интерполяция')

    def on_validate(self, P):
        return is_digit(P)

    def do(self):
        if self.var.get() == 0:
            st = "sinx"
            function = f
        elif self.var.get() == 1:
            st = "5/(x^2+2)"
            function = g
        elif self.var.get() == 2:
            st = "sin(x) - y"
            function = z
        else:
            st = "x^2 + 2y"
            function = s
        euler_method = EulerMethod(float(self.x0.get()), float(self.y0.get()), float(self.accuracy.get()),
                                   float(self.xn.get()), function)
        array_with_dots = euler_method.solve_with_euler_method()
        plt.title("График")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        if len(array_with_dots) <= MaxCountOfDots:
            interpolation_method = Interpolation(float(self.x0.get()), float(self.xn.get()), array_with_dots)
            array = interpolation_method.get_dots_for_function()
            x = [array[i][0] for i in range(len(array))]
            y = [array[i][1] for i in range(len(array))]
        else:
            x = [array_with_dots[i][0] for i in range(len(array_with_dots))]
            y = [array_with_dots[i][1] for i in range(len(array_with_dots))]
        plt.plot(x, y, color='#008B8B', label='результат')

        if st == "sinx":
            value_of_function = []
            for i in range(len(x)):
                value_of_function.append(f_true(x[i]))
            plt.plot(x, value_of_function, color='blue', label="true")

        for i in range(len(array_with_dots)):
            plt.scatter(array_with_dots[i][0], array_with_dots[i][1], color='red', s=5, marker='o')
        plt.legend()
        plt.show()





root = Root()
root.mainloop()