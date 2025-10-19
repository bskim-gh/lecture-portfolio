"""
Section 3 - Requests 라이브러리
===============================

주요 내용:
- requests 라이브러리를 이용한 HTTP 통신
- Session 객체 생성 및 활용
- 쿠키(Cookie) 설정 및 전송
- User-Agent 헤더 정보 설정
- stream 옵션을 이용한 대용량 데이터 수신
- JSON 데이터 파싱 및 처리
- iter_lines()를 이용한 라인별 데이터 처리
- REST API 메서드: GET, POST, PUT, DELETE
- raise_for_status()를 이용한 HTTP 상태 체크
- RequestsCookieJar를 이용한 쿠키 관리
- timeout 설정
- jsonplaceholder API 활용
- GitHub API 호출
"""

import json
import requests


# ====================================
# 1. Requests Session 기본 사용법
# ====================================

def session_basic():
    """세션 활성화 및 기본 사용법"""
    # 세션 활성화
    s = requests.Session()
    # r = s.get('https://www.naver.com')

    # 수신 데이터
    # print('1', r.text)

    # 수신 상태 코드
    # print('Status Code : {}'.format(r.status_code))

    # 확인
    # print('OK? : {}'.format(r.ok))

    # 세션 비활성화
    # s.close()

    s = requests.Session()

    # 쿠키 Return
    # r = s.get('http://httpbin.org/cookies', cookies={'name': 'niceman'})
    # print(r.text)

    # 쿠키 Set
    # r = s.get('http://httpbin.org/cookies/set', cookies={'name': 'niceman'})
    # print(r.text)

    # User-Agent
    # url = 'http://httpbin.org/get'
    # headers = {'user-agent': 'niceman_app_v1.0.0'}

    # Header 정보 전송
    # r = s.get(url, headers=headers)
    # print(r.text)

    # 세션 비활성화
    s.close()

    # With 문 사용
    with requests.Session() as s:
        pass
        # r = s.get('https://www.naver.com')
        # print(r.text)


# ====================================
# 2. JSON 데이터 스트리밍 처리
# ====================================

def json_streaming():
    """대용량 JSON 데이터를 스트림으로 처리"""
    s = requests.Session()

    # 100개 Json 데이터 요청
    r = s.get('http://httpbin.org/stream/100', stream=True)

    # 수신 확인
    # print(r.text)

    # Encoding 확인
    # print('Encoding : {}'.format(r.encoding))

    # 데이터 타입 확인
    # print(type(r))

    # Encoding 타입 체크 후 UTF-8 변경
    if r.encoding is None:
        r.encoding = 'UTF-8'

    # 수신 데이터 -> Dict 변환
    for line in r.iter_lines(decode_unicode=True):
        # 라인 출력 후 타입 확인
        # print(line)
        # print(type(line))
        
        # Json(Dict) 변환 후 타입 확인
        b = json.loads(line)
        # print(b)
        # print(type(b))
        
        # 정보 내용 출력
        for k, v in b.items():
            pass
            # print("Key: {}, Values: {}".format(k, v))
        # 줄 바꿈
        print()
        print()

    s.close()


# ====================================
# 3. JSON Placeholder API 사용
# ====================================

def json_placeholder_api():
    """JSON Placeholder API를 이용한 데이터 조회"""
    s = requests.Session()

    # r = s.get('https://jsonplaceholder.typicode.com/posts')
    r = s.get('https://jsonplaceholder.typicode.com/posts/1')

    # Header 정보
    print(r.headers)
    # 본문 정보
    print(r.text)
    # Json 변환
    print(r.json())
    # Key 반환
    print(r.json().keys())
    # Value 반환
    print(r.json().values())
    # 인코딩 정보
    print(r.encoding)
    # 바이너리 정보
    print(r.content)

    s.close()


# ====================================
# 4. REST API 메서드 사용 (GET, POST, PUT, DELETE)
# ====================================

def rest_api_methods():
    """REST API의 다양한 메서드 사용 예제"""
    # Rest API GET, POST, DELETE, PUT:UPDATE, REPLACE (FETCH : UPDATE, MODIFY)
    # https://jsonplaceholder.typicode.com/posts

    # 세션 활성화
    s = requests.Session()

    # *예제1* - GET
    # 요청1
    r = s.get('https://api.github.com/events')

    # 수신 상태 체크
    r.raise_for_status()  # 또는 status_code 체크

    # 출력
    print(r.text)

    # *예제2* - 쿠키 설정
    # 쿠키 설정
    jar = requests.cookies.RequestsCookieJar()

    # 쿠키 삽입
    jar.set('name', 'niceman', domain='httpbin.org', path='/cookies')

    # 요청2
    r = s.get('http://httpbin.org/cookies', cookies=jar)

    # 출력
    print(r.text)

    # *예제3* - Timeout 설정
    # 요청3
    r = s.get('https://github.com', timeout=5)

    # 출력
    print(r.text)

    # *예제4* - POST
    # 요청4
    r = s.post('http://httpbin.org/post', data={'kim': 'stellar'}, cookies=jar)

    # 출력
    print(r.text)

    # 헤더 정보
    print(r.headers)

    # *예제5* - POST (여러 형식)
    # 요청5(POST)
    payload1 = {'name': 'kim', 'pay': 'true'}
    payload2 = (('name', 'park'), ('pay', 'false'))

    r = s.post("http://httpbin.org/post", data=payload2)

    # 출력
    print(r.text)

    # *예제6* - PUT
    # 요청5(PUT)
    r = s.put('http://httpbin.org/put', data={'data': '{"name": "Kim", "grade": "A"}'})

    # 출력
    print(r.text)

    # *예제7* - DELETE (httpbin)
    # 요청6(DELETE)
    r = s.delete('http://httpbin.org/delete')

    # 출력
    print(r.text)

    # *예제8* - DELETE (jsonplaceholder)
    # 요청7(DELETE)
    r = s.delete('https://jsonplaceholder.typicode.com/posts/1')
    print(r.text)

    s.close()


# 실행 예제
if __name__ == '__main__':
    # 1. 세션 기본 사용
    session_basic()
    
    # 2. JSON 스트리밍
    json_streaming()
    
    # 3. JSON Placeholder API
    json_placeholder_api()
    
    # 4. REST API 메서드
    rest_api_methods()

