# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
initial_monthly_payment = 2684.11
monthly_payment = initial_monthly_payment
total_paid = 0.0
extra_payment_month = 12

while principal > 0:
    if extra_payment_month > 0:
        extra_payment_month -= 1
        monthly_payment = initial_monthly_payment + 1000
    else:
       monthly_payment = initial_monthly_payment

    principal = principal * (1 + rate / 12) - monthly_payment
    total_paid = total_paid + monthly_payment
    print('monthly_payment:',monthly_payment)
print("Total paid:",round(total_paid,2))
