from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
from .validators import (
    validate_signup, validate_update_user, validate_change_password)


class AccountsView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]

    def post(self, request):
        is_valid, error_message = validate_signup(request.data)
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
            gender=request.data.get("gender"),
            self_introduction=request.data.get("self_introduction"),
        )
        serializer = UserSerializer(user)
        res_data = serializer.data
        refresh = RefreshToken.for_user(user)
        res_data['refresh_token'] = str(refresh)
        res_data['access_token'] = str(refresh.access_token)
        return Response(res_data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        password = request.data.get('password')
        user = request.user
        if not user.check_password(password):
            return Response({"error": "비밀번호가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

        user.soft_delete()
        return Response({"message": "회원탈퇴에 성공했습니다."})


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


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token_str = request.data.get("refresh_token")
        try:
            refresh_token = RefreshToken(refresh_token_str)
        except TokenError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        refresh_token.blacklist()
        return Response({"message": "성공적으로 로그아웃 되었습니다."})


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        is_valid, error_message = validate_change_password(request.data, user)
        if not is_valid:
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

        new_password = request.data.get('new_password')
        user.set_password(new_password)
        user.save()
        return Response({"message": "패스워드가 변경에 성공했습니다."})


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        if user == request.user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"message": "로그인한 유저와 다릅니다."}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, username):
        user = get_object_or_404(User, username=username)
        if user == request.user:
            is_valid, error_message = validate_update_user(request.data)
            if not is_valid:
                return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)

        else:
            return Response({"message": "수정 권한이 없습니다."}, status=status.HTTP_401_UNAUTHORIZED)
