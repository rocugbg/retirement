def formatCurrencyOutput(x):
    return '{:,.0f}kr'.format(int(x))


initialmoney = input("Hur mycket pengar har du totalt sparat (allt förutom tjänstepension, ips osv.)?\n")
years_of_age = int(input("Hur gammal är du?\n"))
retire_age = int(input("Vid vilken ålder vill du sluta arbeta?\n"))
monthly_payments_from_ppm_and_tjp = int(input("Hur mycket säger pension.se att du kommer få ut i månaden? (Då räknas den allmänna pensionen, tjp, ips med.)\n"))
adding_money_every_year = int(input("Hur mycket pengar sparar du varje år?\n"))
interest_rate_percent = float(
    input("Hur mycket tror du att ditt innehav kommer att öka per år i procent? (Exempelvis 13 för 13%)\n"))
money_earned = float(initialmoney)
print()
for x in range(years_of_age, retire_age):
    interest_rate = interest_rate_percent / 100 + 1
    money_earned = (money_earned + adding_money_every_year) * interest_rate
    print(f"År {x + 1} = {formatCurrencyOutput(money_earned)}")
print()
monthly_payment_from_savings = money_earned / (85 - retire_age) / 12
print(f"Du kommer att få ut totalt {formatCurrencyOutput(monthly_payments_from_ppm_and_tjp + monthly_payment_from_savings)} varje månad (innan skatt) tills du är 85 år.")
