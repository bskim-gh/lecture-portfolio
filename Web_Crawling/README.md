# 웹 크롤링 교육 자료 (Python)

Python을 사용한 웹 크롤링 초급자를 위한 체계적인 교육 자료입니다. BeautifulSoup과 Selenium을 활용하여 정적/동적 웹 페이지에서 데이터를 수집하는 방법을 학습합니다.

> **개발 환경**: Windows 10/11 + Python 3.13

## 📚 교육 과정 개요

본 교육 과정은 웹 크롤링의 기초부터 실전 프로젝트까지 단계적으로 학습할 수 있도록 구성되어 있습니다.

### 학습 목표
- 웹 크롤링의 기본 개념과 원리 이해
- BeautifulSoup을 사용한 HTML 파싱
- Selenium을 활용한 동적 웹 페이지 크롤링
- 데이터 수집, 정제, 저장 기술 습득
- 실전 프로젝트 수행 능력 배양

### 학습 대상
- Python 기초 문법을 이해하는 학습자
- 데이터 수집 업무를 자동화하고 싶은 분
- 웹 개발자, 데이터 분석가 지망생
- 업무 자동화에 관심 있는 비개발자

## 📖 커리큘럼

### Section 1: 웹 크롤링 기초 (01_Section1_웹크롤링기초.py)
**주요 학습 내용:**
- 웹 크롤링이란? (개념, 활용 분야, 주의사항)
- HTTP 프로토콜 기초
- requests 라이브러리 사용법
- 웹 페이지 가져오기
- HTTP 헤더 설정 (User-Agent)
- 타임아웃 및 세션 관리
- URL 파라미터 전달
- 에러 처리
- robots.txt 확인

**학습 시간:** 2-3시간

---

### Section 2: BeautifulSoup 기초 (02_Section2_BeautifulSoup기초.py)
**주요 학습 내용:**
- BeautifulSoup 소개 및 설치
- HTML 파싱 기초
- 태그 선택 방법
  - find(), find_all()
  - 클래스와 ID로 선택
  - 속성 값 가져오기
- 텍스트 추출
- CSS 선택자 사용
  - select(), select_one()
  - 복합 선택자
- 부모/형제 요소 탐색
- 정규표현식 활용

**학습 시간:** 3-4시간

---

### Section 3: BeautifulSoup 실습 (03_Section3_BeautifulSoup실습.py)
**주요 학습 내용:**
- 여러 페이지 크롤링 (페이지네이션)
- 표(Table) 데이터 추출
- 리스트 아이템 수집
- 데이터 정제
  - 가격 문자열 -> 숫자 변환
  - 불필요한 공백 제거
  - 정규표현식 활용
- CSV 파일로 저장
- JSON 파일로 저장
- 링크 추출 및 순회
- URL 변환 (상대 URL -> 절대 URL)
- 에러 처리 및 재시도 로직
- 웹 크롤러 클래스 설계

**학습 시간:** 4-5시간

---

### Section 4: Selenium 기초 (04_Section4_Selenium기초.py)
**주요 학습 내용:**
- Selenium 소개
  - BeautifulSoup vs Selenium
  - 설치 방법 (ChromeDriver)
- Chrome 옵션 설정
  - 헤드리스 모드
  - User-Agent 설정
  - 창 크기 설정
- 드라이버 초기화
- 기본 브라우저 조작
  - 페이지 열기, 뒤로/앞으로 가기
  - 새로고침, 스크린샷
- 요소 찾기 방법
  - By.ID, By.NAME, By.CLASS_NAME
  - By.CSS_SELECTOR, By.XPATH
  - By.TAG_NAME, By.LINK_TEXT
- 요소와 상호작용
  - 텍스트 입력, 클릭
  - 속성 가져오기
- 대기(Wait) 처리
  - Implicit Wait
  - Explicit Wait
  - Expected Conditions
- 드롭다운 선택

**학습 시간:** 4-5시간

---

### Section 5: Selenium 실습 (05_Section5_Selenium실습.py)
**주요 학습 내용:**
- 무한 스크롤 처리
  - scrollTo(), scrollBy()
  - scrollHeight 비교
- Alert/Confirm/Prompt 처리
- iframe 처리
  - switch_to.frame()
  - 상위 프레임으로 복귀
- 새 창/탭 처리
  - window_handles
  - 창 전환
- JavaScript 실행
  - execute_script()
  - DOM 조작
- 마우스 액션
  - ActionChains
  - 드래그 앤 드롭
- 키보드 액션
  - 특수 키 입력
  - 조합키 (Ctrl+A, Ctrl+C 등)
- 쿠키 처리
  - 쿠키 저장 및 로드
  - 로그인 상태 유지
- 스크린샷 및 녹화
- 동적 웹 페이지 크롤러 클래스

**학습 시간:** 5-6시간

---

