def computepay(h,r):
    if hrs <= 40:
        ttl = h * r
    else:
        ttl = r * (40 + (h - 40) * 1.5)
    return ttl

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)
p = computepay(h,r)
print("Pay",p)
