def profit(revenue: float, fixed_costs: float, tax = 18) -> float:
    if revenue < fixed_costs:
        return revenue - fixed_costs
    result = ((revenue - fixed_costs) - (revenue - fixed_costs)*(tax/100))
    return result
data = [[15000, 10000], [10000, 7000], [30000, 40000], [5000, 7000]]
for month in data:
    print(profit(month[0], month[1]), profit(month[0], month[1], 20))



