"""
Section 1: 웹 크롤링 기초
- 웹 크롤링이란?
- HTTP 프로토콜 기초
- HTML 구조 이해
- requests 라이브러리 사용
- 기본적인 웹 페이지 가져오기
"""

import requests
from pprint import pprint

print("=" * 50)
print("  Section 1: 웹 크롤링 기초")
print("=" * 50)

# ============================================
# 1. 웹 크롤링이란?
# ============================================
"""
웹 크롤링(Web Crawling)
- 웹 페이지에서 원하는 정보를 자동으로 수집하는 기술
- 웹 스크래핑(Web Scraping)이라고도 함

활용 분야:
- 가격 비교 사이트
- 뉴스 수집 및 분석
- 부동산 정보 수집
- 채용 정보 수집
- 주식/금융 데이터 수집
- 학술 논문 수집

주의사항:
- robots.txt 파일 확인 (크롤링 허용 여부)
- 저작권 및 개인정보 보호법 준수
- 과도한 요청으로 서버에 부하 주지 않기
- 웹사이트 이용약관 확인
"""

# ============================================
# 2. HTTP 프로토콜 기초
# ============================================
def http_basics():
    print("\n" + "=" * 50)
    print("HTTP 프로토콜 기초")
    print("=" * 50)
    
    """
    HTTP (HyperText Transfer Protocol)
    - 웹에서 데이터를 주고받기 위한 프로토콜
    
    주요 메서드:
    - GET: 데이터 조회 (웹 페이지 가져오기)
    - POST: 데이터 전송 (로그인, 폼 제출)
    - PUT: 데이터 수정
    - DELETE: 데이터 삭제
    
    상태 코드:
    - 200: 성공 (OK)
    - 404: 페이지를 찾을 수 없음 (Not Found)
    - 500: 서버 오류 (Internal Server Error)
    - 403: 접근 거부 (Forbidden)
    """
    
    print("\nHTTP 상태 코드 예시:")
    print("200 OK - 요청 성공")
    print("404 Not Found - 페이지를 찾을 수 없음")
    print("500 Internal Server Error - 서버 오류")

# ============================================
# 3. requests 라이브러리 설치 및 사용
# ============================================
def requests_basics():
    print("\n" + "=" * 50)
    print("requests 라이브러리 기초")
    print("=" * 50)
    
    """
    requests 라이브러리 설치:
    pip install requests
    
    주요 기능:
    - HTTP 요청을 쉽게 보낼 수 있음
    - GET, POST 등 다양한 메서드 지원
    - 응답 데이터 파싱
    """
    
    # 간단한 GET 요청
    print("\n[예제 1] 기본 GET 요청")
    try:
        url = "https://www.google.com"
        response = requests.get(url)
        
        print(f"URL: {url}")
        print(f"상태 코드: {response.status_code}")
        print(f"응답 시간: {response.elapsed.total_seconds()}초")
        print(f"인코딩: {response.encoding}")
        print(f"콘텐츠 타입: {response.headers.get('Content-Type')}")
        
    except Exception as e:
        print(f"오류 발생: {e}")

# ============================================
# 4. 웹 페이지 가져오기
# ============================================
def fetch_webpage():
    print("\n" + "=" * 50)
    print("웹 페이지 가져오기")
    print("=" * 50)
    
    # 예제: 간단한 웹 페이지 가져오기
    print("\n[예제 2] 웹 페이지 HTML 가져오기")
    try:
        url = "http://example.com"
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"✅ 성공! 상태 코드: {response.status_code}")
            print("\nHTML 내용 (처음 500자):")
            print("-" * 50)
            print(response.text[:500])
            print("-" * 50)
        else:
            print(f"❌ 실패! 상태 코드: {response.status_code}")
            
    except Exception as e:
        print(f"오류 발생: {e}")

# ============================================
# 5. HTTP 헤더 설정
# ============================================
def set_headers():
    print("\n" + "=" * 50)
    print("HTTP 헤더 설정")
    print("=" * 50)
    
    """
    User-Agent란?
    - 클라이언트(브라우저)의 정보를 서버에 알려주는 헤더
    - 봇으로 인식되어 차단되는 것을 방지
    """
    
    print("\n[예제 3] User-Agent 설정하기")
    
    # 일반적인 브라우저처럼 보이게 하기
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        url = "http://example.com"
        response = requests.get(url, headers=headers)
        
        print(f"URL: {url}")
        print(f"상태 코드: {response.status_code}")
        print("\n설정한 헤더:")
        pprint(headers)
        
    except Exception as e:
        print(f"오류 발생: {e}")

# ============================================
# 6. 타임아웃 설정
# ============================================
def set_timeout():
    print("\n" + "=" * 50)
    print("타임아웃 설정")
    print("=" * 50)
    
    """
    타임아웃이란?
    - 요청이 응답을 받을 때까지 기다리는 시간 제한
    - 서버 응답이 느릴 때 무한 대기 방지
    """
    
    print("\n[예제 4] 타임아웃 설정하기")
    
    try:
        url = "http://example.com"
        response = requests.get(url, timeout=5)  # 5초 제한
        
        print(f"✅ 5초 이내 응답 성공")
        print(f"상태 코드: {response.status_code}")
        
    except requests.Timeout:
        print("❌ 타임아웃! 5초 내에 응답 없음")
    except Exception as e:
        print(f"오류 발생: {e}")

