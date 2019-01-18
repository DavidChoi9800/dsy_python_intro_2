# This first 2 lines are provided for you

hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter Rates:")
r = float(rate)

if h > 40 :
    extra = h - 40
    total_pay = (40 * r) + (float(extra) * (r * 1.5))
else :
    total_pay = (h * r)

print ('Pay;: ', total_pay)
