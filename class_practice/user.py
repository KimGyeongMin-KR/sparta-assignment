
class User:
    def __init__(self):
        self.profile = {
            'name': '',
            'birth_year_day': '',
            'phone' : '',
            'sex' : '',
            'local' : '',
            'email' : ''
        }
    def user_set_profile(self):
        for i in self.profile.keys():
            self.profile[i] = input(f'What is your {i}?')
    def hard_set_profile(self,profile):
        self.profile = profile