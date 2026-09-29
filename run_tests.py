
import unittest


def run_module(module_name):

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(module_name)
    result = unittest.TextTestRunner(verbosity=0).run(suite)

    all_tests = result.testsRun
    failures = result.failures + result.errors
    failed = len(failures)
    passed = all_tests - failed

    return all_tests, passed, failed, failures


# --- набор тестов ---
print("Запуск тестов, полетели...\n")

total_my, passed_my, failed_my, _ = run_module("test_my_project")
total_dl, passed_dl, failed_dl, delivery_failures = run_module("test_delivery")

total_all = total_my + total_dl


# --- ПУНКТ А ---
print("=" * 60)
print("ПУНКТ А")
print("=" * 60)
print(f"Всего написано тестов: {total_all}")
print(f"  • Для своего кода (main.py):     {passed_my} из {total_my} прошло")
print(f"  • Для чужого кода (delivery.py): {passed_dl} из {total_dl} прошло")
print()


# --- ПУНКТ Б ---
print("=" * 60)
print("ПУНКТ Б")
print("=" * 60)
print(f"Упавших тестов для delivery.py: {failed_dl}")
print()


# --- ПУНКТ В ---
print("=" * 60)
print("ПУНКТ В")
print("=" * 60)
if delivery_failures:
    for i, (test, traceback) in enumerate(delivery_failures, start=1):
        test_name = str(test).split(" ")[0]
        last_line = traceback.strip().split("\n")[-1]
        print(f"{i}. Тест: {test_name}")
        print(f"   Ошибка: {last_line}")
        print()
else:
    print("Упавших тестов нет.")