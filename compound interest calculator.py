# python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input ("Enter the principle amount: "))
    if principle < 0:
        print("Principle cant be lower than zero")
    else:
        break



while rate <= 0:
    rate = float(input ("Enter the interest rate: "))
    if rate < 0:
        print("interest rate cant be lower than zero")
    else:
        break



while time <= 0:
    time = float(input ("Enter the time in years: "))
    if time < 0:
        print("time cant be lower than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} years: ${total:.2f}")
