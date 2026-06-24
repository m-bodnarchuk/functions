# task 2
def currency_uah(amount: float, rate: float, fee_percentage = 0):
    return amount *rate* (1 - fee_percentage/100)
    return result
def currency_usd(amount: float, rate: float, fee_percentage = 0):
    return amount/rate * (1 - fee_percentage / 100)

print(currency_usd(1000, 42))
print(currency_uah(50, 44.5, 10))





