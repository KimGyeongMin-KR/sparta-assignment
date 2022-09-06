# from .calculator import cal << ImportError: attempted relative import with no known parent package
# import calculator
from calculator import cal
print(cal(*tuple(input('숫자 숫자 연산자(+,-,*,/)').split())))