from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
from .validators import validate_signup


class SingupView(APIView):
    def post(self, request):
        is_valid, error_message = validate_signup(request.data)
        print(is_valid, error_message)
        if not is_valid:
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=request.data.get("username"),
            password=request.data.get("password"),
            first_name=request.data.get("first_name"),
            last_name=request.data.get("last_name"),
            email=request.data.get("email"),
            nickname=request.data.get("nickname"),
            birthday=request.data.get("birthday"),
        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data.get(
            "username"), password=request.data.get("password"))
        if not user:
            return Response({"error": "아이디나 비밀번호가 틀립니다."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        res_data = serializer.data

        refresh = RefreshToken.for_user(user)
        res_data['refresh_token'] = str(refresh)
        res_data['access_token'] = str(refresh.access_token)
        return Response(res_data)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        if user == request.user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"message": "로그인한 유저와 다릅니다."})
