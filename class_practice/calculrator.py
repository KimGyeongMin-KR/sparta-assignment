class Cal:
    history = []
    op_dict = {
        '+' : lambda x,y: x+y,
        '-' : lambda x,y: x-y,
        '*' : lambda x,y: x*y,
        '/' : lambda x,y: x/y
    }
    def cal(self, num1, op, num2):
        self.history.append((num1,op,num2))
        return self.op_dict[op](num1,num2)
    def reaction_history(self, idx):
        if abs(idx-1) > len(self.history):
            return 'out of range'
        return self.cal(*self.history[idx-1])