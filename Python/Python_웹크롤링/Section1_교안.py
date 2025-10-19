"""
Section 1 - Python 크롤링 기초
==============================

주요 내용:
- urllib.request 모듈을 이용한 파일 다운로드
- urlretrieve() 함수로 이미지/HTML 파일 저장
- urlopen() 함수로 웹 리소스 읽기
- HTTP 상태 코드 및 헤더 정보 확인
- HTTPError, URLError 예외 처리
- lxml 라이브러리를 사용한 HTML 파싱
- CSS 선택자와 XPath를 이용한 데이터 추출
- 네이버 메인 뉴스 스탠드 스크랩핑
- requests + lxml을 이용한 웹 스크랩핑
"""

import urllib.request as req
from urllib.error import URLError, HTTPError
import requests
import lxml.html
from lxml.html import fromstring, tostring


# ====================================
# 1. urllib - urlretrieve를 이용한 파일 다운로드
# ====================================

def download_with_urlretrieve():
    """urlretrieve를 사용한 이미지 및 HTML 파일 다운로드"""
    # 파일 URL
    img_url = "http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
    html_url = "http://google.com"

    # 다운받을 경로
    save_path1 = "c:/test1.jpg"
    save_path2 = "c:/index.html"

    # 예외 처리
    try:
        file1, header1 = req.urlretrieve(img_url, save_path1)
        file2, header2 = req.urlretrieve(html_url, save_path2)
    except Exception as e:
        print("Download failed.")
        print(e)
    else:
        # Header 정보 출력
        # print(header1)
        # print(header2)
        
        # 다운로드 파일 정보
        print("Filename1 {}".format(file1))
        print("Filename2 {}".format(file2))
        print()
        
        # 성공
        print("Download Succeed.")


# ====================================
# 2. urllib - urlopen을 이용한 파일 다운로드
# ====================================

def download_with_urlopen():
    """urlopen을 사용한 파일 다운로드 및 상태 정보 출력"""
    # 다운로드 경로 및 파일명
    path_list = ["c:/bskim02_test.jpg", "c:/index.html"]

    # 다운로드 리소스 URL
    target_url = ["http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg",
                  "http://google.com"]

    for i, url in enumerate(target_url):
        # 예외 처리
        try:
            # 웹 수신 정보 읽기
            response = req.urlopen(url)
            
            # 수신 내용
            contents = response.read()

            print('---------------------------------------------------')

            # 상태 정보 중간 출력
            print('Header Info-{} : {}'.format(i, response.info()))
            print('HTTP Status Code : {}'.format(response.getcode()))
            print()
            print('---------------------------------------------------')

            # 파일 쓰기
            with open(path_list[i], 'wb') as c:
                c.write(contents)

            # HTTP 에러 발생 시
        except HTTPError as e:
            print("Download failed.")
            print('HTTPError Code : ', e.code)

            # URL 에러 발생 시
        except URLError as e:
            print("Download failed.")
            print('URL Error Reason : ', e.reason)

            # 성공
        else:
            print()
            print("Download Succeed.")


# ====================================
# 3. lxml 사용 기초 스크랩핑(1) - CSS 선택자
# ====================================

def scrape_naver_news_cssselect():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 - CSS 선택자 사용
    """
    # 세션 사용 권장
    # session = requests.Session()
    # session.get('https://www.naver.com/')

    # 스크랩핑 대상 URL
    response = requests.get('https://www.naver.com/')
    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page_css(response)
    # 결과 출력
    for url in urls:
        print(url)


def scrape_news_list_page_css(response):
    """CSS 선택자를 이용한 뉴스 리스트 추출"""
    # URL 리스트 선언
    urls = []
    # 태그 정보 문자열 저장
    root = lxml.html.fromstring(response.content)

    # 문서내 경로 절대 경로 변환
    # root.make_links_absolute(response.url)

    for a in root.cssselect('.api_list .api_item a.api_link'):
        # 링크 
        url = a.get('href')
        # 리스트 삽입
        urls.append(url)
    return urls


# ====================================
# 4. lxml 사용 기초 스크랩핑(2) - XPath
# ====================================

def scrape_naver_news_xpath():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 - XPath 사용
    """
    # 세션 사용
    session = requests.Session()

    # 스크랩핑 대상 URL
    response = session.get('http://www.naver.com/')
    # 신문사 정보 딕셔너리 획득
    urls = scrape_news_list_page_xpath(response)

    # 딕셔너리 확인
    # print(urls)

    # 결과 출력
    for name, url in urls.items():
        print(name, url)


def scrape_news_list_page_xpath(response):
    """XPath를 이용한 뉴스 리스트 추출"""
    # URL 딕셔너리 선언
    urls = {}
    # 태그 정보 문자열 저장
    root = fromstring(response.content)

    # 문서내 경로 절대 경로 변환
    root.make_links_absolute(response.url)

    for a in root.xpath('//ul[@class="api_list"]/li[@class="api_item"]/a[@class="api_link"]'):
        # a 구조 확인
        # print(dir(a))

        # a 문자열 출력
        # print(tostring(a, pretty_print=True))

        # 신문사, 링크 추출 함수
        name, url = extract_contents(a)

        # 딕셔너리 삽입
        urls[name] = url
    return urls


def extract_contents(dom):
    """DOM에서 신문사명과 링크 추출"""
    # 링크 주소
    link = dom.get('href')
    # dom 구조 확인
    # print(tostring(dom, pretty_print=True))

    # 신문사 명
    name = dom.xpath('./img')[0].get('alt')  # xpath('./img')
    return name, link


# 실행 예제
if __name__ == '__main__':
    # 1. urlretrieve 예제
    download_with_urlretrieve()
    
    # 2. urlopen 예제
    download_with_urlopen()
    
    # 3. lxml CSS 선택자 예제
    scrape_naver_news_cssselect()
    
    # 4. lxml XPath 예제
    scrape_naver_news_xpath()

