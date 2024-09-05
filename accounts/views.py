from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
