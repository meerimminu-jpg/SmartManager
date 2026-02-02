import os
from datetime import datetime
from colorama import Fore, Style, init
from art import tprint

# Түстөрдү жана режимдерди иштетүү
init()

def main():
    # 1. Кооз логотип чыгаруу
    print(Fore.YELLOW)
    tprint("SmartManager") 
    print(Style.RESET_ALL)

    # 2. Системалык маалыматтарды алуу (Стандарттык китепканалар менен)
    uibaqyt = datetime.now().strftime("%H:%M:%S")
    papka = os.getcwd()

    print(Fore.CYAN + "--- СИСТЕМАЛЫК МААЛЫМАТ ---")
    print(f"Учурдагы убакыт: {uibaqyt}")
    print(f"Долбоордун жайгашкан жери: {papka}")
    print("-" * 27 + Style.RESET_ALL)

    # 3. Колдонуучу менен интерактивдүү байланыш
    print(Fore.GREEN + "\nПрограмма ийгиликтүү иштеп жатат!")
    user_name = input(Fore.WHITE + "Студенттин аты-жөнү: ")
    
    print(f"\n{Fore.GREEN}Азаматсыз, {Fore.YELLOW}{user_name}{Fore.GREEN}!")
    print(f"Сиз №4 лабораторияда 4 башка китепкананы колдондуңуз!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
