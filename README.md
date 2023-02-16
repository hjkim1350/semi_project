# 중고의 집(Semi Project1)
> - 지역 커뮤니티에서 서로 소통하며 중고 매물을 업로드하고 의견을 주고받는 커뮤니티
> - 사용자 맞춤 세부 서비스: DM 보내기, 팔로우, 좋아요, 댓글/대댓글, 매너온도, 거래장소 지정, 인기 검색어 등

![image](https://user-images.githubusercontent.com/108647811/218964833-5d816153-6171-42d9-92d3-ba7cb88b2e3d.png)

<br>

## 🔨 프로젝트 기간
- 2022.10.31(MON) ~ 2022.11.07(MON), ** 총 8일 **

<div>
    <h3>📚 사용한 기술 STACKS</h3>
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
    <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
    <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
    <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
    <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
</div>

<br>

### 📚 사용한 API

- 거래장소 지정용 지도 - kakaoMap

<br>

### 😎 프로젝트 인원 구성
- 총 5명
- 담당 역할: BackEnd

<br>

### 🕶️ 벤치마킹/레퍼런스 사이트

- **당근마켓** https://www.daangn.com/
- **오늘의집** https://ohou.se/

<br>

### ⚛️ 기능 설계

- **회원관리**
  - 회원가입
  - 로그인
  - 로그아웃
  - 회원 프로필
  - 팔로우 / 취소
  - 블랙리스트
- **지역 커뮤니티**
  - 이미지 업로드
  - 글 수정 / 삭제
  - 좋아요 / 취소
  - 댓글 작성 / 수정 / 삭제 / 신고
  - 대댓글 작성 / 수정 / 삭제 / 신고
- **상품**
  - 이미지 업로드
  - 글 수정 / 삭제
  - 좋아요 / 취소
  - 판매 위치 또는 택배 거래 유무
  - 판매자가 파는 다른 상품 소개
  - 매너온도
- **채팅**
- **검색**
  - 인기 검색어 순위
- **문의하기**
  - 문의 제목
  - 문의 글
  - 사진 업로드 (선택)
  - 자주 묻는 질문 (후순위)

<br>

### 📱 ERD 설계
![ERD](README.assets/ERD.png)

<br>

### 📁 주요 source 파일 트리구조

```text
┌─📁 semi_pjt_1 (프로젝트 - setting 파일)
├─📁 accounts (회원관리 App)
├─📁 articles (사용자 커뮤니티 App)
├─📁 products (중고물품 판매 게시판 App)
├─📁 chats (채팅 App)
├─📁 service_center (서비스센터 및 CS 상담 App)
├─🗒️ .gitignore (env, 가상환경 파일 git ignore)
└─🗒️ requirements.txt (pip 패키지 목록)
```

<br>

### ✅ 내가 담당한 기능

> **💻 메인 Role - BackEnd: articles App(CRUD, 이미지, 좋아요/싫어요, 대댓글, 검색어, 인기검색어 출력) 구현**
- 코드 저장소: https://github.com/hjkim1350/semi_project/tree/master/articles
- 구현 주요 기능
  - CRUD: 글 제목, 내용, 작성시간, 마지막 수정시간, 이미지, 사용자명, 좋아요 사용자수, 싫어요 사용자수, 조회수
  - 이미지의 경우 ProcessedImageField를 이용하여 모델을 정의하고 서버 내에 이미지를 저장하고 저장된 위치의 링크만 DB table에 저장하도록 하여, 이미지를 업로드할 때 저장된 서버의 링크를 읽어들여 이미지를 출력하도록 함
  - 좋아요 사용자수와 싫어요 사용자 수는 별도의 칼럼을 두어 각자 카운팅하도록 함
  - 댓글 model에 parent_comment 칼럼 추가하여 기존 모델을 활용하면서 대댓글 달도록 기능 구현, 즉 대댓글의 경우 대댓글 칼럼에 index 값이 부여되며 일반 댓글일 경우 대댓글 칼럼이 null
  - 검색어의 경우 테이블을 생성하여 검색어, 검색 일시, 검색 횟수를 저장하며 검색 횟수를 역순으로 정렬하여 가장 많은 조회수 Top5를 출력하도록 함


> **💻 서브 Role - FrontEnd: 전반적인 커뮤니티 디자인**
- ** article App 화면 디자인 **
![image](https://user-images.githubusercontent.com/108647811/218971994-297db4ee-ed43-42d9-acc6-b7ca94bfc6c4.png)

<br>

### ⌨️ 프로젝트 후기
교육 시작하고 아무 가이드 없이 빈 화면에서 시작한 첫 프로젝트였다. 교육 때 배웠던 CRUD, 좋아요, 팔로우를 기본틀로 잡고 지도API, 채팅, 싫어요 사용자수, 대댓글이라는 부가적인 기능을 올리기 시작하면서 많은 검색과 코드 이해를 필요로 했다. 사실 CRUD 수업을 할때 개념을 듣고 "그렇구나"라고 이해를 하다가도 막상 처음부터 코딩을 하라그러면 굉장히 막막했다. 프로젝트를 시작하니 새로운 기능을 업로드하기 위해서는 기존의 코드를 이해해야 새로운 기능을 올릴 수 있었기 때문에 어떻게 CRUD가 구현되는지 그 원리를 깊게 들여다볼 수 있었다. 이래서 주변에서 자율 프로젝트를 반드시하라고 조언을 해줬다는걸 깨달은 프로젝트였다.
