class Figure:
    area = 0
    perimeter = 0
    angles = 0
    height = 0
    width = 0
    radius = 0
    square_side = 0
    triangle_side1 = 0
    triangle_side2 = 0
    triangle_side3 = 0

    def add_area(self, figure):
        """Считает и возвращает сумму площадей фигуры и переданной в функцию фигуры"""
        if not isinstance(figure, Figure):
            print("Передан неправильный класс")
        else:
            return int(figure.area + self.area)

    def count_perimeter(self):
        """Считает периметр фигуры в зависимости от инстанса объекта"""
        if isinstance(self, Rectangle):
            self.perimeter = int(2 * self.height + 2 * self.width)
        elif isinstance(self, Square):
            self.perimeter = int(self.square_side * 4)
        elif isinstance(self, Circle):
            self.perimeter = int(self.radius * 2 * 3.14)
        else:
            self.perimeter = int(self.triangle_side1 + self.triangle_side2 + self.triangle_side3)

    def count_area(self):
        """Считает площадь фигуры в завсимости от инстанса объекта"""
        if isinstance(self, Rectangle):
            self.area = int(self.height * self.width)
        elif isinstance(self, Square):
            self.area = self.square_side ** 2
        elif isinstance(self, Circle):
            self.area = int(self.radius ** 2 * 3.14)
        else:
            self.area = int(((self.perimeter / 2 - self.triangle_side1) * (self.perimeter / 2 - self.triangle_side2) * (
                    self.perimeter / 2 - self.triangle_side3) * self.perimeter / 2) ** 0.5)
            return self.area

    def count_angles(self):
        """Считает углы фигуры в зависимости от инстанса объекта"""
        if isinstance(self, Rectangle):
            self.angles = 4
        elif isinstance(self, Square):
            self.angles = 4
        elif isinstance(self, Circle):
            self.angles = 0
        else:
            self.angles = 3


class Rectangle(Figure):

    def __init__(self, name, height, width):
        self.height = height
        self.width = width
        self.name = name


class Square(Figure):

    def __init__(self, name, side):
        self.name = name
        self.square_side = side


class Circle(Figure):

    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


class Triangle(Figure):

    def __init__(self, name, triangle_side1, triangle_side2, triangle_side3):
        self.name = name
        self.triangle_side1 = triangle_side1
        self.triangle_side2 = triangle_side2
        self.triangle_side3 = triangle_side3
