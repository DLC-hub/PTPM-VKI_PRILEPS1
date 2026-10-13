class Controller:
    def __init__(self, calculator, db, ui, email_service):
        self.calculator = calculator
        self.db = db
        self.ui = ui
        self.email_service = email_service

    def process_triangle(self):
        a, b, c = self.ui.get_sides()
        record = self.db.get_record(a, b, c)

        if record is None:
            result = self.calculator.get_triangle_type(a, b, c)
            if result.startswith("Ошибка"):
                triangle_type = None
                error = result
            else:
                triangle_type = result
                error = None
            self.db.add_record(a, b, c, triangle_type, error)
        else:
            triangle_type, error = record

        if error:
            message = f"Ошибка: {error}"
        else:
            message = f"Тип треугольника: {triangle_type}"

        self.email_service.send_result(message)
        return message