class Figure():
    def __init__(self, color=None, type_figure=None):
        self.color = color
        self.type_figure = type_figure

    def get_color(self):
        return self.color

    def info(self):
        print(f'Фігура - {self.type_figure}, колір - {self.color}')


class Rectangle(Figure):
    def __init__(self, side=0, height=0):
        self.side = side
        self.height = height
        super().__init__('red', 'rectangle')

    def square(self):
        return self.side * self.height * 0.5


class Square(Figure):
    def __init__(self, wight=0, height=0):
        self.wight = wight
        self.height = height
        super().__init__('green', 'square')

    def square(self):
        return self.wight * self.height

sqr = Square(15, 25)
# sqr.color = 'red'
# sqr.type_figure = 'square'
sqr.info()
print(f'Square {sqr.type_figure} - {sqr.square()}')
rec = Rectangle(15, 25)
# rec.color = 'green'
# rec.type_figure = 'rectangle'
rec.info()
print(f'Square {rec.type_figure} - {rec.square()}')