## 🎯 실전 예제 프로젝트

### 예제 1: 뉴스 수집 프로그램 (예제1_뉴스수집.py)
**내용:**
- 뉴스 사이트에서 기사 제목, 링크, 날짜 수집
- 여러 페이지 순회 (페이지네이션)
- CSV 파일로 저장
- 수집 결과 요약 출력

**활용 분야:**
- 언론사 뉴스 모니터링
- 특정 키워드 뉴스 수집
- 뉴스 트렌드 분석

---

### 예제 2: 상품 가격 비교 프로그램 (예제2_상품가격비교.py)
**내용:**
- 여러 쇼핑몰의 상품 가격 수집
- 가격 데이터 정제 (문자열 -> 숫자)
- 최저가 상품 찾기
- 가격 통계 분석 (평균, 최저가, 최고가)
- JSON 파일로 저장

**활용 분야:**
- 가격 비교 서비스
- 최저가 알림
- 시장 조사

---

### 예제 3: 동적 웹 페이지 크롤링 (예제3_동적웹페이지.py)
**내용:**
- Selenium을 사용한 동적 콘텐츠 수집
- 무한 스크롤 처리
- 로그인 자동화
- JavaScript로 생성되는 데이터 수집
- 스크린샷 저장
- JSON 파일로 저장

**활용 분야:**
- 소셜 미디어 데이터 수집
- SPA(Single Page Application) 크롤링
- 동적 콘텐츠 모니터링

---

## 🚀 시작하기

### 필수 준비물 (Windows 환경)

1. **Python 3.13**
   - 다운로드: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - 설치 시 "Add Python to PATH" 체크

2. **필수 라이브러리 설치**
```bash
# 기본 라이브러리
pip install requests
pip install beautifulsoup4
pip install lxml

# Selenium
pip install selenium

# ChromeDriver 자동 설치 (선택)
pip install webdriver-manager
```

3. **Chrome 브라우저**
   - Selenium 사용 시 필수
   - 최신 버전 설치 권장

4. **텍스트 에디터 또는 IDE**
   - Visual Studio Code (추천)
   - PyCharm
   - Jupyter Notebook

### 실행 방법

#### 기본 실행
```bash
# Section 1 실행
python 01_Section1_웹크롤링기초.py

# Section 2 실행
python 02_Section2_BeautifulSoup기초.py
```

#### 예제 프로젝트 실행
```bash
# 뉴스 수집
python 예제1_뉴스수집.py

# 가격 비교
python 예제2_상품가격비교.py

# 동적 웹 페이지
python 예제3_동적웹페이지.py
```

---

## 📝 학습 방법

### 권장 학습 순서
1. Section 1부터 순서대로 학습
2. 각 섹션의 코드를 직접 실행해보기
3. 코드를 수정하며 동작 원리 파악
4. 실습 문제 풀어보기
5. 예제 프로젝트를 실제 사이트에 적용해보기

### 학습 팁
- **코드를 직접 작성하세요**: 복사-붙여넣기보다 타이핑하며 학습
- **에러 메시지 읽기**: 에러는 학습의 기회입니다
- **실제 웹사이트 분석**: 크롤링하고 싶은 사이트의 HTML 구조 분석
- **단계별 진행**: 작은 부분부터 시작해서 점진적으로 확장
- **법적/윤리적 고려**: 항상 robots.txt와 이용약관 확인

---

## 💡 크롤링 실습 프로젝트 아이디어

### 초급 프로젝트
1. **날씨 정보 수집기**: 기상청 날씨 정보 수집
2. **환율 정보 수집기**: 실시간 환율 데이터 수집
3. **블로그 포스트 수집**: 특정 블로그의 게시글 목록 수집
4. **영화 정보 수집**: 영화 제목, 평점, 개봉일 수집

### 중급 프로젝트
1. **부동산 정보 수집**: 아파트 매매/전세 시세 수집
2. **채용 공고 수집**: 구인 사이트에서 직무별 공고 수집
3. **쇼핑몰 상품 모니터링**: 특정 상품의 가격 변동 추적
4. **SNS 해시태그 분석**: 특정 해시태그의 게시물 수집

### 고급 프로젝트
1. **뉴스 트렌드 분석**: 여러 언론사 뉴스 수집 및 키워드 분석
2. **주식 정보 수집**: 증권사 사이트에서 주식 데이터 수집
3. **학술 논문 수집**: 논문 제목, 초록, 인용 수 수집
4. **경쟁사 모니터링**: 경쟁사 웹사이트 변경사항 추적

---

## 📚 추가 학습 자료

