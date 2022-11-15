from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import CustomTokenObtainPairSerializer, UserSerializer#, UserProfileSerializer
from .models import User

# Create your views here.

class UserView(APIView):
    # def get(self, request):
    #     users = request.user
    #     serializer = UserSerializer(users)
    #     return Response(serializer.data)
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'회원 가입이 완료되었습니다'}, status=status.HTTP_201_CREATED)
        else:
            return Response({"msg" : f"{serializer.errors}"}, status = status.HTTP_400_BAD_REQUEST)





from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


