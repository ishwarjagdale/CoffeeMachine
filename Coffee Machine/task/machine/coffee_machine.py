water_stock = 400
milk_stock = 540
coffee_beans_stock = 120
disposable_cups_stock = 9
money_earned = 550


def status():
    print(f"The coffee machine has:\n"
          f"{water_stock} of water\n"
          f"{milk_stock} of milk\n"
          f"{coffee_beans_stock} of coffee beans\n"
          f"{disposable_cups_stock} of disposable cups\n"
          f"${money_earned} of money\n")


def buy():
    coffee_option = input("What do you want to buy? 1 -  espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    global water_stock, milk_stock, coffee_beans_stock, disposable_cups_stock, money_earned
    if coffee_option == '1':
        water_can = int(water_stock / 250)
        coffee_beans_can = int(coffee_beans_stock / 16)
        disposable_cups_can = disposable_cups_stock - 1
        capable = min(water_can, coffee_beans_can, disposable_cups_can)
        if capable >= 1:
            print("I have enough resources, making you a coffee!")
            water_stock -= 250
            milk_stock -= 0
            coffee_beans_stock -= 16
            disposable_cups_stock -= 1
            money_earned += 4

        else:
            print(f"Sorry, not enough {min(water_can, coffee_beans_can, disposable_cups_stock)}")

    elif coffee_option == '2':
        water_can = int(water_stock / 350)
        milk_can = int(milk_stock / 75)
        coffee_beans_can = int(coffee_beans_stock / 20)
        disposable_cups_can = disposable_cups_stock - 1
        capable = min(water_can, milk_can, coffee_beans_can, disposable_cups_can)
        if capable >= 1:
            print("I have enough resources, making you a coffee!")
            water_stock -= 350
            milk_stock -= 75
            coffee_beans_stock -= 20
            disposable_cups_stock -= 1
            money_earned += 7

        else:
            if water_can is min(water_can, milk_can, coffee_beans_can, disposable_cups_stock):
                print(f"Sorry, not enough water")
            elif milk_can is min(water_can, milk_can, coffee_beans_can, disposable_cups_stock):
                print(f"Sorry, not enough milk")
            elif coffee_beans_can is min(water_can, milk_can, coffee_beans_can, disposable_cups_stock):
                print(f"Sorry, not enough coffee beans")
            elif disposable_cups_stock == 0:
                print(f"Sorry, not enough disposable cups")
            else:
                print("Not enough resources.")

    elif coffee_option == '3':
        water_can = int(water_stock / 200)
        milk_can = int(milk_stock / 100)
        coffee_beans_can = int(coffee_beans_stock / 12)
        disposable_cups_can = disposable_cups_stock - 1
        capable = min(water_can, milk_can, coffee_beans_can, disposable_cups_can)
        if capable >= 1:
            print("I have enough resources, making you a coffee!")
            water_stock -= 200
            milk_stock -= 100
            coffee_beans_stock -= 12
            disposable_cups_stock -= 1
            money_earned += 6
        else:
            print(f"Sorry, not enough {min(water_can, milk_can, coffee_beans_can, disposable_cups_stock)}")

    elif coffee_option == 'back':
        act()

    else:
        raise NameError("Incorrect Option")


def fill():
    global milk_stock, water_stock, coffee_beans_stock, disposable_cups_stock
    water_fill = int(input("Write how many ml of water the coffee machine to add:\n"))
    milk_fill = int(input("Write how many ml of milk the coffee machine to add:\n"))
    coffee_beans_fill = int(input("Write how many grams of coffee beans the coffee machine to add:\n"))
    disposable_cups_fill = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    water_stock += water_fill
    milk_stock += milk_fill
    coffee_beans_stock += coffee_beans_fill
    disposable_cups_stock += disposable_cups_fill


def take():
    global money_earned
    print(f"I gave you {money_earned}")
    money_earned = 0


def remaining():
    global water_stock, milk_stock, coffee_beans_stock, disposable_cups_stock, money_earned
    status()


def act():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        action = action.strip().lower()

        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'remaining':
            remaining()
        elif action == 'exit':
            exit()
        else:
            raise NameError("Incorrect Option")


act()