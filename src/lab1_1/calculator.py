'''module that calc some math example'''


def get_split_arr(data_st: str):
    '''split input string to arr of numbers and operations'''
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



def do_operation(first_arg: float,second_arg: float,operation: str):
    '''do some operation to first and second arguments'''
    match operation:
        case '+': return round(first_arg + second_arg,7)
        case '-': return round(first_arg - second_arg,7)
        case '*': return round(first_arg * second_arg,7)
        case '/': return round(first_arg / second_arg,7)
        case '^': return round(first_arg ** second_arg,7)


def to_calc(calc_example_str: str):
    '''calc some math example in string format'''
    try:
        num_stack = []
        op_stack = []
        prior = {'+': 1,'-': 1, '*': 2, '/': 2,'^':3}
        calc_example_arr = get_split_arr(calc_example_str)

        for i in calc_example_arr:
            if i == '(':
                op_stack.append('(')
            elif (i.isdigit()
                  or i.replace('.','',1).isdigit()
                  or i.replace('-','',1).isdigit()):
                num_stack.append(float(i))
            elif i in '+-*/^':
                if (len(op_stack) == 0 or op_stack[-1] == '('
                        or prior[i] > prior[op_stack[-1]]):
                    op_stack.append(i)
                elif prior[i] <= prior[op_stack[-1]]:
                    while (len(op_stack) > 0 and op_stack[-1] != '('
                           and prior[i] <= prior[op_stack[-1]]):
                        second_arg = num_stack.pop()
                        first_arg = num_stack.pop()
                        operation = op_stack.pop()
                        num_stack.append(do_operation(first_arg,second_arg,
                                                      operation))
                    op_stack.append(i)
            elif i == ')':
                while op_stack[-1] != '(':
                    second_arg = num_stack.pop()
                    first_arg = num_stack.pop()
                    operation = op_stack.pop()
                    num_stack.append(do_operation(first_arg, second_arg,
                                                  operation))
                del_br = op_stack.pop()

        while len(op_stack) > 0:
            second_arg = num_stack.pop()
            first_arg = num_stack.pop()
            operation = op_stack.pop()
            num_stack.append(do_operation(first_arg, second_arg,
                                          operation))

        return num_stack[0]
    except ZeroDivisionError:
        return 'Error: Division by zero'
    except:
        return 'Input Error'


