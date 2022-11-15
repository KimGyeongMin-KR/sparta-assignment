def get_grade(score):
    score = score//10 - 7 if score%10 != 0 else score//10 - 8
    rank = ''
    if score<0:
        rank = 'F'
    else:
        rank = ['C','B','A'][score]
    return rank

# print(get_grade(int(input())))

def mul_two():
    cnt = 0
    while True:
        n = input()
        if n == 'exit':
            print('종료')
            break
        else:
            try:
                n = int(n) * 2
            except ValueError:
                print('숫자만 입력하소')
            else:
                cnt += 1
                print(f'{cnt}번째로 입력한 문자는 {n}입니다')
        if cnt >= 5:
            break
# mul_two()

users = [
    {"name": "Ronald", "age": 30, "math_score": 93, "science_score": 65, "english_score": 93, "social_score": 92},
    {"name": "Amelia", "age": 24, "math_score": 88, "science_score": 52, "english_score": 78, "social_score": 91},
    {"name": "Nathaniel", "age": 28, "math_score": 48, "science_score": 40, "english_score": 49, "social_score": 91},
    {"name": "Sally", "age": 29, "math_score": 100, "science_score": 69, "english_score": 67, "social_score": 82},
    {"name": "Alexander", "age": 30, "math_score": 69, "science_score": 52, "english_score": 98, "social_score": 44},
    {"name": "Madge", "age": 22, "math_score": 52, "science_score": 63, "english_score": 54, "social_score": 47},
    {"name": "Trevor", "age": 23, "math_score": 89, "science_score": 88, "english_score": 69, "social_score": 93},
    {"name": "Andre", "age": 23, "math_score": 50, "science_score": 56, "english_score": 99, "social_score": 54},
    {"name": "Rodney", "age": 16, "math_score": 66, "science_score": 55, "english_score": 58, "social_score": 43},
    {"name": "Raymond", "age": 26, "math_score": 49, "science_score": 55, "english_score": 95, "social_score": 82},
    {"name": "Scott", "age": 15, "math_score": 85, "science_score": 92, "english_score": 56, "social_score": 85},
    {"name": "Jeanette", "age": 28, "math_score": 48, "science_score": 65, "english_score": 77, "social_score": 94},
    {"name": "Sallie", "age": 25, "math_score": 42, "science_score": 72, "english_score": 95, "social_score": 44},
    {"name": "Richard", "age": 21, "math_score": 71, "science_score": 95, "english_score": 61, "social_score": 59},
    {"name": "Callie", "age": 15, "math_score": 98, "science_score": 50, "english_score": 100, "social_score": 74},
] 


def filter_users(users):
    for user in users:
        user_sco = 0
        for k,v in user.items():
            if k in ['name', 'age']:
                continue
            else:
                user_sco += v
        user['avg'] = user_sco/4
    filter_users = [{'age':x['age'],'name':x['name']} for x in users if x['avg'] >= 70]
    return filter_users
                
# print(filter_users(users))