class Cal:
    history = []
    op_dict = {
        '+' : lambda x,y: x+y,
        '-' : lambda x,y: x-y,
        '*' : lambda x,y: x*y,
        '/' : lambda x,y: x/y
    }
    def cal(self, num1, op, num2):
        is_success = True
        try:
            num1,num2 = int(num1),int(num2)
            return self.op_dict[op](num1,num2)
        except ValueError:
            is_success = False
            return '숫자 연산자 숫자로 입력해주세요.'
        except KeyError:
            is_success = False
            return '+-*/ 중 하나의 연산자를 입력해주세요.'
        except ZeroDivisionError:
            is_success = False
            return '0으로는 못 나눕니다.'
        finally:
            if is_success:
                self.history.append((num1,op,num2))

    def again_history(self, idx):
        try:
            return self.cal(*self.history[idx])
        except IndexError:
            return '내역의 범위 밖입니다.'