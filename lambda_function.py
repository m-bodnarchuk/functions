def double(x):
    return x * 2
arr = [6.7, 89, 3.4, 23.4567, 9.765]
new_arr = list(map(double, arr))
print(new_arr)

def double(x):
    return x * 2
arr = [6.7, 89, 3.4, 23.4567, 9.765]
new_arr = list(map(lambda x: x*2, arr))
print(new_arr)

arr1 = ["hello", "apple", "sixseven", "ballerinacapuchina"]
new_arr = list(map(lambda x: len(x), arr1))
print(new_arr)

arr = [-6, 8, 9, 0, -45, 34, 78, 32, -15]
arr.sort(key=lambda x: abs(x))
print(arr)

arr = [34, 95, 54, 35, 31, 85, 52]
arr.sort(key=lambda x: (x%10, x))
print(arr)

raw_salaries = ["  1500", "2300 ", "  1850  ", "4000"]
new_salaries = list(map(lambda x: int(x.strip()), raw_salaries))
print(new_salaries)

transfers = [50, 1500, 3200, 15, 25000, 400, 31000]
new = list(filter(lambda x: x<100 or x>20000, transfers))
print(new)