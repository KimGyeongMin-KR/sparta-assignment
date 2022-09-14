class Cal:
    history = []
    op_dict = {
        '+' : lambda x,y: x+y,
        '-' : lambda x,y: x-y,
        '*' : lambda x,y: x*y,
        '/' : lambda x,y: x/y
    }
    def cal(self, num1, op, num2):
        try:
            num1,num2 = int(num1),int(num2)
            op = self.op_dict[op]
            self.history.append((num1,op,num2))
            return op(num1,num2)
        except ValueError:
            return '숫자 연산자 숫자로 입력해주세요.'
        except KeyError:
            return '+-*/ 중 하나의 연산자를 입력해주세요.'
        except ZeroDivisionError:
            return '0으로는 못 나눕니다.'
    def reaction_history(self, idx):
        if abs(idx-1) > len(self.history):
            return 'out of range'
        return self.cal(*self.history[idx-1])