# ============================================
# 7. 세션 사용하기
# ============================================
def use_session():
    print("\n" + "=" * 50)
    print("세션(Session) 사용하기")
    print("=" * 50)
    
    """
    Session이란?
    - 여러 요청에 걸쳐 쿠키와 설정을 유지
    - 로그인 상태 유지에 유용
    - 연결을 재사용하여 성능 향상
    """
    
    print("\n[예제 5] 세션으로 여러 요청하기")
    
    try:
        # 세션 생성
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        })
        
        # 여러 요청 보내기
        urls = [
            "http://example.com",
            "http://example.org",
        ]
        
        for url in urls:
            response = session.get(url, timeout=5)
            print(f"URL: {url}")
            print(f"상태 코드: {response.status_code}")
            print()
        
        # 세션 종료
        session.close()
        print("세션 종료 완료")
        
    except Exception as e:
        print(f"오류 발생: {e}")

# ============================================
# 8. URL 파라미터 전달
# ============================================
def url_parameters():
    print("\n" + "=" * 50)
    print("URL 파라미터 전달")
    print("=" * 50)
    
    """
    URL 파라미터란?
    - URL에 데이터를 전달하는 방법
    - 예: https://example.com/search?q=python&page=1
    """
    
    print("\n[예제 6] 검색 쿼리 파라미터 전달")
    
    # 파라미터 딕셔너리
    params = {
        'q': 'python web crawling',
        'page': 1,
        'limit': 10
    }
    
    # requests가 자동으로 URL 인코딩
    base_url = "https://api.example.com/search"
    
    print(f"기본 URL: {base_url}")
    print(f"파라미터: {params}")
    
    # 실제 요청 URL 생성 예시
    from urllib.parse import urlencode
    full_url = f"{base_url}?{urlencode(params)}"
    print(f"\n완성된 URL: {full_url}")

# ============================================
# 9. 에러 처리
# ============================================
def error_handling():
    print("\n" + "=" * 50)
    print("에러 처리")
    print("=" * 50)
    
    """
    주요 예외:
    - requests.ConnectionError: 네트워크 연결 오류
    - requests.Timeout: 타임아웃
    - requests.HTTPError: HTTP 오류
    - requests.RequestException: 일반적인 요청 오류
    """
    
    print("\n[예제 7] 안전한 요청 처리")
    
    def safe_request(url):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # 4xx, 5xx 에러 발생
            return response
        
        except requests.ConnectionError:
            print(f"❌ 연결 오류: {url}")
        except requests.Timeout:
            print(f"❌ 타임아웃: {url}")
        except requests.HTTPError as e:
            print(f"❌ HTTP 오류: {e}")
        except Exception as e:
            print(f"❌ 알 수 없는 오류: {e}")
        
        return None
    
    # 테스트
    urls = [
        "http://example.com",
        "http://thisurldoesnotexist12345.com",
    ]
    
    for url in urls:
        print(f"\n요청: {url}")
        result = safe_request(url)
        if result:
            print(f"✅ 성공: {result.status_code}")

# ============================================
# 10. robots.txt 확인
# ============================================
def check_robots_txt():
    print("\n" + "=" * 50)
    print("robots.txt 확인")
    print("=" * 50)
    
    """
    robots.txt란?
    - 웹 크롤러에게 크롤링 규칙을 알려주는 파일
    - 웹사이트 루트에 위치: https://example.com/robots.txt
    
    주요 지시어:
    - User-agent: 적용 대상 봇
    - Disallow: 크롤링 금지 경로
    - Allow: 크롤링 허용 경로
    - Crawl-delay: 요청 간 대기 시간
    """
    
    print("\n[예제 8] robots.txt 가져오기")
    
    try:
        url = "https://www.naver.com/robots.txt"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print(f"✅ {url}")
            print("\nrobots.txt 내용 (처음 20줄):")
            print("-" * 50)
            lines = response.text.split('\n')[:20]
            for line in lines:
                print(line)
            print("-" * 50)
        
    except Exception as e:
        print(f"오류 발생: {e}")

# ============================================
# Main 실행
# ============================================
if __name__ == "__main__":
    http_basics()
    requests_basics()
    fetch_webpage()
    set_headers()
    set_timeout()
    use_session()
    url_parameters()
    error_handling()
    check_robots_txt()
    
    print("\n" + "=" * 50)
    print("  Section 1 완료!")
    print("=" * 50)

"""
실습 문제:

1. 원하는 웹사이트의 robots.txt 파일을 가져와서 출력하세요.

2. 다음 웹사이트들의 상태 코드를 확인하는 프로그램을 작성하세요:
   - https://www.google.com
   - https://www.naver.com
   - https://www.daum.net

3. 세션을 사용하여 5개의 웹사이트를 순차적으로 방문하고
   각각의 응답 시간을 측정하세요.

4. 타임아웃을 3초로 설정하고, 느린 웹사이트 접근 시
   적절한 에러 메시지를 출력하는 함수를 작성하세요.

5. User-Agent를 다양하게 설정하여 요청을 보내고
   서버의 응답이 달라지는지 확인하세요.
"""

