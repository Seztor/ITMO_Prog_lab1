
def get_split_arr(data_st: str):

    data_st = (data_st.
               replace('(',' ( ').
               replace(')',' ) ').
               replace('*',' * ').
               replace('+',' + ').
               replace('-',' - ').
               replace('/',' / ').
               replace('^',' ^ ').
               strip())
    while '  ' in data_st:
        data_st = data_st.replace('  ',' ')

    example = data_st.split()

    return example


def do_oper(x: int,y: int,op: str):
    match op:
        case '+': return x+y
        case '-': return x-y
        case '*': return x*y
        case '/': return x/y
        case '^': return x**y


def to_calc(calc_example_str):
    num_stack = []
    op_stack = []
    prior = {'+': 1,'-': 1, '*': 2, '/': 2,'^':3}
    calc_example_arr = get_split_arr(calc_example_str)

    for i in calc_example_arr:
        #print('!', i, end=' : ')
        if i == '(': op_stack.append('(')
        elif i.isdigit() or i.replace('.','',1).isdigit(): num_stack.append(i)
        elif i in '+-*/^':
            if len(op_stack) == 0 or op_stack[-1] == '(' or prior[i] > prior[op_stack[-1]]: op_stack.append(i)
            elif prior[i] <= prior[op_stack[-1]]:
                while len(op_stack) > 0 and op_stack[-1] != '(' and prior[i] <= prior[op_stack[-1]]:
                    y = float(num_stack.pop())
                    x = float(num_stack.pop())
                    op = op_stack.pop()
                    num_stack.append(str(do_oper(x,y,op)))
                op_stack.append(i)
        elif i == ')':
            while op_stack[-1] != '(':
                y = float(num_stack.pop())
                x = float(num_stack.pop())
                op = op_stack.pop()
                num_stack.append(str(do_oper(x, y, op)))
            del_br = op_stack.pop()
        #print(op_stack, num_stack)

    while len(op_stack) > 0:
        y = float(num_stack.pop())
        x = float(num_stack.pop())
        op = op_stack.pop()
        num_stack.append(str(do_oper(x, y, op)))

    return num_stack[0]

