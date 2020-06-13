def formatCurrencyOutput(x):
    return '{:,.0f}kr'.format(int(x))


initialmoney = input("How much money do you start with? ")
years_to_retire = int(input("How many years left before you need the money? "))
adding_money_every_year = int(input("How much do you add every year? "))
interest_rate = float(
    input("What is the percentage it will raise? (ex 1.13 = 13%) "))
money_earned = float(initialmoney)

for x in range(1, years_to_retire):
    money_earned = (money_earned + adding_money_every_year) * interest_rate
    print(f"År {x} = {formatCurrencyOutput(money_earned)}")

print(f"Till slut finns det {formatCurrencyOutput(money_earned)}")
