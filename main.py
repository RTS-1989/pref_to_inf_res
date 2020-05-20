def pref_count(inp_math_op):

    pref_list = inp_math_op.split(' ')
    assert not len(pref_list) != 3, 'Количество аргументов должно быть 3. Например + 3 2'
    
    operator_list = ['+', '-', '*', '/']
    operator = pref_list[0]
    assert operator in operator_list, 'Значение оператора должно быть следующим: +, -, *, /'

    try:
        arg_1 = int(pref_list[1])
        arg_2 = int(pref_list[-1])
    except ValueError:
        return print('Ошибка! Для вычислений необходимо вводить числовые значения')

    
    if operator == '+':
        print(arg_1 + arg_2)
    elif operator == '-':
        print(arg_1 - arg_2)
    elif operator == '*':
        print(arg_1 * arg_2)
    elif operator == '/':
        try:
            print(arg_1 / arg_2)
        except ZeroDivisionError:
            return print('Ошибка! На ноль делить нельзя!')

while True:
    pref_count(input('Введите математическую операцию: '))