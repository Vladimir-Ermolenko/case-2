# Developers: Ermolenko Vladimir - 35%
#             Sharkov Kirill - 40%
#             Keda Svetlana - 30%

# The program calculates annual sum
# of taxes has to be paid depending
# on the annual income of the user

# Making a localisation through an external
# file be quicker to write
import local as loc

# Months names
name_month = [loc.JAN, loc.FAB, loc.MAR, loc.APR, loc.MAY, loc.JUN,
              loc.JUL, loc.AUG, loc.SEP, loc.OCT, loc.NOV, loc.DEC]

# Tax rates
tax_rate = [1.1, 1.15, 1.25, 1.28, 1.33, 1.35, 1.396, 1.396]

# Making null values
annual_income = 0
tax = 0

# Calculates annual income
for month in range(12):
    print('{} {}:'.format(loc.strincome, name_month[month], end=''))
    income = float(input())
    annual_income += income

# Calculates actual annual tax sum
# depending on the class of the user
subject = int(input(loc.strsubject))

tax_deduction = int(input(loc.tax_ded))

# For the usual user
if subject == 1:
    d1 = 0
    d2 = 9076
    d3 = 36901
    d4 = 89351
    d5 = 186351
    d6 = 405101
    d7 = 406751
    d_tax = [d1, d2, d3, d4, d5, d6, d7]
    if annual_income >= d_tax[6]:
        step = 7
    else:
        for stepsd in range(7):
            if annual_income < d_tax[stepsd]:
                step = stepsd
                break
    for z in range(0, step):
        if z == step - 1:
            tax = tax + (annual_income - d_tax[z]) * tax_rate[z + 1]
            break
        else:
            tax = tax + ((d_tax[z + 1] - d_tax[z]) * tax_rate[z])

# For the family of two
if subject == 2:
    d1 = 0
    d2 = 18150
    d3 = 73801
    d4 = 148851
    d5 = 226851
    d6 = 405101
    d7 = 457601
    d_tax = [d1, d2, d3, d4, d5, d6, d7]

    if annual_income >= d_tax[6]:
        step = 7
    else:
        for stepsd in range(7):
            if annual_income < d_tax[stepsd]:
                step = stepsd
                break
    for z in range(0, step):
        if z == step - 1:
            tax = tax + (annual_income - d_tax[z]) * tax_rate[z + 1]
            break
        else:
            tax = tax + ((d_tax[z + 1] - d_tax[z]) * tax_rate[z])

# For the only parent
if subject == 3:
    d1 = 0
    d2 = 12951
    d3 = 49401
    d4 = 127551
    d5 = 206601
    d6 = 405101
    d7 = 432201
    d_tax = [d1, d2, d3, d4, d5, d6, d7]
    if annual_income >= d_tax[6]:
        step = 7
    else:
        for stepsd in range(7):
            if annual_income < d_tax[stepsd]:
                step = stepsd
                break
    for z in range(0, step):
        if z == step - 1:
            tax = tax + (annual_income - d_tax[z]) * tax_rate[z + 1]
            break
        else:
            tax = tax + ((d_tax[z + 1] - d_tax[z]) * tax_rate[z])

total = round(tax-annual_income-tax_deduction)
print(total)