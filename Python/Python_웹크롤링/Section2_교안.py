"""
Section 2- 기본 스크랩핑 실습
==============================

주요 내용:
- urllib를 이용한 GET 방식 데이터 통신
- urlopen() 함수로 웹 페이지 정보 읽기
- geturl(), status, getheaders(), getcode() 메서드
- URL 파싱 및 쿼리 파라미터 처리
- urlencode()를 이용한 파라미터 인코딩
- API 호출 및 JSON 응답 처리
- 행정안전부 RSS API 연동
- 다음 주식 정보 API 크롤링
- fake_useragent를 이용한 User-Agent 설정
- Referer 헤더 설정
"""

import urllib.request
import urllib.parse
from urllib.parse import urlparse
import json
from fake_useragent import UserAgent


# ====================================
# 1. 기본 GET 요청 - encar
# ====================================

def get_request_basic():
    """기본 GET 요청 및 응답 정보 확인"""
    # 기본 요청1(encar)
    url = "http://www.encar.com/"

    mem = urllib.request.urlopen(url)

    # 여러 정보
    print('type : {}'.format(type(mem)))
    print("geturl : {}".format(mem.geturl()))
    print("status : {}".format(mem.status))
    print("headers : {}".format(mem.getheaders()))
    print("getcode : {}".format(mem.getcode()))
    print("read : {}".format(mem.read(1).decode('utf-8'))) # 바이트 수
    print('parse : {}'.format(urlparse('http://www.encar.co.kr?test=test').query))


# ====================================
# 2. GET 방식 파라미터 전달 - ipify API
# ====================================

def get_request_with_params():
    """GET 방식으로 파라미터를 전달하여 API 호출"""
    # 기본 요청2(ipify)
    API = "https://api.ipify.org"

    # Get 방식 Parameter
    values = {
        'format': 'json'
    }

    print('before param : {}'.format(values))
    params = urllib.parse.urlencode(values)
    print('after param : {}'.format(params))

    # 요청 URL 생성
    url = API + "?" + params
    print("요청 url= {}".format(url))

    # 수신 데이터 읽기
    data = urllib.request.urlopen(url).read()

    # 수신 데이터 디코딩
    text = data.decode("utf-8")
    print('response : {}'.format(text))


# ====================================
# 3. GET 방식 데이터 통신 - RSS
# ====================================

def get_rss_data():
    """행정안전부 RSS API 연속 호출"""
    # 행정 안전부 : https://www.mois.go.kr
    # 행정 안전부 RSS API URL
    API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

    params = []

    for num in [1001, 1012, 1013, 1014]:
        params.append(dict(ctxCd=num))

    # 연속해서 4회 요청
    for c in params:
        # 파라미터 출력
        # print(c)
        # URL 인코딩
        param = urllib.parse.urlencode(c)
        # URL 완성
        url = API + "?" + param
        # URL 출력
        print("url=", url)
        # 요청
        res_data = urllib.request.urlopen(url).read()
        # 수신 후 디코딩
        contents = res_data.decode("utf-8")
        # 출력
        print(contents)


# ====================================
# 4. 다음 주식 정보 API 크롤링
# ====================================

def get_daum_stock_info():
    """다음 주식 정보 API에서 실시간 주식 순위 가져오기"""
    # Fake Header 정보(가상으로 User-Agent 생성)
    ua = UserAgent()

    # 헤더 선언
    headers = {
        'User-Agent': ua.ie,
        'referer': 'https://finance.daum.net/'
    }

    # 다음 주식 요청 URL
    url = "https://finance.daum.net/api/search/ranks?limit=10"

    # 요청
    res = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read().decode('utf-8')

    # 응답 데이터 확인(Json Data)
    # print('res', res)

    # 응답 데이터 str -> json 변환 및 data 값 저장
    rank_json = json.loads(res)['data']

    # 중간 확인
    print('중간 확인 : ', rank_json, '\n')

    for elm in rank_json:
        # print(type(elm)) #Type 확인
        print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm['tradePrice'], elm['name']), )


# 실행 예제
if __name__ == '__main__':
    # 1. 기본 GET 요청
    get_request_basic()
    
    # 2. GET 파라미터 전달
    get_request_with_params()
    
    # 3. RSS 데이터 가져오기
    get_rss_data()
    
    # 4. 다음 주식 정보 크롤링
    get_daum_stock_info()

