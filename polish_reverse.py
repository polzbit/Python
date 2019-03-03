# Evaluate a reverse polish notation 

def parse_rpn(expression):
    
 
    stack = []
 
    for val in expression.split(' '):
        if val in ['-', '+', '*', '/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if val=='-': result = op2 - op1
            if val=='+': result = op2 + op1
            if val=='*': result = op2 * op1
            if val=='/': result = op2 / op1
            stack.append(result)
        else:
            stack.append(int(val))
 
    return stack.pop()

def main():
    print parse_rpn('10 5 /')

if __name__ == "__main__": main()