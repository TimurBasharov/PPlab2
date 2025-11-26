from date_finder import DateFinder


def display_menu():
    """Отображение главного меню"""
    print("\n" + "=" * 50)
    print("ПОИСК ДАТ В ФОРМАТЕ ДД.ММ.ГГГГ")
    print("=" * 50)
    print("1. Ввод текста с клавиатуры")
    print("2. Загрузка с веб-страницы")
    print("3. Чтение из файла")
    print("4. Выход")
    print("=" * 50)


def display_results(dates):
    """Отображение результатов поиска"""
    if dates:
        print(f"\n Найдено корректных дат: {len(dates)}")
        for i, date in enumerate(dates, 1):
            print(f"  {i}. {date}")
    else:
        print("\n Корректных дат не найдено")


def main():
    """Главная функция программы"""
    date_finder = DateFinder()

    while True:
        display_menu()
        choice = input("Выберите вариант (1-4): ").strip()

        if choice == '1':
            dates = date_finder.get_dates_from_user_input()
            display_results(dates)

        elif choice == '2':
            url = input("Введите URL: ").strip()
            if url:
                dates = date_finder.get_dates_from_url(url)
                display_results(dates)
            else:
                print(" URL не может быть пустым!")

        elif choice == '3':
            filename = input("Введите имя файла: ").strip()
            if filename:
                dates = date_finder.get_dates_from_file(filename)
                display_results(dates)
            else:
                print(" Имя файла не может быть пустым!")

        elif choice == '4':
            print(" До свидания!")
            break

        else:
            print(" Неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    main()

#URL https://otvet.mail.ru/question/22649722
