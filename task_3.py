balance = 0
wealth_tax = 0.1
transactions = []

def print_balance():
    global balance
    print(f"Ваш текущий баланс: {balance} у.е.")

def deposit(amount):
    global balance, transactions
    if amount % 50 == 0:
        balance += amount
        transactions.append(f"Пополнение: +{amount} у.е.")
        print(f"Вы пополнили счет на {amount} у.е.")
        print_balance()
    else:
        print("Сумма пополнения должна быть кратной 50 у.е.")

def withdraw(amount):
    global balance, transactions
    if amount % 50 == 0:
        if amount <= balance:
            if balance > 5_000_000:
                amount_with_tax = amount + amount * wealth_tax
                balance -= amount_with_tax
                transactions.append(f"Снятие: -{amount_with_tax} у.е. (с налогом)")
                print(f"Вы сняли {amount} у.е. (с налогом)")
            else:
                balance -= amount
                transactions.append(f"Снятие: -{amount} у.е.")
                print(f"Вы сняли {amount} у.е.")
            print_balance()
        else:
            print("На вашем счету недостаточно средств.")
    else:
        print("Сумма снятия должна быть больше 50 у.е.")


def exit_program():
    global transactions
    print("Выход из программы.")
    print("История операций:")
    for transaction in transactions:
        print(transaction)
    exit()


def atm():
    global transactions
    while True:
        print("\nВыберите действие:")
        print("1. Пополнить счет")
        print("2. Снять средства")
        print("3. Выйти")
        choice = input("Введите номер действия: ")
        if choice == "1":
            amount = int(input("Введите сумму для пополнения: "))
            deposit(amount)
        elif choice == "2":
            amount = int(input("Введите сумму для снятия: "))
            withdraw(amount)
        elif choice == "3":
            exit_program()
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    atm()
