import logging
import math
import os
import sys

LOG_DIR = "Logs"
LOG_FILE = os.path.join(LOG_DIR, "file_txt.log")
EPS = 1e-9


def setup_logging():

    os.makedirs(LOG_DIR, exist_ok=True)

    log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        level=logging.DEBUG,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(LOG_FILE, encoding="utf-8")
        ]
    )

    logging.info("Логгер успешно сконфигурирован")
    logging.info("Приложение запущено")


def calculate_vertices(a: float, b: float, c: float):

    A = (0.0, 0.0)
    B = (c, 0.0)

    x = (b * b + c * c - a * a) / (2.0 * c)
    y = math.sqrt(max(0.0, b * b - x * x))
    C = (x, y)

    points = [A, B, C]

    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    width = max_x - min_x
    height = max_y - min_y

    if width <= EPS:
        width = 1.0
    if height <= EPS:
        height = 1.0

    padding = 10.0
    scale = min(
        (100.0 - 2 * padding) / width,
        (100.0 - 2 * padding) / height
    )

    offset_x = (100.0 - width * scale) / 2.0
    offset_y = (100.0 - height * scale) / 2.0

    result = []
    for px, py in points:
        X = int(round((px - min_x) * scale + offset_x))
        Y = int(round((max_y - py) * scale + offset_y))

        X = max(0, min(100, X))
        Y = max(0, min(100, Y))

        result.append((X, Y))

    return result


def compute_triangle(s1, s2, s3):

    logging.info("Параметры запроса: A=%r, B=%r, C=%r", s1, s2, s3)

    raw_sides = [s1, s2, s3]
    parsed = []


    for i, raw in enumerate(raw_sides, start=1):
        try:
            value = float(raw)
        except (ValueError, TypeError):
            logging.error("Невалидные данные: сторона %d = %r", i, raw)
            coords = [(-2, -2), (-2, -2), (-2, -2)]
            logging.error("Неуспешный запрос: координаты=%s", coords)
            return "", coords
        parsed.append(value)


    for i, value in enumerate(parsed, start=1):
        if not math.isfinite(value) or value <= 0:
            logging.error("Ошибочные числовые данные: сторона %d = %r", i, value)
            coords = [(-1, -1), (-1, -1), (-1, -1)]
            logging.error("Неуспешный запрос: координаты=%s", coords)
            return "не треугольник", coords

    a, b, c = parsed


    if not (a + b > c + EPS and a + c > b + EPS and b + c > a + EPS):
        coords = [(-1, -1), (-1, -1), (-1, -1)]
        logging.error("Не треугольник: не выполняется неравенство")
        return "не треугольник", coords


    if (math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9) and
            math.isclose(b, c, rel_tol=1e-9, abs_tol=1e-9)):
        triangle_type = "равносторонний"
    elif (math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9) or
          math.isclose(b, c, rel_tol=1e-9, abs_tol=1e-9) or
          math.isclose(a, c, rel_tol=1e-9, abs_tol=1e-9)):
        triangle_type = "равнобедренный"
    else:
        triangle_type = "разносторонний"

    coords = calculate_vertices(a, b, c)
    logging.info("Успешный запрос: тип=%s, координаты=%s", triangle_type, coords)
    return triangle_type, coords


def main():
    setup_logging()
    try:
        s1 = input("Введите сторону A: ")
        s2 = input("Введите сторону B: ")
        s3 = input("Введите сторону C: ")

        triangle_type, coords = compute_triangle(s1, s2, s3)

        print(triangle_type)
        print(coords)
        logging.info("Результат выдан: тип=%r, координаты=%r", triangle_type, coords)
    except Exception as e:
        logging.exception("Критическая ошибка: %s", e)
        print("")
        print([(-1, -1), (-1, -1), (-1, -1)])


if __name__ == "__main__":
    main()