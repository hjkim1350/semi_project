# 중고의 집(Semi Project1)
> - 지역 커뮤니티에서 서로 소통하며 중고 매물을 업로드하고 의견을 주고받는 커뮤니티
> - 사용자 맞춤 세부 서비스: DM 보내기, 팔로우, 좋아요, 댓글/대댓글, 매너온도, 거래장소 지정, 인기 검색어 등

![image](https://user-images.githubusercontent.com/108647811/218964833-5d816153-6171-42d9-92d3-ba7cb88b2e3d.png)

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


### 📚 사용한 API

- 거래장소 지정용 지도 - kakaoMap


### 😎 프로젝트 인원 구성
- 총 5명
- 담당 역할: BackEnd

### 🕶️ 벤치마킹/레퍼런스 사이트

- **당근마켓** https://www.daangn.com/
- **오늘의집** https://ohou.se/


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



### 📱 ERD 설계
![ERD](README.assets/ERD.png)



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


### ✅ 내가 담당한 기능

> **💻 메인 Role - BackEnd: articles App, 검색 기능 및 인기 검색어, 대댓글 기능 구현**
> 
> **💻 서브 Role - FrontEnd: 전반적인 커뮤니티 디자인**

- **articles App CRUD 구현**
- 코드 저장소: https://github.com/hjkim1350/semi_project/tree/master/articles
- 구현 주요 기능
1) 
