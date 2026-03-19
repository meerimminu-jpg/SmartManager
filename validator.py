def check_email(email):
    """Проверка формата электронной почты (наличие @ и .)"""
    if "@" in email and "." in email:
        # Точка должна идти после символа @
        if email.find("@") < email.rfind("."):
            return True, "Почта введена верно."
    return False, "Ошибка! В почте должны быть '@' и '.'."

def check_password_strong(password):
    """Проверка сложности пароля (длина, наличие цифр и заглавных букв)"""
    if len(password) < 8:
        return False, "Пароль должен содержать минимум 8 символов."
    
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    if not has_upper:
        return False, "В пароле должна быть хотя бы одна заглавная буква."
    if not has_digit:
        return False, "В пароле должна быть хотя бы одна цифра."
    
    return True, "Пароль надежный."

def is_username_unique(username):
    """Проверка уникальности логина"""
    existing_users = ["admin", "user1", "almaz", "kyrgyz_boy"]
    if username.lower() in existing_users:
        return False, "Этот логин уже занят. Выберите другой."
    return True, "Логин свободен."
