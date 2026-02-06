def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Нөлгө бөлүүгө болбойт!")
    return a / b