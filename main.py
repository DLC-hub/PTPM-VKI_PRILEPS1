from src.database import DatabaseRepository


def main():
    db = DatabaseRepository("forum.db")

    # просто чекаем работу
    db.add(1, "Ivan", "Привет")
    print(db.get_by_id(1))

    print(db.get_by_name("Ivan"))


if __name__ == "__main__":
    main()