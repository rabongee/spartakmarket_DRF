from django.core.validators import validate_email
from datetime import datetime
from .models import User


def validate_signup(signup_data):
    username = signup_data.get("username")
    password = signup_data.get("password")
    first_name = signup_data.get("first_name")
    last_name = signup_data.get("last_name")
    email = signup_data.get("email")
    nickname = signup_data.get("nickname")
    birthday = signup_data.get("birthday")
    gender = signup_data.get("gender")
    self_introduction = signup_data.get("self_introduction")

    if not all([username, password, first_name, last_name, nickname, email, birthday]):
        return False, "필수 입력값이 누락되었습니다."

    error_messages = []

    if User.objects.filter(username=username).exists():
        error_messages.append({"username": "이미 존재하는 username입니다."})

    if len(nickname) > 50:
        error_messages.append({"nickname": "닉네임의 길이는 50자 이하여야 합니다."})

    if len(first_name) > 50:
        error_messages.append({"first_name": "이름이 너무 깁니다."})
    if len(last_name) > 50:
        error_messages.append({"last_name": "성이 너무 깁니다."})

    try:
        validate_email(email)
    except:
        error_messages.append({"email": "email 형식이 잘못되었습니다."})
    if User.objects.filter(email=email).exists():
        error_messages.append({"email": "이미 존재하는 email입니다."})

    try:
        datetime.strptime(birthday, '%Y-%m-%d')
    except:
        error_messages.append({"birthday": "생일 형식은 YYYY-MM-DD여야 합니다."})

    return not bool(error_messages), error_messages


def validate_update_user(user_data):
    username = user_data.get("username")
    first_name = user_data.get("first_name")
    last_name = user_data.get("last_name")
    email = user_data.get("email")
    nickname = user_data.get("nickname")
    birthday = user_data.get("birthday")
    gender = user_data.get("gender")
    self_introduction = user_data.get("self_introduction")

    error_messages = []

    if username and User.objects.filter(username=username).exists():
        error_messages.append({"username": "이미 존재하는 username입니다."})

    if nickname and len(nickname) > 50:
        error_messages.append({"nickname": "닉네임의 길이는 50자 이하여야 합니다."})

    if first_name and len(first_name) > 50:
        error_messages.append({"first_name": "이름이 너무 깁니다."})
    if last_name and len(last_name) > 50:
        error_messages.append({"last_name": "성이 너무 깁니다."})

    if email:
        try:
            validate_email(email)
        except:
            error_messages.append({"email": "email 형식이 잘못되었습니다."})
        if User.objects.filter(email=email).exists():
            error_messages.append({"email": "이미 존재하는 email입니다."})

    if birthday:
        try:
            datetime.strptime(birthday, '%Y-%m-%d')
        except:
            error_messages.append({"birthday": "생일 형식은 YYYY-MM-DD여야 합니다."})

    return not bool(error_messages), error_messages
