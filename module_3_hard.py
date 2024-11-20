
def calculate_structure_sum(*n):
    ob_summa = 0
    for i in n:
        if isinstance(i, int):
            ob_summa += i
        elif isinstance(i, float):
            ob_summa += i
        elif  isinstance(i, str):
            ob_summa += len(i)
        elif isinstance(i, (list,set)):
            ob_summa += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            ob_summa += calculate_structure_sum(*i.keys())
            ob_summa += calculate_structure_sum(*i.values())
        elif isinstance(i, tuple):
            ob_summa += calculate_structure_sum(*i)
    return ob_summa


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),"Hello", ((),
                                                                                     [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)

print(result)