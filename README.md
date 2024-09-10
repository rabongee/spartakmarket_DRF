# spartakmarket_DRF

## 프로젝트 소개
Django를 이용해서 개발했던 spartamarket의 백엔드 부분을 DRF 형식으로 일부 재구현

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
기능별 넣어야 하는 이미지가 너무 많아 성공 사진으로 대체함
### 1️⃣ 회원 기능
회원 가입 : url로 요청이 들어오면 유효성 검증을 진행한 뒤에 유저 정보를 데이터베이스에 반영하고 가입한 유저 정보와 access token, refresh token을 같이 줌.
![회원 가입](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_project_image/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%EC%84%B1%EA%B3%B5.png)

회원 탈퇴 : 패스워드 검증을 진행한 후에 데이터베이스에서 유저 계정을 비활성화 시킴으로써 회원 탈퇴 기능을 구현.
![회원 탈퇴](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_project_image/%ED%9A%8C%EC%9B%90%20%ED%83%88%ED%87%B4%20%EC%84%B1%EA%B3%B5.png)

로그인 : 유저네임과 패스워드를 입력받아서 데이터베이스의 정보와 일치하다면 로그인.
![로그인](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_project_image/%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%84%B1%EA%B3%B5.png)

로그아웃 : 로그아웃 요청시 refresh token을 블랙리스트에 등록함.
![로그아웃](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_project_image/%EB%A1%9C%EA%B7%B8%EC%95%84%EC%9B%83%20%EC%84%B1%EA%B3%B5.png)

프로필 조회 : 로그인한 유저가 자신의 프로필을 확인할 수 있음, 다른 유저가 접근시 유저가 다르다고 알려줌.
![프로필 조회](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_project_image/%ED%94%84%EB%A1%9C%ED%95%84%20%EC%A1%B0%ED%9A%8C%20%EC%84%B1%EA%B3%B5.png)

본인 정보 수정 : 로그인 한 사용자만 본인 프로필 수정 가능. 수정된 이메일은 기존 다른 사용자의 이메일과 username은 중복되면 안 됨.
![본인 정보 수정](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_project_image/%EB%B3%B8%EC%9D%B8%20%EC%A0%95%EB%B3%B4%20%EC%88%98%EC%A0%95%20%EC%84%B1%EA%B3%B5.png)

패스워드 변경 : 패스워드 규칙 검증 후에 데이터베이스에 반영.
![패스워드 변경](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_project_image/%ED%8C%A8%EC%8A%A4%EC%9B%8C%EB%93%9C%20%EB%B3%80%EA%B2%BD%20%EC%84%B1%EA%B3%B5.png)

### 2️⃣ 상품 기능
상품 등록 : 로그인 상태, 제목과 내용, 상품 이미지 입력 필요. 데이터 검증 후에 데이터베이스에 반영함.
![상품 등록](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_project_image/%EC%83%81%ED%92%88%20%EB%93%B1%EB%A1%9D%20%EC%84%B1%EA%B3%B5.png)

상품 목록 조회 : 로그인 상태 불필요. 데이터베이스에 있는 상품 목록 전체를 가져옴.
![상품 목록 조회](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_project_image/%EC%83%81%ED%92%88%20%EB%AA%A9%EB%A1%9D%20%EC%A1%B0%ED%9A%8C%20%EC%84%B1%EA%B3%B5.png)

상품 상세 조회 : 로그인 상태 필요. 요청된 URL에 맞는 productId를 가진 상품을 가져옴.
![상품 상세 조회](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_project_image/%EC%83%81%ED%92%88%20%EC%83%81%EC%84%B8%20%EC%A1%B0%ED%9A%8C%20%EC%84%B1%EA%B3%B5.png)

상품 수정 : 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능. 검증 후에 데이터베이스에 반영함.
![상품 수정](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_project_image/%EC%83%81%ED%92%88%20%EC%88%98%EC%A0%95%20%EC%84%B1%EA%B3%B5.png)

상품 삭제 : 로그인 상태, 삭제 권한 있는 사용자(게시글 작성자)만 가능. 삭제가 성공하면 productId번의 게시물이 삭제되었다고 알려줌.
![상품 삭제](https://github.com/rabongee/spartamarket_DRF/blob/dev/DRF_project_image/%EC%83%81%ED%92%88%20%EC%82%AD%EC%A0%9C%20%EC%84%B1%EA%B3%B5.png)

