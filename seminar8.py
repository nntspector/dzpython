

import os


phonebook = {}


def load_phonebook(file_name):
    global phonebook
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            for line in f:
                name, phone = line.strip().split(",")
                phonebook[name] = phone


def save_phonebook(file_name):
    with open(file_name, "w") as f:
        for name, phone in phonebook.items():
            f.write(f"{name},{phone}\n")


def print_phonebook():
    if not phonebook:
        print("Телефонный справочник пуст")
        return
    print("Телефонный справочник:")
    for name, phone in phonebook.items():
        print(f"{name}: {phone}")


def add_contact():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    phonebook[name] = phone
    print(f"Контакт {name} успешно добавлен")


def delete_contact():
    name = input("Введите имя контакта для удаления: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Контакт {name} успешно удален")
    else:
        print(f"Контакт {name} не найден")


def update_contact():
    name = input("Введите имя контакта для изменения: ")
    if name in phonebook:
        phone = input("Введите новый номер телефона: ")
        phonebook[name] = phone
        print(f"Контакт {name} успешно изменен")
    else:
        print(f"Контакт {name} не найден")


def search_contacts():
    query = input("Введите часть имени или фамилии для поиска: ")
    results = []
    for name, phone in phonebook.items():
        if query.lower() in name.lower():
            results.append((name, phone))
    if not results:
        print("Контакты не найдены")
        return
    print(f"Результаты поиска для запроса '{query}':")
    for name, phone in results:
        print(f"{name}: {phone}")


def print_menu():
    print("=" * 30)
    print("Меню:")
    print("1. Показать все контакты")
    print("2. Добавить контакт")
    print("3. Удалить контакт")
    print("4. Изменить контакт")
    print("5. Поиск контактов")
    print("6. Выход")
    print("=" * 30)


def main():
    load_phonebook("phonebook.txt")
    while True:
        print_menu()
        choice = input("Введите номер команды: ")
        if choice == "1":
            print_phonebook()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            search_contacts()
        elif choice == "6":
            save_phonebook("phonebook.txt")
            break
        else:
            print("Некорректный ввод")


if __name__ == "__main__":
    main()
