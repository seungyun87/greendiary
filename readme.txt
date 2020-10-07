greendiary 프로젝트 생성
diary 앱 생성
settings.py 에 등록
greendiary/templates/base.html 생성

8/11
leedy 브랜치 생성
연습 끝

8/11
ksy 브랜치 생성
연습

8/12
ksh 브랜치 생성
연습

8/12
jsh 브랜치 생성
연습

8/13 leedy
account app 생성.
templates/account 생성.
templates/diary 생성.
settings.py 앱 등록, 템플릿 경로 설정.
base.html 안에 block content 작성.
diary관련 html 생성, base 상속 받음.

8/14 ksy
greendiary/settings.py 124~126번째 줄 static 경로 설정.
greendiary/urls.py diary.urls include 설정.
diary/urls.py 생성 및 path(home) 추가.
static/css/style.css 생성.
templates/home.html 생성 및 css 추가, 테스트 문구 추가.
templates/base.html 부트스트랩 navbar 추가, css 추가.

8/14 leedy
☆pip install pillow
settings.py 가장 하단 media 경로 설정.

- login, logout, signup 구현
(html 생성, views작성, url 설정)
- Profile 모델 생성
(signup을 통해 가입하면 함께 생성되도록 설정.
여기에 point를 저장해서 다뤄볼 예정..)
- calendar, diary_create, diary_list 구현
*현재 달력은 모든 글의 썸네일이 보입니다.

위 내용들 테스트를 위해 base.html에 링크.
테스트계정 test01, test02 (pw:likelion)을 만들었습니다.

8/16 ksh
views.py에 DiaryDetail, DiaryEdit, DiaryDelete 구현

8/18 ksh
django버전 2.1.1 => 2.1.5로 업데이트

9/08 ksy
- base.html 전체 메뉴 수정
- base, calendar.css 생성 및 적용

9/09 ksh
-diary_detail.html, diary_delete.html 살짝 구현
-('detail', 'delete', 'edit' ) url 설정

9/09 leedy
diary_detail.html, diary_list.html 수정

<<<<<<< HEAD
9/10 ksh
diary_detail.html, diary_delete.html 수정 (디테일 페이지에 '수정', '삭제' 달았습니다.)
diary_edit.html 구현
setting.py 안에 TIME_ZONE 수정 (우리나라 시간으로 고쳤습니다.)
=======
9/09 ksy
base.css 내용 추가 및 수정
html style 추가 및 수정
>>>>>>> c3f71a7855dd3e1725dacc604c24c0623ca5976a

9/27 ksy
css 아이콘 추가
css 수정

10/6 ksy
회원가입 로그인 로그아웃 페이지 수정
로그인시 안보이기 추가
웹사이트 사이즈 위치 추가

10/7 ksh
diary_news.html 구현 ( 아직 수정할 거 남아있음.)
views.py, url.py를 통해 경로설정 필요함.
