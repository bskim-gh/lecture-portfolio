"""
Section 4 - BeautifulSoup
=========================

주요 내용:
- BeautifulSoup 라이브러리를 이용한 HTML 파싱
- prettify()를 이용한 코드 정리
- 태그 접근 방법 (html.body.h1, html.body.p)
- next_sibling을 이용한 다음 태그 접근
- find(), find_all() 메서드
- 클래스, ID, 속성을 이용한 태그 검색
- CSS 선택자 (select(), select_one())
- 자식 선택자 (>), ID 선택자 (#), 속성 선택자 ([])
- nth-of-type() 선택자
- 네이버 이미지 검색 크롤링
- fake_useragent를 이용한 User-Agent 설정
- 이미지 다운로드 및 저장
- 폴더 생성 및 예외 처리
- 다나와 로그인 처리
- Session을 이용한 로그인 유지
- 로그인 후 페이지 이동 및 데이터 추출
"""

import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests as req2


# ====================================
# 1. BeautifulSoup 기초 사용법
# ====================================

def beautifulsoup_basic():
    """BeautifulSoup 기본 사용법 및 태그 접근"""
    # 테스트 html (response data 또는 파일에서 읽어온 data로 가정)
    html = """
    <html>
    <head>
    <title>The Dormouse's story</title>
    </head>
    <body>
    <h1>this is h1 area</h1>
    <h2>this is h2 area</h2>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
    <a data-io="link3" href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
    </p>
    <p class="story">story...</p>
    </body>
    </html>
    """

    # 예제1(Beautiful 기초)
    # bs4 초기화
    soup = BeautifulSoup(html, 'html.parser')

    # 타입 확인
    print('soup', type(soup))

    # 코드 정리
    print('prettify', soup.prettify())

    # h1 태그 접근
    h1 = soup.html.body.h1
    print('h1', h1)

    # p 태그 접근
    p1 = soup.html.body.p
    print('p1', p1)

    # 다음 태그
    p2 = p1.next_sibling.next_sibling
    print('p2', p2)

    # 텍스트 출력1
    print("h1 >> ", h1.string)

    # 텍스트 출력2
    print("p >> ", p1.string)

    # 함수 확인
    print(dir(p2))

    # 다음 엘리먼트 확인
    print(list(p2.next_elements))

    # 반복 출력 확인
    for v in p2.next_elements:
        print(v)


# ====================================
# 2. Find, Find_all 메서드
# ====================================

def beautifulsoup_find():
    """find, find_all 메서드를 이용한 태그 검색"""
    html = """
    <html>
    <head>
    <title>The Dormouse's story</title>
    </head>
    <body>
    <h1>this is h1 area</h1>
    <h2>this is h2 area</h2>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
    <a data-io="link3" href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
    </p>
    <p class="story">story...</p>
    </body>
    </html>
    """

    # 예제2(Find, Find_all)
    # bs4 초기화
    soup = BeautifulSoup(html, 'html.parser')

    # a 태그 모두 선택
    links1 = soup.find_all("a")  # limit=2
    # 타입 확인
    print('links', type(links1))
    # 리스트 요소 확인
    print(links1)
    # dir 확인
    print(dir(links1))

    links2 = soup.find_all("a", class_='sister')  # id="link2" , string="Tillie" , string=["Elsie","Tillie"] , {} 다중 조건
    print(links2)

    for t in links1:
        print("link1 >> ", t.text)

    # 처음 발견한 a 태그 선택
    link1 = soup.find("a")  # find 연결 가능
    print('links', type(link1))
    # 리스트 요소 확인
    print(link1)
    # dir 확인
    print(dir(link1))
    # 태그 텍스트 출력
    print(link1.string)
    print(link1.text)

    # 다중 조건
    link2 = soup.find("a", {"class": "sister", "data-io": "link3"})
    # 출력
    print(link2)


# ====================================
# 3. Select, Select_one 메서드 (CSS 선택자)
# ====================================

def beautifulsoup_select():
    """CSS 선택자를 이용한 태그 검색"""
    html = """
    <html>
    <head>
    <title>The Dormouse's story</title>
    </head>
    <body>
    <h1>this is h1 area</h1>
    <h2>this is h2 area</h2>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
    <a data-io="link3" href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
    </p>
    <p class="story">story...</p>
    </body>
    </html>
    """

    # 예제3(Select, Select_one)
    # bs4 초기화
    soup = BeautifulSoup(html, 'html.parser')

    # CSS 선택자 중요
    # 태그 + 클래스 + 자식 선택자
    link1 = soup.select_one("p.title > b")
    # 태그 + id 선택자
    link2 = soup.select_one("a#link1")
    # 태그 + 속성 선택자
    link3 = soup.select_one("a[data-io='link3']")

    # 전체 구조 및 텍스트 출력
    print(link1)
    print(link1.string)
    print(link2)
    print(link2.string)
    print(link3)
    print(link3.string)

    # 선택자에 맞는 전체 선택
    # 태그 + 클래스 + 자식
    link4 = soup.select("p.story > a")
    # 태그 + 클래스 + 자식 + 태그 + 순서
    link5 = soup.select("p.story > a:nth-of-type(2)")
    # 태그 + 클래스
    link6 = soup.select("p.story")

    # 전체 구조 및 텍스트 출력
    print(link4)
    print(link5)
    print(link6[1])


