from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user  = super().create(validated_data) # 저장하고
        password = user.password
        user.set_password(password) # 지정하고
        user.save() # 다시 저장?
        return user

    # def update(self, vaildated_data): #비밀번호 변경을 따로 만들어서 회원의 일부를 수정가능하게 만드는 법 알기



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        return token