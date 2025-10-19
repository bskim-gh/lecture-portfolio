"""
Section 4: Selenium 기초
- Selenium 소개 및 설치
- 웹 드라이버 설정
- 기본 브라우저 조작
- 요소 찾기 및 상호작용
- 동적 콘텐츠 처리
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

print("=" * 50)
print("  Section 4: Selenium 기초")
print("=" * 50)

# ============================================
# 1. Selenium 소개
# ============================================
"""
Selenium이란?
- 웹 브라우저를 자동화하는 도구
- 동적 웹 페이지 크롤링에 적합
- JavaScript로 생성되는 콘텐츠 수집 가능
- 사용자 행동 시뮬레이션 가능

BeautifulSoup vs Selenium:
- BeautifulSoup: 정적 HTML 파싱 (빠름, 가벼움)
- Selenium: 동적 콘텐츠, 사용자 상호작용 (느림, 무거움)

설치 방법:
pip install selenium

Chrome WebDriver 설치:
1. Chrome 버전 확인
2. ChromeDriver 다운로드
3. PATH에 추가 또는 경로 지정

또는 자동 설치:
pip install webdriver-manager
"""

# ============================================
# 2. Chrome 옵션 설정
# ============================================
def setup_chrome_options():
    print("\n" + "=" * 50)
    print("Chrome 옵션 설정")
    print("=" * 50)
    
    print("\n[예제 1] Chrome 옵션")
    
    # Chrome 옵션 객체 생성
    options = Options()
    
    # 헤드리스 모드 (브라우저 창을 띄우지 않음)
    # options.add_argument('--headless')
    
    # 창 크기 설정
    options.add_argument('--window-size=1920,1080')
    
    # User-Agent 설정
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    # GPU 비활성화 (안정성 향상)
    options.add_argument('--disable-gpu')
    
    # 샌드박스 비활성화
    options.add_argument('--no-sandbox')
    
    # DevTools 비활성화
    options.add_argument('--disable-dev-shm-usage')
    
    # 이미지 로딩 비활성화 (속도 향상)
    # prefs = {'profile.managed_default_content_settings.images': 2}
    # options.add_experimental_option('prefs', prefs)
    
    # 알림 비활성화
    options.add_argument('--disable-notifications')
    
    # 자동화 감지 우회
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    print("Chrome 옵션 설정 완료")
    print("- 창 크기: 1920x1080")
    print("- User-Agent 설정")
    print("- 알림 비활성화")
    print("- 자동화 감지 우회")
    
    return options

# ============================================
# 3. 드라이버 초기화
# ============================================
def initialize_driver():
    print("\n" + "=" * 50)
    print("드라이버 초기화")
    print("=" * 50)
    
    print("\n[예제 2] WebDriver 생성")
    
    """
    # 방법 1: 수동으로 ChromeDriver 경로 지정
    service = Service('C:/path/to/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    
    # 방법 2: webdriver-manager 사용 (자동)
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # 방법 3: 환경변수 PATH에 있는 경우
    driver = webdriver.Chrome(options=options)
    """
    
    print("드라이버 생성 방법:")
    print("1. 수동 경로 지정")
    print("2. webdriver-manager 사용 (추천)")
    print("3. PATH 환경변수 사용")
    
    try:
        options = setup_chrome_options()
        # driver = webdriver.Chrome(options=options)
        print("\n✅ 드라이버 초기화 준비 완료")
        # return driver
    except Exception as e:
        print(f"❌ 에러: {e}")
        return None

# ============================================
# 4. 기본 브라우저 조작
# ============================================
def basic_browser_control():
    print("\n" + "=" * 50)
    print("기본 브라우저 조작")
    print("=" * 50)
    
    print("\n[예제 3] 브라우저 제어 명령")
    
    """
    # 페이지 열기
    driver.get('https://www.example.com')
    
    # 현재 URL 가져오기
    current_url = driver.current_url
    
    # 페이지 제목 가져오기
    title = driver.title
    
    # 뒤로 가기
    driver.back()
    
    # 앞으로 가기
    driver.forward()
    
    # 새로고침
    driver.refresh()
    
    # 창 크기 조절
    driver.set_window_size(1920, 1080)
    
    # 최대화
    driver.maximize_window()
    
    # 스크린샷 저장
    driver.save_screenshot('screenshot.png')
    
    # 페이지 소스 가져오기
    page_source = driver.page_source
    
    # 브라우저 종료
    driver.close()  # 현재 탭만
    driver.quit()   # 모든 창
    """
    
    commands = [
        "driver.get(url) - 페이지 열기",
        "driver.current_url - 현재 URL",
        "driver.title - 페이지 제목",
        "driver.back() - 뒤로 가기",
        "driver.forward() - 앞으로 가기",
        "driver.refresh() - 새로고침",
        "driver.maximize_window() - 창 최대화",
        "driver.save_screenshot() - 스크린샷",
        "driver.quit() - 브라우저 종료"
    ]
    
    print("\n주요 브라우저 제어 명령:")
    for cmd in commands:
        print(f"  • {cmd}")

# ============================================
# 5. 요소 찾기 방법
# ============================================
def find_elements():
    print("\n" + "=" * 50)
    print("요소 찾기 방법")
    print("=" * 50)
    
    print("\n[예제 4] 요소 선택자")
    
    """
    By 클래스 사용 (Selenium 4+):
    
    # ID로 찾기
    element = driver.find_element(By.ID, 'username')
    
    # Name으로 찾기
    element = driver.find_element(By.NAME, 'email')
    
    # Class name으로 찾기
    element = driver.find_element(By.CLASS_NAME, 'btn-primary')
    
    # Tag name으로 찾기
    element = driver.find_element(By.TAG_NAME, 'h1')
    
    # CSS Selector로 찾기
    element = driver.find_element(By.CSS_SELECTOR, '#container > div.content')
    
    # XPath로 찾기
    element = driver.find_element(By.XPATH, '//div[@class="content"]')
    
    # Link text로 찾기
    element = driver.find_element(By.LINK_TEXT, '로그인')
    
    # Partial link text로 찾기
    element = driver.find_element(By.PARTIAL_LINK_TEXT, '로그')
    
    # 여러 요소 찾기 (복수)
    elements = driver.find_elements(By.CLASS_NAME, 'item')
    """
    
    selectors = [
        ("By.ID", "ID 속성으로 찾기"),
        ("By.NAME", "Name 속성으로 찾기"),
        ("By.CLASS_NAME", "Class 이름으로 찾기"),
        ("By.TAG_NAME", "태그 이름으로 찾기"),
        ("By.CSS_SELECTOR", "CSS 선택자로 찾기"),
        ("By.XPATH", "XPath로 찾기"),
        ("By.LINK_TEXT", "링크 텍스트로 찾기"),
        ("By.PARTIAL_LINK_TEXT", "부분 링크 텍스트로 찾기"),
    ]
    
    print("\n요소 선택 방법:")
    for selector, desc in selectors:
        print(f"  • {selector:25s} - {desc}")

# ============================================
# 6. 요소와 상호작용
# ============================================
def interact_with_elements():
    print("\n" + "=" * 50)
    print("요소와 상호작용")
    print("=" * 50)
    
    print("\n[예제 5] 요소 조작")
    
    """
    # 텍스트 입력
    input_box = driver.find_element(By.ID, 'username')
    input_box.send_keys('my_username')
    
    # 기존 텍스트 지우기
    input_box.clear()
    
    # 엔터키 입력
    input_box.send_keys(Keys.RETURN)
    
    # 버튼 클릭
    button = driver.find_element(By.ID, 'submit')
    button.click()
    
    # 텍스트 가져오기
    element = driver.find_element(By.CLASS_NAME, 'title')
    text = element.text
    
    # 속성 가져오기
    link = driver.find_element(By.TAG_NAME, 'a')
    href = link.get_attribute('href')
    
    # CSS 속성 가져오기
    color = element.value_of_css_property('color')
    
    # 요소가 표시되는지 확인
    is_displayed = element.is_displayed()
    
    # 요소가 활성화되어 있는지 확인
    is_enabled = element.is_enabled()
    
    # 요소가 선택되어 있는지 확인 (체크박스, 라디오)
    is_selected = element.is_selected()
    """
    
    actions = [
        "send_keys(text) - 텍스트 입력",
        "clear() - 입력값 지우기",
        "click() - 클릭",
        "text - 텍스트 가져오기",
        "get_attribute(name) - 속성 가져오기",
        "is_displayed() - 표시 여부 확인",
        "is_enabled() - 활성화 여부 확인",
        "is_selected() - 선택 여부 확인",
    ]
    
    print("\n요소 조작 메서드:")
    for action in actions:
        print(f"  • {action}")

# ============================================
# 7. 대기(Wait) 처리
# ============================================
def handle_waits():
    print("\n" + "=" * 50)
    print("대기(Wait) 처리")
    print("=" * 50)
    
    print("\n[예제 6] 다양한 대기 방법")
    
    """
    1. Implicit Wait (암시적 대기)
    - 요소를 찾을 때까지 지정된 시간 동안 대기
    - 모든 요소 검색에 적용
    
    driver.implicitly_wait(10)  # 최대 10초 대기
    
    2. Explicit Wait (명시적 대기)
    - 특정 조건이 만족될 때까지 대기
    - 더 정확하고 유연함
    
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((By.ID, 'myElement'))
    )
    
    3. Sleep (단순 대기)
    - 무조건 지정된 시간만큼 대기
    - 비효율적이지만 간단함
    
    time.sleep(3)  # 3초 대기
    """
    
    print("\n대기 방법 비교:")
    print("1. Implicit Wait:")
    print("   - 요소를 찾을 때까지 자동 대기")
    print("   - 설정: driver.implicitly_wait(10)")
    
    print("\n2. Explicit Wait (추천):")
    print("   - 특정 조건 충족까지 대기")
    print("   - 더 정확하고 효율적")
    
    print("\n3. Sleep:")
    print("   - 무조건 지정 시간 대기")
    print("   - 비효율적, 테스트용으로만 사용")

# ============================================
# 8. Expected Conditions (예상 조건)
# ============================================
def expected_conditions():
    print("\n" + "=" * 50)
    print("Expected Conditions")
    print("=" * 50)
    
    print("\n[예제 7] 자주 사용하는 조건")
    
    """
    WebDriverWait와 함께 사용하는 조건들:
    
    # 요소가 존재할 때까지
    EC.presence_of_element_located((By.ID, 'element'))
    
    # 요소가 보일 때까지
    EC.visibility_of_element_located((By.ID, 'element'))
    
    # 요소가 클릭 가능할 때까지
    EC.element_to_be_clickable((By.ID, 'button'))
    
    # 제목이 특정 값일 때까지
    EC.title_is('Page Title')
    EC.title_contains('Title')
    
    # URL이 특정 값일 때까지
    EC.url_to_be('https://example.com')
    EC.url_contains('example')
    
    # 요소의 텍스트가 특정 값일 때까지
    EC.text_to_be_present_in_element((By.ID, 'msg'), 'Success')
    
    # alert창이 나타날 때까지
    EC.alert_is_present()
    
    사용 예:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
    element.click()
    """
    
    conditions = [
        "presence_of_element_located - 요소 존재",
        "visibility_of_element_located - 요소 표시",
        "element_to_be_clickable - 클릭 가능",
        "title_is / title_contains - 제목 확인",
        "url_to_be / url_contains - URL 확인",
        "text_to_be_present_in_element - 텍스트 확인",
        "alert_is_present - Alert 확인",
    ]
    
    print("\n주요 Expected Conditions:")
    for cond in conditions:
        print(f"  • {cond}")

# ============================================
# 9. 드롭다운 선택
# ============================================
def select_dropdown():
    print("\n" + "=" * 50)
    print("드롭다운 선택")
    print("=" * 50)
    
    print("\n[예제 8] Select 요소 다루기")
    
    """
    from selenium.webdriver.support.ui import Select
    
    # Select 요소 찾기
    select_element = driver.find_element(By.ID, 'dropdown')
    select = Select(select_element)
    
    # 인덱스로 선택 (0부터 시작)
    select.select_by_index(1)
    
    # value 속성으로 선택
    select.select_by_value('option2')
    
    # 보이는 텍스트로 선택
    select.select_by_visible_text('옵션2')
    
    # 선택된 옵션 가져오기
    selected_option = select.first_selected_option
    print(selected_option.text)
    
    # 모든 옵션 가져오기
    all_options = select.options
    for option in all_options:
        print(option.text)
    
    # 선택 해제 (다중 선택 가능한 경우)
    select.deselect_all()
    """
    
    print("\nSelect 메서드:")
    print("  • select_by_index() - 인덱스로 선택")
    print("  • select_by_value() - value로 선택")
    print("  • select_by_visible_text() - 텍스트로 선택")
    print("  • first_selected_option - 선택된 옵션")
    print("  • options - 모든 옵션")

# ============================================
# 10. 간단한 실습 예제
# ============================================
def simple_example():
    print("\n" + "=" * 50)
    print("간단한 실습 예제")
    print("=" * 50)
    
    print("\n[예제 9] Google 검색 자동화 (의사 코드)")
    
    example_code = """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Chrome 옵션 설정
