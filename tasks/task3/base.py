class Figure:
    def area(self):
        pass

    def perimeter(self):
        pass

    def compare_area(self, other):
        if self.area() > other.area():
            return "БОЛЬШЕ"
        elif self.area() < other.area():
            return "МЕНЬШЕ"
        else:
            return "РАВНА"

    def compare_perimeter(self, other):
        if self.perimeter() > other.perimeter():
            return "БОЛЬШЕ"
        elif self.perimeter() < other.perimeter():
            return "МЕНЬШЕ"
        else:
            return "РАВЕН"
