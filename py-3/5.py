class Circle:
    _pi = 3.14

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def pi(self):
        return self._pi

    def calculate_area(self):
        return self._pi * self._radius ** 2


class SemiCircle(Circle):
    def calculate_area(self):
        return super().calculate_area() / 2

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

# В дочернем классе SemiCircle, который наследуется от родительского класса
# Circle с методами:
# __init__(self, radius)
# radius(self) с декоратором property
# pi с декоратором property
# calculate_area, который считает площадь круга по формуле S=πR^2
# реализуйте метод calculate_area, который считает половину площади круга.
# Желательно, чтобы это было сделано через переиспользование метода calculate_area
# родительского класса.
# Входные данные
#
# semi_circle = SemiCircle(2)
# print(semi_circle.calculate_area())
# Выходные данные
#
# 6.28