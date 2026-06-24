def analyze_branches(goal, *data):
    suma = sum(data)
    q = 0
    for i in data:
        if i > goal:
            q += 1
    return suma, q
print(*analyze_branches(50000, 45000, 52000, 60000, 30000))



