# Python 웹 크롤링 교육 과정

## 📚 과정 개요

본 교육 과정은 Python을 활용한 웹 크롤링과 웹 스크래핑의 기초부터 고급 기법까지 체계적으로 학습하는 실무 중심 과정입니다. urllib, requests, BeautifulSoup, Selenium 등 다양한 라이브러리를 활용하여 정적/동적 웹 페이지의 데이터를 수집하고 처리하는 방법을 배웁니다.

**총 5개 Section**으로 구성된 웹 크롤링 전문 교육 커리큘럼

---

## 📖 Section 구성

### Section 1: Python 크롤링 기초

**주요 내용:**
- **urllib.request 모듈**
  - urlretrieve() - 파일 직접 다운로드
  - urlopen() - 웹 리소스 읽기
  - HTTP 상태 코드 확인
  - 헤더 정보 확인 (info(), getheaders())
  - getcode() - 응답 코드 확인

- **예외 처리**
  - HTTPError - HTTP 에러 처리
  - URLError - URL 에러 처리
  - try-except 구문 활용

- **lxml 라이브러리**
  - fromstring() - HTML 파싱
  - tostring() - HTML 문자열 변환
  - cssselect() - CSS 선택자로 요소 선택
  - xpath() - XPath 표현식으로 요소 선택

- **실습 예제**
  - 이미지 파일 다운로드
  - HTML 파일 다운로드
  - 네이버 메인 뉴스 스탠드 스크랩핑
  - requests + lxml 조합 활용

**학습 포인트:**
- 웹 크롤링의 기본 개념 이해
- urllib를 활용한 파일 다운로드
- lxml을 활용한 HTML 파싱

---

### Section 2: 기본 스크랩핑 실습

**주요 내용:**
- **urllib를 이용한 GET 방식 데이터 통신**
  - urlopen() 기본 사용법
  - geturl() - 요청 URL 확인
  - status - HTTP 상태 코드
  - getheaders() - 모든 헤더 정보
  - getcode() - 응답 코드

- **URL 파싱 및 파라미터 처리**
  - urlparse() - URL 구조 분석
  - urlencode() - 파라미터 인코딩
  - 쿼리 스트링 생성

- **API 호출**
  - ipify API - IP 주소 조회
  - 행정안전부 RSS API
  - 다음 주식 정보 API
  - JSON 응답 처리

- **fake_useragent**
  - User-Agent 랜덤 생성
  - 브라우저 인식 회피
  - Referer 헤더 설정

**실습 예제:**
- encar 웹사이트 접근
- ipify API로 IP 주소 조회
- RSS 피드 수집
- 다음 주식 정보 크롤링

**학습 포인트:**
- GET 방식 HTTP 통신
- API 호출 및 JSON 처리
- User-Agent 설정의 중요성

---

### Section 3: Requests 라이브러리

**주요 내용:**
- **Requests 라이브러리 기본**
  - Session 객체 생성 및 활용
  - get(), post(), put(), delete() 메서드
  - 응답 객체 (Response)
    - status_code - 상태 코드
    - text - 텍스트 응답
    - content - 바이트 응답
    - json() - JSON 파싱

- **Session 관리**
  - 쿠키 설정 및 전송
  - RequestsCookieJar 활용
  - 로그인 세션 유지

- **헤더 설정**
  - User-Agent 헤더
  - Referer 헤더
  - Custom 헤더

- **대용량 데이터 처리**
  - stream 옵션
  - iter_lines() - 라인별 처리
  - iter_content() - 청크별 처리

- **REST API 메서드**
  - GET - 데이터 조회
  - POST - 데이터 생성
  - PUT - 데이터 수정
  - DELETE - 데이터 삭제

- **예외 처리**
  - raise_for_status() - HTTP 에러 체크
  - timeout 설정
  - 네트워크 에러 처리

**실습 예제:**
- jsonplaceholder API 활용
- GitHub API 호출
- JSON 스트리밍 처리
- Session을 이용한 쿠키 관리

**학습 포인트:**
- Requests의 강력한 기능
- RESTful API 호출 방법
- Session을 활용한 상태 유지

---

### Section 4: BeautifulSoup

**주요 내용:**
- **BeautifulSoup 기초**
  - BeautifulSoup 객체 생성
  - html.parser 파서 사용
  - prettify() - 코드 정리

- **태그 접근 방법**
  - 계층 구조 접근 (html.body.h1)
  - next_sibling - 다음 태그
  - parent - 부모 태그
  - children - 자식 태그
  - next_elements - 다음 요소들

