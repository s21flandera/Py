class Circle:
   pi = 3.14

   def calculate_area(self, radius):
       return pow(radius, 2) * self.pi

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

# Реализуйте метод calculate_area в классе “Circle”, в котором уже есть
# атрибут класса pi, который понадобится для расчета:
# Этот метод будет рассчитывать площадь круга по формуле S=πR^2, где R
# передается в качестве параметра
# Входные данные
#
# circle = Circle()
# print(circle.calculate_area(2))
# Выходные данные
#
# 12.56