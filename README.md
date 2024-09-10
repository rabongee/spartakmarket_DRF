# spartakmarket_DRF

## 프로젝트 소개
Django를 이용해서 개발했던 spartamarket의 백엔드 부분을 DRF 형식으로 재구현

##  개발기간
- 2024.09.04.(수) ~ 2024.09.09.(월)

## 개발환경
- Language : Python 3.10.11
- IDE : Visual Studio Code
- Framework : Django 4.2, Django Rest Framework

## ERD
![ER다이어그램](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_ER%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8.drawio.png)

## API 명세
|기능|method type|Endpoint|
|---|---|------|
|회원가입|POST|/api/accounts/|
|회원 탈퇴|DELETE|/api/accounts/|
|로그인|POST|/api/accounts/login/|
|로그아웃|POST|/api/accounts/logout/|
|프로필 조회|GET|/api/accounts/<str:username>/|
|본인 정보 수정|PUT|/api/accounts/<str:username>/|
|패스워드 변경|PUT|/api/accounts/password/|
|상품 등록|POST|/api/products/|
|상품 목록 조회|GET|/api/products/|
|상품 상세 조회|GET|/api/products/<int:productId>/|
|상품 수정|PUT|/api/products/<int:productId>/|
|상품 삭제|DELETE|/api/products/<int:productId>/|

## 주요 기능



