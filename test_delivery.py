import unittest
import datetime
from delivery import calculate_delivery_cost


class TestDelivery(unittest.TestCase):

    def test_base_cost(self):
        """Базовый расчет стоимости"""
        cost, _ = calculate_delivery_cost(2, 100, "обычный")
        # 200 + 100*5 = 700
        self.assertEqual(cost, 700)

    def test_weight_surcharge_medium(self):
        """Надбавка за вес > 5 и < 20 кг"""
        cost, _ = calculate_delivery_cost(10, 100, "обычный")
        # (200 + 100*5) * 1.2 = 840
        self.assertEqual(cost, 840)

    def test_weight_surcharge_heavy(self):
        """Надбавка за вес >= 20 кг"""
        cost, _ = calculate_delivery_cost(25, 100, "обычный")
        # (200 + 100*5) * 1.5 = 1050
        self.assertEqual(cost, 1050)

    def test_fragile_surcharge(self):
        """Надбавка за хрупкий груз"""
        cost, _ = calculate_delivery_cost(2, 100, "хрупкий")
        # 700 + 300 = 1000
        self.assertEqual(cost, 1000)

    def test_dangerous_surcharge(self):
        """Надбавка за опасный груз (+1000)"""
        cost, _ = calculate_delivery_cost(2, 100, "опасный")
        # 700 + 1000 = 1700
        self.assertEqual(cost, 1700)

    def test_express_cost_bug(self):
        """БАГ (строка 36): Экспресс-доставка должна быть дороже, а не дешевле"""
        normal_cost, _ = calculate_delivery_cost(10, 1000, "обычный", False)
        express_cost, _ = calculate_delivery_cost(10, 1000, "обычный", True)

        self.assertGreater(express_cost, normal_cost)

    def test_express_time_bug(self):
        """Снова БАГ (чтоб не забыть: строка 44): Экспресс-доставка не может занимать 0 дней"""
        _, date = calculate_delivery_cost(2, 600, "обычный", True)

        self.assertGreater(datetime.date.fromisoformat(date), datetime.date(2026, 9, 3))

    def test_invalid_weight_zero(self):
        """Нулевой вес"""
        cost, date = calculate_delivery_cost(0, 100, "обычный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")

    def test_invalid_weight_over_max(self):
        """Тутс вес больше 50 кг"""
        cost, date = calculate_delivery_cost(60, 100, "обычный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")

    def test_invalid_distance_zero(self):
        """Нулевая дистанция"""
        cost, date = calculate_delivery_cost(10, 0, "обычный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")

    def test_invalid_distance_over_max(self):
        """Дистанция больше 5000 км"""
        cost, date = calculate_delivery_cost(10, 6000, "обычный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")

    def test_invalid_package_type(self):
        """Неверный тип посылки"""
        cost, date = calculate_delivery_cost(10, 100, "секретный")
        self.assertEqual(cost, -1)
        self.assertEqual(date, "0000-00-00")


if __name__ == '__main__':
    unittest.main()