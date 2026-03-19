from validator import check_email, check_password_strong, is_username_unique

def registration():
    print("=== Регистрация в системе ===")
    
    # 1. Проверка логина
    while True:
        login = input("Введите новый логин: ")
        ok, msg = is_username_unique(login)
        if ok:
            break
        print(msg)

    # 2. Проверка почты
    while True:
        email = input("Ваша электронная почта: ")
        ok, msg = check_email(email)
        if ok:
            break
        print(msg)

    # 3. Проверка и подтверждение пароля
    while True:
        pwd1 = input("Придумайте пароль: ")
        ok, msg = check_password_strong(pwd1)
        if not ok:
            print(msg)
            continue
            
        pwd2 = input("Повторите пароль: ")
        if pwd1 == pwd2:
            print("Регистрация прошла успешно!")
            break
        else:
            print("Ошибка! Пароли не совпадают.")

if __name__ == "__main__":
    registration()

