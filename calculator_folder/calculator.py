def cal(num1:float, num2:float, op:str):
    """
    num1, num2 have to be float type\n
    op has to be one in '+-*/'\n
    return float
    """
    op_dict={
    '+' : lambda x,y: float(x)+float(y),
    '-' : lambda x,y: float(x)-float(y),
    '*' : lambda x,y: float(x)*float(y),
    '/' : lambda x,y: float(x)/float(y),
    }
    return op_dict[op](num1,num2)
