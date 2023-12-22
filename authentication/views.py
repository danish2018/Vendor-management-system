from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserLoginSerializer,UserRegistraionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Create your views here.
class UserRegistrationView(APIView):
    def post(self,request):
        serializer = UserRegistraionSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({"token":token,"Msg":"User Created Successfully"},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email = email , password = password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({"Token":token,"msg":"Login Sucess"},status = status.HTTP_200_OK)
            return Response({"Error":"Email or password is not valid"})
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