options = Options()
options.add_argument('--start-maximized')

# 드라이버 생성
driver = webdriver.Chrome(options=options)

try:
    # Google 접속
    driver.get('https://www.google.com')
    
    # 검색창 찾기
    search_box = driver.find_element(By.NAME, 'q')
    
    # 검색어 입력
    search_box.send_keys('Python Selenium')
    
    # 엔터키 입력
    search_box.send_keys(Keys.RETURN)
    
    # 결과 로딩 대기
    time.sleep(2)
    
    # 페이지 제목 출력
    print(f'페이지 제목: {driver.title}')
    
finally:
    # 브라우저 종료
    driver.quit()
"""
    
    print(example_code)

# ============================================
# Main 실행
# ============================================
if __name__ == "__main__":
    setup_chrome_options()
    initialize_driver()
    basic_browser_control()
    find_elements()
    interact_with_elements()
    handle_waits()
    expected_conditions()
    select_dropdown()
    simple_example()
    
    print("\n" + "=" * 50)
    print("  Section 4 완료!")
    print("=" * 50)

"""
실습 문제:

1. Selenium을 사용하여 웹 페이지를 열고 제목과 URL을 출력하는
   프로그램을 작성하세요.

2. 특정 웹사이트의 검색 기능을 자동화하세요:
   - 검색어 입력
   - 검색 버튼 클릭
   - 결과 페이지의 제목 10개 추출

3. 로그인 페이지를 자동화하세요:
   - 아이디/비밀번호 입력
   - 로그인 버튼 클릭
   - 로그인 성공 메시지 확인

4. Explicit Wait를 사용하여 동적으로 로드되는 요소를
   안전하게 찾는 함수를 작성하세요.

5. 드롭다운 메뉴에서 모든 옵션을 순회하며 선택하고
   각 옵션의 텍스트를 출력하는 프로그램을 작성하세요.

주의: 실제 웹사이트 크롤링 시 robots.txt와 이용약관을 확인하세요.
"""

