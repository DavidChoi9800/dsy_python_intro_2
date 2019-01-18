# This first 6 lines are provided for you

def computepay(h,r):
    if h > 40 :
        extra = h - 40
        total_pay = (40 * r) + (float(extra) * (r * 1.5))
        return total_pay
    else :
        total_pay = (h * r)
        return total_pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter Rates:")
r = float(rate)

p = computepay(h,r)
print("Pay",p)
