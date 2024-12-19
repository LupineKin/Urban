def calculate_structure_sum(a):
    summ = 0
    if isinstance(a, (list, tuple, set)):
        for i in a:
            summ += calculate_structure_sum(i)
    elif isinstance(a, dict):
        for value in a.values():
            summ += calculate_structure_sum(value)
        for i in a:
            summ += calculate_structure_sum(i)
    else:
        if isinstance (a, str):
            summ += len(a)
        else:
            summ += a
        
    return summ


data_structure = [
    [1, 2, 3],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}]),
]

print("Сумма: ", calculate_structure_sum(data_structure))
