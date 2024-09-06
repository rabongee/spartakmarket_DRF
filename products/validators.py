from .models import Product


def validate_create(create_data):
    title = create_data.get("title")
    content = create_data.get("content")
    image = create_data.get("image")

    if not all([title, content, image]):
        return False, "필수 입력값이 누락되었습니다."

    if len(title) > 30:
        return False, {"title": "제목의 길이는 30자 이하여야 합니다."}

    return True, None
