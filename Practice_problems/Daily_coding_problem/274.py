'''
This problem was asked by Facebook.

Given a string consisting of parentheses, single digits, and positive and negative signs, convert the string into a mathematical expression to obtain the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4.
'''

def simplify_expression(expr):
    if len(expr) == 0:
        raise ValueError("Expression cannot be of length 0")
    
    stack = []
    for i in range(len(expr)):
        if expr[i] == ' ':
            continue
        
        if expr[i] == ')':
            cur_expr = []
            while stack[-1] != '(':
                cur_expr = [stack.pop()] + cur_expr
            stack.pop()
            stack += [evaluate_expression(cur_expr)]
        elif expr[i].isdigit():
            stack.append(int(expr[i]))
        else:
            stack.append(expr[i])
    
    return stack
    
def evaluate_expression(expr):
    res = 0
    sign = 1
    for i in range(len(expr)):
        if expr[i] == '+':
            sign = 1
        elif expr[i] == '-':
            sign = -1
        else:
            res += (sign * int(expr[i]))
    
    return res

if __name__=="__main__":
    expr1 = '-1 + (2 + 3)'
    print(evaluate_expression(simplify_expression(expr1)))