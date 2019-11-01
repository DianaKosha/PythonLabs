class Rectangle:
        #Rectangle accepts two parameters and raises ValueError if at least one of them is < 0
        #get_area() returns rectangle area

    def __init__(self, side_a, side_b):
        if side_a < 0 or side_b < 0:
            raise ValueError("Side should be greater or equal 0")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

class Square(Rectangle):
        #Square accepts only one parameter and raises ValueError if this parameter is < 0
        #get_area() returns square area

    def __init__(self, side_a):
        if side_a < 0:
            raise ValueError("Side should be greater or equal 0")
        self.side_a = self.side_b = side_a

    def get_perimeter(self):
        return self.side_a * 4


class Triangle:
       #Triangle accepts three parameters and raises ValueError if at least one of them is < 0
       #get_area() returns triangle area
    def __init__(self, side_a, side_b, side_c):
        if side_a < 0 or side_b < 0 or side_c < 0:
            raise ValueError("Side should be greater or equal 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        return (self.side_a + self.side_b + self.side_c)/2

class Circle:
       #Circle accepts one parameter and raises ValueError if it is < 0
      # get_area() returns circle area
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius should be greater or equal 0")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


class Notifier:
    def notify(self):
        print("User successfully notified")


class AreaCalculator():
    def __init__(self, notifier):
        self.shapes_container = []
        self.notifier = notifier

    def add_shape(self, shape):
        self.shapes_container.append(shape)

    def calculate_area(self):
        for shape in self.shapes_container:
            print ("Area of {} is {}".format(type(shape).__name__, shape.get_area()))
            self.notifier.notify()

notifier = Notifier()

area_calc = AreaCalculator(notifier)
area_calc.add_shape(Square(5))
area_calc.add_shape(Rectangle(5, 6))
area_calc.add_shape(Triangle(5, 6, 7))
area_calc.add_shape(Circle(5))

area_calc.calculate_area()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
