import datetime

def show_time():
    print("Негизги бутактын жаңы жазуусу")
    print(f"Учурдагы убакыт: {datetime.datetime.now().strftime('%H:%M:%S')}")

def show_author():
    print("Программанын автору: Сиздин Атыңыз")