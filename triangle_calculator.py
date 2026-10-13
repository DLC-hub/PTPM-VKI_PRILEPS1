class TriangleCalculator:
    def get_triangle_type(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return "Ошибка: стороны должны быть положительными"
        if a + b <= c or a + c <= b or b + c <= a:
            return "Ошибка: треугольник не существует"

        if a == b == c:
            return "Равносторонний"
        elif a == b or a == c or b == c:
            return "Равнобедренный"
        else:
            return "Разносторонний"