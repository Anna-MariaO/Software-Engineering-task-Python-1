from square import Square
from rectangle import Rectangle
from triangle import Triangle
from circle import Circle



square = Square(12)
rectangle = Rectangle(3, 5)
triangle = Triangle(3, 4, 5)
circle = Circle(5)


print(f'Площадь квадрата: {square.area()}')
print(f'Периметр квадрата: {square.perimeter()}\n')

print(f'Площадь прямоугольника: {rectangle.area()}')
print(f'Периметр прямоугольника: {rectangle.perimeter()}\n')

print(f'Площадь треугольника: {triangle.area()}')
print(f'Периметр треугольника: {triangle.perimeter()}\n')

print(f'Площадь круга: {circle.area()}')
print(f'Периметр круга: {circle.perimeter()}\n')

print(f'Сравнение площади квадрата и круга: площадь квадрата {square.compare_area(circle)} площади круга')
print(f'Сравнение периметра квадрата и круга: периметр квадрата {square.compare_perimeter(circle)} периметра круга')

