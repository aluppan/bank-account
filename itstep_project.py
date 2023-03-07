import sys #выход из Python
def usd_cur():
    global currency
    currency = "USD"
def azn_cur():
    global currency
    currency = "AZN"
def eur_cur():
    global currency
    currency = "EUR"
def currency_falce():
    print("Сбой создания аккаунта. Повторите попытку. При выборе валюты вводите числа от 1 до 3!")
    open_acc()
def currency_conver_false():
    print("Сбой конвертации. Введите одну из этих валют AZN, EUR, USD!!!")
    conver_currency()

def not_correct_step_menu():
    print("Введите число от 2 до 8!")
    user_menu()

def not_correct_step_main():
    print("Введите число 1 или 8!")
    main_()

#1
def open_acc():
    global user_name
    user_name = str(input("Чтобы создать аккаунт, укажите ваше имя: "))
    print(f"{user_name}, выберите одну из поддерживаемых валют:")
    print("Нажмите 1, чтобы выбрать USD - доллар США")
    print("Нажмите 2, чтобы выбрать EUR - евро")
    print("Нажмите 3, чтобы выбрать AZN - манат")
    global currency
    try:
        currency = int(input("Выберите валюту: "))
        if currency > 3 or currency < 1:
            currency_falce()
        if currency == 1:
            usd_cur()
        if currency == 2:
            eur_cur()
        if currency == 3:
            azn_cur()
    except ValueError:
            currency_falce()
    print(f"{user_name} вы создали аккаунт в нашем банке с {currency} валютой! Ваши дальнейшие действия?")
    user_menu()

#2
def del_acc():
    print(f"{user_name}, ваш аккаунт удален из нашей базы данных.")
    main_()

#3
def check_currency():
    print(f"{user_name}, сейчас на вашем балансе {balance} {currency}")
    user_menu()

#4
def conver_currency():
    global balance
    try:
        conver_balance = float(input(f"Введите сумму для конвертации от вашего баланса {balance}: "))
        if conver_balance > balance:
            print(f"Сумма конвертации больше вашего баланса {balance}!")
            user_menu()
    except ValueError:
        print("Введите число!")
        conver_currency()

    global currency_2
    global currency
    try:
        currency_2 = str(input(f"Выберите валюту, в которую хотите конвертировать ваши {currency}: AZN, EUR, USD "))
        currency_2 = currency_2.upper()
        if currency != "USD" and currency != "EUR" and currency != "AZN":
            currency_conver_false()
        if currency == "USD" and currency_2 == "AZN":
            balance = conver_balance * 1.70
            print("USD в AZN - ", balance)
            currency = currency_2
        if currency == "USD" and currency_2 == "EUR":
            balance = conver_balance * 0.81
            print("USD в EUR - ", balance)
            currency = currency_2

        if currency == "EUR" and currency_2 == "AZN":
            balance = conver_balance * 2.07
            print("EUR в AZN - ", balance)
            currency = currency_2
        if currency == "EUR" and currency_2 == "USD":
            balance = conver_balance * 1.22
            print("EUR в USD - ", balance)
            currency = currency_2

        if currency == "AZN" and currency_2 == "USD":
            balance = conver_balance * 0.58
            print("AZN в USD - ", balance)
            currency = currency_2
        if currency == "AZN" and currency_2 == "EUR":
            balance = conver_balance * 0.48
            print("AZN в EUR - ", balance)
            currency = currency_2
    except ValueError:
        currency_conver_false()
    user_menu()

balance = 0
#5
def debit_balance():
    global balance
    if balance > 0:
        try:
            debit = float(input(f"Сколько вы хотите списать с {balance}: "))
            if debit > balance:
                print("У вас нет столько средств!")
                debit_balance()
            else:
                balance -= debit
                print(f"На вашем счету осталось {balance} {currency}")
        except ValueError:
            print("Введите число!")
            debit_balance()
    else:
        print("На вашем счету нет средств")
    user_menu()

#6
def balance_acc():
    global balance
    global deposit
    try:
        deposit = float(input("На какую сумму хотите пополнить счет: "))
        balance = (balance + deposit)
        print(f"На вашем балансе сейчас {balance} {currency}")
    except ValueError:
        print("Введите число!")
        balance_acc()
    user_menu()

#7
def debit_acc():
    global balance
    if balance > 0:
        global withdrawal_balance
        try:
            withdrawal_balance = float(input(f"Сколько вы вывести с вашего баланса {balance} {currency}: "))
            if withdrawal_balance > balance:
                print("У вас нет столько средств!")
                debit_acc()
            else:
                old_balance = withdrawal_balance
                balance -= withdrawal_balance
                print(f"Вы вывели {old_balance} {currency}. На вашем счету осталось {balance} {currency}")
        except ValueError:
            print("Введите число!")
            debit_acc()
    else:
        print("На вашем счету нет средств")
    user_menu()

#8
def break_app():
    sys.exit() #выход из Python

def user_menu():
    print("\n\t\t\t", "Банковский аккаунт:", "\n")
    #print("Нажмите 1, чтобы создать аккаунт c возможностью выбора валюты. Поддерживаемые валюты: USD, EUR, AZN")
    print("Нажмите 2, чтобы удалить аккаунт")
    print("Нажмите 3, чтобы узнать счёт в определённой валюте (например, USD - доллар США) и его сумма.")
    print("Нажмите 4, чтобы конвертировать валюту. Поддерживаемые валюты: USD, EUR, AZN")
    print("Нажмите 5, чтобы списать средства")
    print("Нажмите 6, чтобы пополнить средства")
    print("Нажмите 7, чтобы вывести баланс")
    print("Нажмите 8, чтобы выйти из программы", "\n")
    step = int(input("Выбрать: "))
    if step == 2:
        del_acc()
    elif step == 3:
        check_currency()
    elif step == 4:
        conver_currency()
    elif step == 5:
        debit_balance()
    elif step == 6:
        balance_acc()
    elif step == 7:
        debit_acc()
    elif step == 8:
        break_app()
    elif step >= 9 or step <= 1:
        not_correct_step_menu()
    main_()

def main_():
    print("\n\t\t\t", "Банковский аккаунт:", "\n")
    print("Нажмите 1, чтобы создать аккаунт c возможностью выбора валюты. Поддерживаемые валюты: USD, EUR, AZN")
    print("Нажмите 8, чтобы выйти из программы", "\n")

    try:
        step = int(input("Выбрать: "))
        if step == 1:
            open_acc()
        elif step == 8:
            break_app()
        elif step != 1 or step != 8 or step != int:
            not_correct_step_main()
    except ValueError:
        not_correct_step_main()
main_()