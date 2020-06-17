def formatCurrencyOutput(x):
    return '{:,.0f}kr'.format(int(x))


initialmoney = input("Hur mycket pengar har du totalt sparat? ")
years_of_age = int(input("Hur gammal är du? "))
retire_age = int(input("Vid vilken ålder vill du sluta arbeta? "))
monthly_payments_from_ppm_and_tjp = int(input("Hur mycket säger pension.se att du kommer få ut i månaden? "))
adding_money_every_year = int(input("Hur mycket pengar sparar du varje år? "))
interest_rate = float(
    input("Hur mycket tror du att ditt innehav kommer att öka per år? (ex 1.13 = 13%) "))
money_earned = float(initialmoney)
print()
for x in range(years_of_age, retire_age):
    money_earned = (money_earned + adding_money_every_year) * interest_rate
    print(f"År {x + 1} = {formatCurrencyOutput(money_earned)}")
print()
monthly_payment_from_savings = money_earned / (85 - retire_age) / 12
print(f"Du kommer att få ut totalt {formatCurrencyOutput(monthly_payments_from_ppm_and_tjp + monthly_payment_from_savings)} varje månad tills du är 85 år...")
