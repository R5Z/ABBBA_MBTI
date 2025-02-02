</br>
<div align=center>

## 영화 & 친구 추천 시스템 with MBTI 

</br>
MBTI를 바탕으로 한 취향 매칭 서비스 프로젝트
</br>
🔗 프론트 레포 주소
https://github.com/kmg0485/ABBBA_MBTI_front.git
</br></br>

🔗팀 노션
https://www.notion.so/2-730aeb20c24f414f889915f81393c62b

</div>
</br></br></br>

#### **프로젝트 개요**

1. 프로젝트 소개
2. API
3. 프로젝트 주요 기능
4. 프로젝트 마무리
</br></br></br></br>

>### 프로젝트 소개

“MBTI가 어떻게 되세요?” 이런저런 논란도 많지만 관계지향적 문화를 가지고 있는 한국에서는 여전히 핫한 주제입니다. </br>
(2022년 11월 기준 MBTI 검색 구글 트렌드, 지역별 관심도는 여전히 대한민국이 압도적 1위!)</br> 
이 MBTI를 바탕으로 취향이 맞는 영화와 성향이 비슷한 사용자를 추천해주는 서비스를 구현했습니다. 
</br></br></br>

>### 와이어프레임
<img width="883" alt="스크린샷 2022-11-08 11 59 05" src="https://user-images.githubusercontent.com/108252926/200464830-ad798404-04c7-4b4b-b1b2-c9abc5822baa.png">

</br></br></br>

>### ERD
<img width="883" src="https://user-images.githubusercontent.com/18550082/205482639-4d45681c-9895-496f-bbdf-e599a8485326.png">

</br></br></br>

>### API
<img width="1222" alt="스크린샷 2022-11-08 14 09 01" src="https://user-images.githubusercontent.com/108252926/200480210-cd7d8c56-2891-4a21-9620-26f950866458.png">
<img width="1222" alt="스크린샷 2022-11-08 14 09 11" src="https://user-images.githubusercontent.com/108252926/200480223-6887a34d-b70c-4ddc-b056-721bc0d18bcd.png">

</br></br></br>

>### Structure
```
┌─MBTI recommand
├── MBTI                // project
│   ├── urls.py         // base url
│   ├── settings.py     // setting
│   └── ...
├── articles            // app
│   ├── models.py       // DB Model - Article, Comment
│   ├── views.py        // View Functions
│   ├── serializers.py  // Serializers
│   ├── urls.py         // article url
│   └── ...
├── movies              // app
│   ├── models.py       // DB Model - Movie, Movielike
│   ├── views.py        // View Functions
│   ├── serializers.py  // Serializers
│   ├── crawling.py     // crawling movie data
│   ├── loaders_like_user.py
│   ├── loaders_moive.py
│   ├── machine.py      // AI cosine similarity
│   ├── urls.py         // movie url
│   └── ...
├── user                // app
│   ├── models.py       // DB Model - User
│   ├── views.py        // View Functions
│   ├── serializers.py  // Serializers
│   ├── urls.py         // user url
│   └── ...
├── **manage.py**           // 메인
└── requirements.txt
```

</br></br></br>

>### 일정표
<img width="393" alt="스크린샷 2022-11-08 11 59 47" src="https://user-images.githubusercontent.com/108252926/200465161-35293a8e-562d-48ef-968a-70294db1141b.png">


</br></br></br>

>### 프로젝트 주요 기능
</br>

#### 필터링을 이용한 추천 시스템

- ****코사인 유사도(Cosine Similarity)****를 활용하여 나(로그인한 사용자)와 가입된 사용자의 성향 유사도를 파악하여 성향이 맞는 사용자를 추천해줍니다.
- 내가 좋아요한 영화와 비슷한 영화를 추천해줍니다.
- 나와 비슷한 성향의 사용자가 좋아요한 영화도 함께 추천해줍니다.
- MBTI를 필수로 입력받고 나면 추천 페이지는 사이트 어느 곳에서도 접근할 수 있습니다.
</br>

#### 영화 추천과 친구 추천, 좋아요하기

- 시스템에 입력된 영화 중 마음에 드는 영화를 좋아요 할 수 있습니다.
- 내가 좋아요한 영화를 바탕으로 영화와 친구를 추천받을 수 있습니다.
- 추천받은 친구를 팔로우할 수 있습니다.
</br>

#### 프로필에 내 정보 입력하고 친구 추천 받기

- 프로필 편집에서 내 프로필 사진을 업로드하고 MBTI와 Email, 자기소개를 입력하고 저장할 수 있습니다.
- 프로필 저장이 완료되면 친구 추천 목록으로 이동합니다.
</br>

#### 커뮤니티에서 소통하기

- 커뮤니티에서 게시글을 업로드할 수 있고, 다른 사용자가 작성한 글도 확인할 수 있습니다.
- 내가 업로드한 게시글을 수정, 삭제할 수 있습니다.
- 게시글 자세히 보기에서 댓글을 작성하고 수정, 삭제할 수 있습니다.
</br>

#### 내 프로필에서 모아보기

- 내가 좋아요한 영화, 내가 작성한 글과 코멘트 그리고 팔로우한 사용자 목록을 프로필 페이지에서 한 번에 확인할 수 있습니다.
</br>

#### 회원가입 후 서비스 사용 가능

- 아이디 / 비밀번호로 회원 가입과 로그인이 가능합니다. 이미지 게시글 등록과 검색, 댓글 등록과 수정, 삭제 모두 회원가입 후 로그인한 사용자만 사용할 수 있습니다.
- 수정 페이지를 제외한 모든 페이지에서 현재 로그인한 사용자를 확인할 수 있습니다.
- 로그인한 사용자만 좋아요를 누를 수 있습니다.
- 로그아웃된 상태로 접속하면 게시글 업로드 기능과 댓글 업로드 기능을 사용할 수 없습니다.
- 게시글과 댓글 기능에서 작성한 사용자 확인이 가능합니다.
- 동일한 아이디 가입 중복은 막아뒀습니다.
</br>

#### 사용자가 많을수록 추천 성능 👆🏻

- 가입된 사용자가 많아지고, 좋아요와 같은 상호작용을 많이 할수록 추천 성능은 높아집니다.
</br></br></br></br>

>### 프로젝트를 마치며

- 프로젝트를 보시고 궁금하신 점이나 알려주고 싶으신 점은 언제든 공유해주세요!
</br>

****저희는 스파르타코딩클럽 내일배움캠프 3기 5인으로 구성된 팀입니다.****
|**김민규**|오민규|윤민성|윤장미|이금빈|
|:---:|:---:|:---:|:---:|:---:|
|Contact: [:electric_plug:](https://kmg0485.tistory.com/)|Contact: [:bulb:](https://dhalsrbbbbbbb.tistory.com/)|Contact: [:computer:](https://tweakycoding.tistory.com/)|Contact: [:sunglasses:](https://velog.io/@r5zyoon)|Contact: [:sparkling_heart:](https://lgb9811.tistory.com/)|
</br>
</br>
