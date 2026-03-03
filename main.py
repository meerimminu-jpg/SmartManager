def add(a, b):
    return a + b

# test_calculator.py
import pytest
# Төмөнкү сапты өчүрдүк, себеби add() ушул эле файлда
# from calculator import add 

def test_add_success():
    assert add(2, 3) == 5

def test_add_wrong():
    assert add(2, 2) != 5

def get_user_age():
    try:
        age = int(input("Жашыңызды киргизиңиз: "))
        print(f"Сиздин жашыңыз: {age}")
    except ValueError:
        print("Ката! Сураныч, тамга эмес, бир гана сан киргизиңиз.")

# Функцияны иштетүү үчүн аны чакыруу керек:
if __name__ == "__main__":
    get_user_age()