- **find() / find_all() 메서드**
  - 태그 이름으로 검색
  - 클래스로 검색 (class_)
  - ID로 검색 (id)
  - 속성으로 검색 (attrs)
  - 텍스트로 검색 (string)
  - 정규표현식 활용

- **CSS 선택자**
  - select() - 다중 선택
  - select_one() - 단일 선택
  - 자식 선택자 (>)
  - ID 선택자 (#)
  - 클래스 선택자 (.)
  - 속성 선택자 ([])
  - nth-of-type() 선택자

- **데이터 추출**
  - .text - 텍스트 추출
  - .string - 문자열 추출
  - ['속성'] - 속성 값 추출
  - get() - 속성 값 가져오기

**실습 예제:**
- 네이버 이미지 검색 크롤링
- 이미지 다운로드 및 저장
- 다나와 로그인 처리
- 로그인 후 페이지 이동

**학습 포인트:**
- HTML 파싱의 핵심 기술
- CSS 선택자의 강력함
- 실전 크롤링 구현

---

### Section 5: Selenium

**주요 내용:**
- **Selenium 기본**
  - WebDriver 설정 (Chrome, Firefox)
  - Chrome WebDriver 경로 설정
  - 브라우저 제어 기본

- **브라우저 제어**
  - get() - 페이지 이동
  - set_window_size() - 창 크기 조절
  - maximize_window() - 최대화
  - minimize_window() - 최소화

- **대기 시간 설정**
  - implicitly_wait() - 암묵적 대기
  - WebDriverWait - 명시적 대기
  - expected_conditions (EC)
    - presence_of_element_located
    - element_to_be_clickable
    - visibility_of_element_located

- **페이지 정보 확인**
  - page_source - HTML 소스
  - session_id - 세션 ID
  - title - 페이지 제목
  - current_url - 현재 URL
  - get_cookies() - 쿠키 정보

- **요소 찾기**
  - find_element_by_id()
  - find_element_by_name()
  - find_element_by_class_name()
  - find_element_by_css_selector()
  - find_element_by_xpath()

- **요소 조작**
  - send_keys() - 입력
  - click() - 클릭
  - submit() - 폼 제출
  - clear() - 지우기

- **스크린샷**
  - save_screenshot() - 파일 저장
  - get_screenshot_as_file()
  - get_screenshot_as_png()

- **Headless 모드**
  - chrome_options 설정
  - --headless 옵션
  - 백그라운드 실행

- **BeautifulSoup 조합**
  - Selenium으로 페이지 로드
  - page_source를 BeautifulSoup으로 파싱
  - 동적 콘텐츠 크롤링

**실습 예제:**
- 다나와 노트북 상품 크롤링
- 페이지 이동 크롤링
- 엑셀(xlsxwriter)로 결과 저장
- 이미지 다운로드 및 엑셀 삽입

**학습 포인트:**
- 동적 웹 페이지 크롤링의 핵심
- JavaScript 렌더링 페이지 처리
- 실무 수준의 크롤링 구현

---

## 🎯 학습 포인트

### 크롤링 기술 스택
1. **urllib**: 기본 HTTP 통신, 파일 다운로드
2. **requests**: 고급 HTTP 통신, Session 관리
3. **lxml**: 빠른 HTML 파싱, XPath 지원
4. **BeautifulSoup**: 쉬운 HTML 파싱, CSS 선택자
5. **Selenium**: 동적 페이지 크롤링, 브라우저 자동화

### 크롤링 전략
- **정적 페이지**: requests + BeautifulSoup
- **동적 페이지**: Selenium + BeautifulSoup
- **API 활용**: requests + JSON 처리
- **대용량 데이터**: stream 옵션, iter_lines()

### 윤리와 법률
- **robots.txt 준수**: 크롤링 가능 여부 확인
- **요청 빈도 제한**: time.sleep() 활용
- **User-Agent 설정**: 신원 확인
- **저작권 준수**: 데이터 사용 범위
- **서버 부하 고려**: 적절한 요청 간격

---

## 📊 권장 학습 순서

### 1단계: 기초 (1주)
- **Section 1**: urllib 기초
- 목표: 웹 크롤링 개념 이해, 파일 다운로드

### 2단계: HTTP 통신 (1주)
- **Section 2-3**: GET/POST 통신, Requests 라이브러리
- 목표: HTTP 통신 완전 숙달, API 호출

### 3단계: HTML 파싱 (1-2주)
- **Section 4**: BeautifulSoup
- 목표: CSS 선택자 활용, 데이터 추출

### 4단계: 동적 크롤링 (2주)
- **Section 5**: Selenium
- 목표: 동적 페이지 크롤링, 브라우저 자동화

### 5단계: 실전 프로젝트 (2-3주)
- 실제 웹사이트 크롤링 프로젝트
- 데이터 수집 → 전처리 → 저장 → 분석

---

## 💡 학습 방법

### 효과적인 학습 전략
1. **작은 사이트부터**: 간단한 구조의 웹사이트부터 시작
2. **개발자 도구 활용**: Chrome DevTools로 HTML 구조 분석
3. **단계별 접근**: 페이지 접근 → HTML 파싱 → 데이터 추출
4. **에러 처리**: 예외 상황에 대한 철저한 대비
5. **윤리적 크롤링**: robots.txt 확인, 적절한 요청 간격

### 실습 루틴
- **Step 1**: 대상 웹사이트 분석 (HTML 구조, CSS 클래스)
- **Step 2**: 크롤링 코드 작성
- **Step 3**: 데이터 추출 및 검증
- **Step 4**: 데이터 저장 (CSV, Excel, DB)
- **Step 5**: 에러 처리 및 최적화

---

## 🛠️ 필요한 라이브러리

```bash
# HTTP 통신
pip install requests urllib3

# HTML 파싱
pip install beautifulsoup4 lxml

# 동적 크롤링
pip install selenium

# User-Agent 생성
pip install fake-useragent

# 데이터 저장
pip install pandas openpyxl xlsxwriter

# 추가 도구
pip install pillow  # 이미지 처리
```

### 웹 드라이버 설치
```bash
# ChromeDriver 다운로드
# https://chromedriver.chromium.org/

# 또는 webdriver-manager 사용
pip install webdriver-manager
```

---

## 📂 파일 구조

```
Python_웹크롤링/
├── Section1_교안.py (urllib, lxml 기초)
├── Section2_교안.py (기본 스크랩핑)
├── Section3_교안.py (Requests 라이브러리)
├── Section4_교안.py (BeautifulSoup)
└── Section5_교안.py (Selenium)
```

---

## 🎯 크롤링 실습 프로젝트

### 초급 프로젝트
- 블로그 포스트 제목/본문 수집
- 뉴스 기사 헤드라인 수집
- 날씨 정보 수집

### 중급 프로젝트
- 쇼핑몰 상품 정보 수집
- 부동산 매물 정보 수집
- 주식 가격 정보 수집

### 고급 프로젝트
- 소셜 미디어 데이터 수집
- 이미지 대량 다운로드
- 로그인 필요한 사이트 크롤링
- 페이지네이션 자동 처리

---

## 🔒 크롤링 주의사항

### 법적 이슈
- **저작권법**: 수집한 데이터의 저작권 확인
- **개인정보보호법**: 개인정보 수집 금지
- **전기통신사업법**: 서비스 방해 금지
- **약관 확인**: 웹사이트 이용 약관 준수

### 기술적 고려사항
- **robots.txt**: 크롤링 허용 범위 확인
- **요청 빈도**: time.sleep()로 간격 조절
- **User-Agent**: 적절한 식별자 사용
- **에러 처리**: 네트워크 에러, HTTP 에러 대비
- **IP 차단 대비**: 프록시 사용, 요청 간격 증가

---

## 📚 추가 학습 자료

### 공식 문서
- **requests**: https://requests.readthedocs.io/
- **BeautifulSoup**: https://www.crummy.com/software/BeautifulSoup/
- **Selenium**: https://selenium-python.readthedocs.io/
- **lxml**: https://lxml.de/

### 유용한 도구
- **Chrome DevTools**: HTML 구조 분석
- **Postman**: API 테스트
- **Regex101**: 정규표현식 테스트
- **CSS Selector Tester**: CSS 선택자 테스트

---

## 📝 정리

본 교육 과정은 Python을 활용한 웹 크롤링의 모든 것을 다룹니다. urllib의 기초부터 Selenium을 활용한 고급 동적 크롤링까지, 실무에서 바로 활용할 수 있는 실전 기술을 학습합니다.

**주요 특징:**
- 기초부터 고급까지 체계적 학습
- 다양한 라이브러리 활용법
- 실전 프로젝트 중심 교육
- 윤리적 크롤링 강조

**학습 후 가능한 것:**
- 정적/동적 웹 페이지 크롤링
- API를 통한 데이터 수집
- 이미지/파일 자동 다운로드
- 크롤링 데이터 DB/Excel 저장
- 웹 자동화 프로그램 개발

각 Section의 예제를 직접 실습하고, 자신만의 크롤링 프로젝트를 만들어보세요!