### 온라인 리소스
- [BeautifulSoup 공식 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium 공식 문서](https://www.selenium.dev/documentation/)
- [Requests 라이브러리](https://requests.readthedocs.io/)
- [Real Python - Web Scraping](https://realpython.com/python-web-scraping-practical-introduction/)

### 추천 도서
- "파이썬을 이용한 웹 스크레이핑" - Ryan Mitchell
- "웹 크롤링 & 데이터 분석 with 파이썬"
- "실전 웹 크롤링 & 데이터 분석"

### 유용한 도구
- **Chrome DevTools**: 웹 페이지 구조 분석
- **Selector Gadget**: CSS 선택자 생성
- **XPath Helper**: XPath 표현식 테스트
- **Postman**: API 테스트

---

## ⚖️ 법적/윤리적 고려사항

### 필수 확인 사항
1. **robots.txt 확인**
   - 웹사이트의 크롤링 허용 범위 확인
   - 예: `https://example.com/robots.txt`

2. **이용약관 확인**
   - 웹사이트의 서비스 이용약관 숙지
   - 크롤링 금지 여부 확인

3. **저작권 준수**
   - 수집한 데이터의 저작권 확인
   - 상업적 이용 시 주의

4. **개인정보 보호**
   - 개인정보 수집 금지
   - 민감 정보 처리 시 각별한 주의

### 크롤링 모범 사례
- ✅ 적절한 요청 간격 (서버 부하 방지)
- ✅ User-Agent 명시
- ✅ API 제공 시 API 사용
- ✅ 데이터 활용 목적 명확히
- ❌ 과도한 요청 금지
- ❌ 서버 공격으로 오인될 수 있는 행위 금지

---

## 🔧 자주 발생하는 문제 해결

### 1. requests 관련
```python
# 타임아웃 에러
response = requests.get(url, timeout=10)

# SSL 인증 오류
response = requests.get(url, verify=False)

# 403 Forbidden
headers = {'User-Agent': 'Mozilla/5.0...'}
response = requests.get(url, headers=headers)
```

### 2. BeautifulSoup 관련
```python
# 요소를 찾을 수 없음
# - CSS 선택자 확인
# - 대소문자 확인
# - 동적 로딩 여부 확인 (Selenium 필요)

# 인코딩 문제
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
```

### 3. Selenium 관련
```python
# ChromeDriver 버전 불일치
# -> webdriver-manager 사용
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# 요소를 찾을 수 없음
# -> Explicit Wait 사용
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'myId')))

# 봇 감지
# -> 자동화 감지 우회 옵션 설정
options.add_experimental_option("excludeSwitches", ["enable-automation"])
```

---

## 📊 학습 진도 체크리스트

각 섹션을 완료하면 체크해보세요:

### 기초 과정
- [ ] Section 1: 웹 크롤링 기초
- [ ] Section 2: BeautifulSoup 기초
- [ ] Section 3: BeautifulSoup 실습

### Selenium 과정
- [ ] Section 4: Selenium 기초
- [ ] Section 5: Selenium 실습

### 실전 프로젝트
- [ ] 예제 1: 뉴스 수집
- [ ] 예제 2: 상품 가격 비교
- [ ] 예제 3: 동적 웹 페이지

### 응용 프로젝트
- [ ] 자신만의 크롤링 프로젝트 구현

---

## 🎯 다음 단계

웹 크롤링 기초를 마스터한 후에는:

1. **고급 기술 학습**
   - Scrapy 프레임워크
   - 분산 크롤링
   - 프록시 사용
   - Captcha 우회 (합법적인 경우만)

2. **데이터 처리**
   - Pandas를 사용한 데이터 분석
   - 데이터 시각화 (Matplotlib, Plotly)
   - 데이터베이스 저장 (SQLite, MySQL)

3. **자동화**
   - 스케줄링 (cron, Task Scheduler)
   - 클라우드 배포 (AWS, GCP)
   - API 서버 구축 (Flask, FastAPI)

4. **머신러닝/AI**
   - 수집한 데이터로 ML 모델 학습
   - 자연어 처리 (NLP)
   - 감성 분석

---

## 📞 도움받기

학습 중 어려움이 있다면:
1. 에러 메시지를 구글에 검색
2. Stack Overflow에서 유사한 질문 찾기
3. 공식 문서 참고
4. 코드를 단계별로 나누어 테스트
5. 개발자 도구로 웹 페이지 구조 분석

---

## 📄 라이센스

이 교육 자료는 학습 목적으로 자유롭게 사용 가능합니다.

---

**즐거운 웹 크롤링 학습 되세요! 🕷️🌐✨**

---

## ⚠️ 면책 조항

본 교육 자료는 학습 목적으로 제공됩니다. 웹 크롤링을 수행할 때는:
- 해당 웹사이트의 이용약관을 반드시 확인하세요
- robots.txt 파일을 준수하세요
- 법적 문제가 발생하지 않도록 주의하세요
- 개인정보 및 저작권을 침해하지 마세요

본 교육 자료의 내용을 사용하여 발생하는 모든 법적 책임은 사용자에게 있습니다.

