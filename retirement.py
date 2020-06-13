def formatCurrencyOutput(x):
    return '{:,.0f}kr'.format(int(x))


initialmoney = input("How much money do you start with? ")
years_of_age = int(input("How old are you? "))
retire_age = int(input("At which age are you going to retire? "))
adding_money_every_year = int(input("How much do you add every year? "))
interest_rate = float(
    input("What is the percentage it will raise? (ex 1.13 = 13%) "))
money_earned = float(initialmoney)

for x in range(years_of_age, retire_age):
    money_earned = (money_earned + adding_money_every_year) * interest_rate
    print(f"År {x + 1} = {formatCurrencyOutput(money_earned)}")

print()

monthly_payment_from_savings = money_earned / (85 - retire_age) / 12

print(f"You get {formatCurrencyOutput(monthly_payment_from_savings)} each month until you are 85 years")