# ====================================
# 4. 네이버 이미지 검색 크롤링 및 다운로드
# ====================================

def naver_image_download():
    """네이버 이미지 검색 결과를 크롤링하여 다운로드"""
    # Header 정보 초기화
    opener = req.build_opener()
    # User-Agent 정보
    opener.addheaders = [('User-agent', UserAgent().ie)]
    # Header 정보 삽입
    req.install_opener(opener)

    # 네이버 이미지 기본 URL(크롬 개발자 도구)
    base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
    # 검색어
    quote = rep.quote_plus("신소율")
    # URL 완성
    url = base + quote

    # 요청 URL 확인
    # print('Request URL : {}'.format(url))

    # Request
    res = req.urlopen(url)

    # 이미지 저장 경로
    savePath = "C:/imagedown/"  # C:\\imagedown\\

    # 폴더 생성 예외처리 (문제 발생 시 프로그램 종료)
    try:
        # 기존 폴더가 있는지 체크
        if not (os.path.isdir(savePath)):
            # 없으면 폴더 생성
            os.makedirs(os.path.join(savePath))
    except OSError as e:
            # 에러 내용
            print("folder creation failed!")
            print("folder name : {}".format(e.filename))
            
            # 런타임 에러 raise
            raise RuntimeError('System Exit!')
    else:
        # 폴더 생성 정상일 경우 실행
        print('folder is created!')

    # bs4 초기화
    soup = BeautifulSoup(res, "html.parser")

    # select 사용
    img_list = soup.select("div.img_area > a.thumb._thumb > img")

    # find_all 사용 할 경우
    # img_list1 = soup.find_all("a", class_='thumb _thumb')
    #
    # print(type(img_list1))
    # for v in img_list1:
    #     img_t = v.find('img')
    #     print(dir(img_t))
    #     print(img_t.attrs['data-source'])

    # 이미지 번호를 붙여주면서 다운로드
    for i, img_list in enumerate(img_list, 1):
        # 속성 확인
        # print(img_list['data-source'])

        # 저장 파일명 및 경로
        fullFileName = os.path.join(savePath, savePath + str(i) + '.png')
        # 파일명 출력 
        # print('full name : {}'.format(fullFileName))
        
        # 다운로드 요청(URL, 저장경로)
        req.urlretrieve(img_list['data-source'], fullFileName)

    # 다운로드 완료 시 출력
    print("download succeeded!")


# ====================================
# 5. 다나와 로그인 처리
# ====================================

def danawa_login():
    """다나와 사이트 로그인 및 세션 유지"""
    # Login 정보(개발자 도구)
    login_info = {
        'redirectUrl': 'http://www.danawa.com/',
        'loginMemberType': 'general',
        'id': 'bskim02_id',
        'password': 'bskim02_pwd'
    }

    # Headers 정보
    headers = {
        'User-Agent': UserAgent().chrome,
        'Referer': 'https://auth.danawa.com/login?url=http%3A%2F%2Fcws.danawa.com%2Fpoint%2Findex.php'
    }

    with req2.session() as s:
        # Request(로그인 시도)
        res = s.post('https://auth.danawa.com/login', login_info, headers=headers)
        
        # 로그인 시도 실패시 예외
        if res.status_code != 200:
            raise Exception('Login failed.')
        
        # 본문 수신 데이터 확인
        # print(res.content.decode('UTF-8'))

        # 로그인 성공 후 세션 정보를 가지고 페이지 이동
        res = s.get('https://buyer.danawa.com/order/Order/orderList', headers=headers)

        # EUC-KR (한글 깨질 경우)
        # res.encoding = 'euc-kr'

        # 페이지 이동 수신 데이터 확인
        # print(res.text)

        # bs4 초기화
        soup = BeautifulSoup(res.text, "html.parser")

        # 로그인 성공 체크
        check_name = soup.find('p', class_="user")
        # print(check_name)
        
        if check_name is None:
            raise Exception('Login failed. Wrong Password.')
        
        # 선택자 사용
        info_list = soup.select("div.my_info > div.sub_info > ul.info_list > li")
        
        # 확인
        # print(info_list)

        # 이부분에서 재요청, 파일다운로드, DB 저장 등의 작업

        # 제목
        print()
        print('***** My info *****')

        for v in info_list:
            # 속성 메소드 확인
            # print(dir(v))
            
            # 필요한 텍스트 추출
            proc, val = v.find('span').string.strip(), v.find('strong').string.strip()
            
            # 최종 출력
            print('{} : {}'.format(proc, val))


# 실행 예제
if __name__ == '__main__':
    # 1. BeautifulSoup 기초
    beautifulsoup_basic()
    
    # 2. Find, Find_all 메서드
    beautifulsoup_find()
    
    # 3. CSS 선택자
    beautifulsoup_select()
    
    # 4. 네이버 이미지 다운로드
    naver_image_download()
    
    # 5. 다나와 로그인
    danawa_login()

