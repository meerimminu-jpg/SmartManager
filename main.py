import datetime

def show_time():
    now = datetime.datetime.now()
    print(f"Учурдагы убакыт: {now.strftime('%H:%M:%S')}")
