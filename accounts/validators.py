from django.core.validators import validate_email
from .models import User


def validate_signup(signup_data):
    username = signup_data.get("username")
    password = signup_data.get("password")
    first_name = signup_data.get("first_name")
    last_name = signup_data.get("last_name")
    email = signup_data.get("email")
    nickname = signup_data.get("nickname")
    birthday = signup_data.get("birthday")

    if not all([username, password, first_name, last_name, nickname, email, birthday]):
        return False, "필수 입력값이 누락되었습니다."

    error_messages = []

    if User.objects.filter(username=username).exists():
        error_messages.append("이미 존재하는 username입니다.")

    if len(nickname) > 50:
        error_messages.append("닉네임의 길이는 50자 이하여야 합니다.")

    if len(first_name) > 50:
        error_messages.append("이름이 너무 깁니다.")
    if len(last_name) > 50:
        error_messages.append("성이 너무 깁니다.")

    try:
        validate_email(email)
    except:
        error_messages.append("email 형식이 잘못되었습니다.")
    if User.objects.filter(email=email).exists():
        error_messages.append("이미 존재하는 email입니다.")

    return not bool(error_messages), error_messages
