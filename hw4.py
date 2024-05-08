
# Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
# — не менее 8 символов
# — наличие прописных и строчных букв
# — наличие цифр
# и переводит его в хэш-значение.


import re
import hashlib


def check_password_strength(password):
    if len(password) < 8:
        return False, "Пароль должен быть не менее 8 символов."

    if not re.search(r"[a-z]", password):
        return False, "Пароль должен содержать хотя бы одну строчную букву."

    if not re.search(r"[A-Z]", password):
        return False, "Пароль должен содержать хотя бы одну прописную букву."

    if not re.search(r"[0-9]", password):
        return False, "Пароль должен содержать хотя бы одну цифру."

    return True, "Пароль соответствует требованиям безопасности."


def hash_password(password):
    # Создаем хэш-объект с помощью SHA-256
    hash_object = hashlib.sha256()
    hash_object.update(password.encode('utf-8'))
    # Получаем хеш в шестнадцатеричном формате
    hashed_password = hash_object.hexdigest()
    return hashed_password


if __name__ == "__main__":
    password = input("Введите пароль для проверки: ")

    is_valid, message = check_password_strength(password)
    print(message)
    if is_valid:
        hashed_password = hash_password(password)
        print("Хеш пароля:", hashed_password)
