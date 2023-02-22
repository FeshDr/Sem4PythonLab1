from constants import (
    ADD_OPER,
    SUB_OPER,
    MULT_OPER,
    DIV_OPER,
)
def hello_world():
    print(f'Hello World')

def calc_func(a, b, operator):

    if operator == ADD_OPER:
        return (a + b)
    elif operator == SUB_OPER:
        return (a - b)
    elif operator == MULT_OPER:
        return (a * b)
    elif operator == DIV_OPER:
        if b != 0:
            return (a / b)
        else: return "inf"
    else:
        return "Incorrect operator"

def task3():
    start = []
    result = []
    s = input("Enter arr in one line divide elements with ' '").split()
    try:
        start = list(map(int,s))
    except ValueError:
        print("Incorrect input")
    for i in start:
        if i % 2 == 0:
            result.append(i)
    return result

if __name__ == '__main__':
    hello_world()

    input_a_str = input("Enter A: ")
    input_b_str = input("Enter B: ")
    input_oper_str = input("Enter operator: ")
    try:
        print(calc_func(int(input_a_str),int(input_b_str),input_oper_str))
    except ValueError:
        print("Incorrecrt input")

    out_list = task3()
    for i in out_list:
        print(str(i),end=', ')