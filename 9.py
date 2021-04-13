##
# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added to the
# balance of the savings account. Write a program that begins by reading the amount of
# money deposited into the account from the user. Then your program should compute
# and display the amount in the savings account after 1, 2, and 3 years. Display each
# amount so that it is rounded to 2 decimal places.
#              

INTEREST = 0.04

initial_deposit = float(input("Inserisci l'ammontare del deposito iniziale: "))

deposit_1_year = initial_deposit + (initial_deposit * INTEREST)
deposit_2_year = deposit_1_year + (deposit_1_year * INTEREST)
deposit_3_year = deposit_2_year + (deposit_2_year * INTEREST)

print("Il deposito iniziale è:", "%.2f" %initial_deposit)
print("Il deposito dopo un anno è:", "%.2f" %deposit_1_year)
print("Il deposito dopo due anni è:", "%.2f" %deposit_2_year)
print("Il deposito dopo tre anni è:", "%.2f" %deposit_3_year)
