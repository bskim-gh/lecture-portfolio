"""
Section 5: Selenium 실습
- 동적 웹 페이지 크롤링
- 스크롤 처리
- 팝업 및 Alert 처리
- iframe 처리
- JavaScript 실행
- 실전 예제
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

print("=" * 50)
print("  Section 5: Selenium 실습")
print("=" * 50)

# ============================================
# 1. 무한 스크롤 처리
# ============================================
def handle_infinite_scroll():
    print("\n" + "=" * 50)
    print("무한 스크롤 처리")
    print("=" * 50)
    
    print("\n[예제 1] 페이지 스크롤")
    
    """
    # 방법 1: 페이지 끝까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # 방법 2: 특정 픽셀만큼 스크롤
    driver.execute_script("window.scrollBy(0, 1000);")
    
    # 방법 3: 특정 요소까지 스크롤
    element = driver.find_element(By.ID, 'target')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    
    # 무한 스크롤 크롤링 패턴
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        # 페이지 끝까지 스크롤
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # 새 콘텐츠 로딩 대기
        time.sleep(2)
        
        # 새로운 높이 계산
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        # 더 이상 로드할 콘텐츠가 없으면 종료
        if new_height == last_height:
            break
        
        last_height = new_height
    """
    
    scroll_methods = [
        "1. 페이지 끝까지: scrollTo(0, document.body.scrollHeight)",
        "2. 특정 픽셀: scrollBy(0, 1000)",
        "3. 요소까지: scrollIntoView()",
        "4. 무한 스크롤: 높이 비교하며 반복"
    ]
    
    print("\n스크롤 방법:")
    for method in scroll_methods:
        print(f"  • {method}")

# ============================================
# 2. Alert/Confirm/Prompt 처리
# ============================================
def handle_alerts():
    print("\n" + "=" * 50)
    print("Alert/Confirm/Prompt 처리")
    print("=" * 50)
    
    print("\n[예제 2] JavaScript 경고창 처리")
    
    """
    # Alert 대기
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    
    # Alert 전환
    alert = driver.switch_to.alert
    
    # Alert 텍스트 가져오기
    alert_text = alert.text
    print(f'Alert 내용: {alert_text}')
    
    # Alert 확인 (OK 버튼)
    alert.accept()
    
    # Alert 취소 (Cancel 버튼)
    alert.dismiss()
    
    # Prompt에 텍스트 입력
    alert.send_keys('입력할 텍스트')
    alert.accept()
    """
    
    alert_methods = [
        "switch_to.alert - Alert로 전환",
        "alert.text - Alert 텍스트 읽기",
        "alert.accept() - 확인 버튼 클릭",
        "alert.dismiss() - 취소 버튼 클릭",
        "alert.send_keys() - 텍스트 입력 (Prompt)",
    ]
    
    print("\nAlert 처리 메서드:")
    for method in alert_methods:
        print(f"  • {method}")

# ============================================
# 3. iframe 처리
# ============================================
def handle_iframes():
    print("\n" + "=" * 50)
    print("iframe 처리")
    print("=" * 50)
    
    print("\n[예제 3] iframe 내부 요소 접근")
    
    """
    iframe이란?
    - 웹 페이지 내부에 다른 HTML 페이지를 삽입
    - iframe 안의 요소는 직접 접근 불가
    - switch_to로 iframe으로 전환 필요
    
    # 방법 1: iframe 요소로 전환
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    
    # 방법 2: iframe의 id/name으로 전환
    driver.switch_to.frame('iframe_name')
    
    # 방법 3: 인덱스로 전환 (0부터 시작)
    driver.switch_to.frame(0)
    
    # iframe 내부 요소 조작
    element = driver.find_element(By.ID, 'inside_iframe')
    element.click()
    
    # 상위 프레임으로 돌아가기
    driver.switch_to.parent_frame()
    
    # 최상위 프레임으로 돌아가기
    driver.switch_to.default_content()
    """
    
    print("\niframe 전환 방법:")
    print("  1. 요소로 전환: switch_to.frame(iframe_element)")
    print("  2. ID/Name으로: switch_to.frame('iframe_id')")
    print("  3. 인덱스로: switch_to.frame(0)")
    print("\niframe 나가기:")
    print("  • parent_frame() - 부모 프레임으로")
    print("  • default_content() - 최상위로")

# ============================================
# 4. 새 창/탭 처리
# ============================================
def handle_windows():
    print("\n" + "=" * 50)
    print("새 창/탭 처리")
    print("=" * 50)
    
    print("\n[예제 4] 여러 창 관리")
    
    """
    # 현재 창 핸들 저장
    main_window = driver.current_window_handle
    
    # 모든 창 핸들 가져오기
    all_windows = driver.window_handles
    
    # 새 창으로 전환 (마지막 창)
    driver.switch_to.window(all_windows[-1])
    
    # 새 탭 열기
    driver.execute_script("window.open('https://example.com', '_blank');")
    
    # 모든 창 순회
    for window in driver.window_handles:
        driver.switch_to.window(window)
        print(f'현재 창 제목: {driver.title}')
    
    # 메인 창으로 돌아가기
    driver.switch_to.window(main_window)
    
    # 현재 창 닫기
    driver.close()
    
    # 모든 창 닫기
    driver.quit()
    """
    
    window_methods = [
        "current_window_handle - 현재 창 핸들",
        "window_handles - 모든 창 핸들 목록",
        "switch_to.window(handle) - 창 전환",
        "close() - 현재 창 닫기",
        "quit() - 모든 창 닫기",
    ]
    
    print("\n창 관리 메서드:")
    for method in window_methods:
        print(f"  • {method}")

# ============================================
# 5. JavaScript 실행
# ============================================
def execute_javascript():
    print("\n" + "=" * 50)
    print("JavaScript 실행")
    print("=" * 50)
    
    print("\n[예제 5] JavaScript 코드 실행")
    
    """
    # 단순 스크립트 실행
    driver.execute_script("alert('Hello World');")
    
    # 값 반환
    title = driver.execute_script("return document.title;")
    
    # 요소에 JavaScript 적용
    element = driver.find_element(By.ID, 'myElement')
    driver.execute_script("arguments[0].style.border='3px solid red'", element)
    
    # 숨겨진 요소 클릭
    hidden_element = driver.find_element(By.ID, 'hidden')
    driver.execute_script("arguments[0].click();", hidden_element)
    
    # 요소 속성 변경
    driver.execute_script("arguments[0].value='새로운 값';", element)
    
    # 새 요소 생성
    driver.execute_script('''
        var newDiv = document.createElement('div');
        newDiv.innerHTML = 'New Content';
        document.body.appendChild(newDiv);
    ''')
    """
    
    js_examples = [
        "alert() 호출",
        "document 속성 반환",
        "요소 스타일 변경",
        "숨겨진 요소 클릭",
        "요소 속성 변경",
        "DOM 조작"
    ]
    
    print("\nJavaScript 활용 예:")
    for example in js_examples:
        print(f"  • {example}")

# ============================================
# 6. 마우스 액션
# ============================================
def mouse_actions():
    print("\n" + "=" * 50)
    print("마우스 액션")
    print("=" * 50)
    
    print("\n[예제 6] ActionChains 사용")
    
    """
    from selenium.webdriver.common.action_chains import ActionChains
    
    actions = ActionChains(driver)
    
    # 요소로 마우스 이동
    element = driver.find_element(By.ID, 'hover')
    actions.move_to_element(element).perform()
    
    # 클릭
    actions.click(element).perform()
    
    # 더블 클릭
    actions.double_click(element).perform()
    
    # 우클릭
    actions.context_click(element).perform()
    
    # 드래그 앤 드롭
    source = driver.find_element(By.ID, 'source')
    target = driver.find_element(By.ID, 'target')
    actions.drag_and_drop(source, target).perform()
    
    # 연속 액션
    actions.move_to_element(element1)\
           .click()\
           .move_to_element(element2)\
           .click()\
           .perform()
    """
    
    action_methods = [
        "move_to_element() - 마우스 이동",
        "click() - 클릭",
        "double_click() - 더블 클릭",
        "context_click() - 우클릭",
        "drag_and_drop() - 드래그 앤 드롭",
        "perform() - 액션 실행"
    ]
    
    print("\nActionChains 메서드:")
    for method in action_methods:
        print(f"  • {method}")

# ============================================
# 7. 키보드 액션
# ============================================
def keyboard_actions():
    print("\n" + "=" * 50)
    print("키보드 액션")
    print("=" * 50)
    
    print("\n[예제 7] 키보드 조작")
    
    """
    from selenium.webdriver.common.keys import Keys
    
    element = driver.find_element(By.ID, 'input')
    
    # 특수 키 입력
    element.send_keys(Keys.RETURN)      # Enter
    element.send_keys(Keys.TAB)         # Tab
    element.send_keys(Keys.ESCAPE)      # ESC
    element.send_keys(Keys.BACK_SPACE)  # Backspace
    element.send_keys(Keys.DELETE)      # Delete
    element.send_keys(Keys.SPACE)       # Space
    
    # 화살표 키
    element.send_keys(Keys.ARROW_UP)
    element.send_keys(Keys.ARROW_DOWN)
    element.send_keys(Keys.ARROW_LEFT)
    element.send_keys(Keys.ARROW_RIGHT)
    
    # Ctrl 조합키
    element.send_keys(Keys.CONTROL, 'a')  # Ctrl+A (전체 선택)
    element.send_keys(Keys.CONTROL, 'c')  # Ctrl+C (복사)
    element.send_keys(Keys.CONTROL, 'v')  # Ctrl+V (붙여넣기)
    
    # ActionChains로 키 조합
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)\
           .send_keys('a')\
           .key_up(Keys.CONTROL)\
           .perform()
    """
    
    special_keys = [
        "RETURN - Enter",
        "TAB - Tab",
        "ESCAPE - ESC",
        "BACK_SPACE - Backspace",
        "DELETE - Delete",
        "ARROW_UP/DOWN/LEFT/RIGHT - 방향키",
        "CONTROL/SHIFT/ALT - 조합키"
    ]
    
    print("\n특수 키:")
    for key in special_keys:
        print(f"  • Keys.{key}")

# ============================================
# 8. 쿠키 처리
# ============================================
def handle_cookies():
    print("\n" + "=" * 50)
    print("쿠키 처리")
    print("=" * 50)
    
    print("\n[예제 8] 쿠키 관리")
    
    """
    # 모든 쿠키 가져오기
    cookies = driver.get_cookies()
    for cookie in cookies:
        print(cookie)
    
    # 특정 쿠키 가져오기
    session_cookie = driver.get_cookie('session_id')
    
    # 쿠키 추가
    driver.add_cookie({
        'name': 'my_cookie',
        'value': 'cookie_value',
        'path': '/',
        'domain': 'example.com'
    })
    
    # 특정 쿠키 삭제
    driver.delete_cookie('my_cookie')
    
    # 모든 쿠키 삭제
    driver.delete_all_cookies()
    
    # 쿠키로 로그인 상태 유지
    # 1. 로그인 후 쿠키 저장
    import pickle
    cookies = driver.get_cookies()
    pickle.dump(cookies, open('cookies.pkl', 'wb'))
    
    # 2. 다음 실행 시 쿠키 로드
    cookies = pickle.load(open('cookies.pkl', 'rb'))
    for cookie in cookies:
        driver.add_cookie(cookie)
    """
    
    cookie_methods = [
        "get_cookies() - 모든 쿠키",
        "get_cookie(name) - 특정 쿠키",
        "add_cookie(dict) - 쿠키 추가",
        "delete_cookie(name) - 쿠키 삭제",
        "delete_all_cookies() - 전체 삭제"
    ]
    
    print("\n쿠키 관리 메서드:")
    for method in cookie_methods:
        print(f"  • {method}")

# ============================================
# 9. 스크린샷 및 녹화
# ============================================
def capture_screen():
    print("\n" + "=" * 50)
    print("스크린샷 및 녹화")
    print("=" * 50)
    
    print("\n[예제 9] 화면 캡처")
    
    """
    # 전체 페이지 스크린샷
    driver.save_screenshot('screenshot.png')
    
    # 특정 요소만 스크린샷
    element = driver.find_element(By.ID, 'content')
    element.screenshot('element.png')
    
    # 바이트로 스크린샷 가져오기
    screenshot_bytes = driver.get_screenshot_as_png()
    
    from PIL import Image
    from io import BytesIO
    
    image = Image.open(BytesIO(screenshot_bytes))
    image.save('screenshot_pil.png')
    
    # 타임스탬프 포함 파일명
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'screenshot_{timestamp}.png'
    driver.save_screenshot(filename)
    """
    
    capture_methods = [
        "save_screenshot(filename) - 전체 화면",
        "element.screenshot(filename) - 요소만",
        "get_screenshot_as_png() - 바이트로",
    ]
    
    print("\n스크린샷 메서드:")
    for method in capture_methods:
        print(f"  • {method}")

# ============================================
# 10. 실전 종합 예제
# ============================================
def comprehensive_crawler():
    print("\n" + "=" * 50)
    print("실전 종합 예제")
    print("=" * 50)
    
    print("\n[예제 10] 동적 웹 페이지 크롤러 클래스")
    
    example_code = """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json

class DynamicWebCrawler:
    def __init__(self, headless=True):
        self.options = Options()
        if headless:
            self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = None
    
    def start(self):
        \"\"\"드라이버 시작\"\"\"
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.implicitly_wait(10)
    
    def stop(self):
        \"\"\"드라이버 종료\"\"\"
        if self.driver:
            self.driver.quit()
    
    def get_page(self, url):
        \"\"\"페이지 로드\"\"\"
        self.driver.get(url)
        time.sleep(2)
    
    def scroll_to_bottom(self):
        \"\"\"페이지 끝까지 스크롤\"\"\"
        last_height = self.driver.execute_script(
            "return document.body.scrollHeight"
        )
        
        while True:
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(2)
            
            new_height = self.driver.execute_script(
                "return document.body.scrollHeight"
            )
            
            if new_height == last_height:
                break
            last_height = new_height
    
    def wait_and_click(self, by, value):
        \"\"\"요소 대기 후 클릭\"\"\"
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((by, value)))
        element.click()
    
    def extract_items(self, selector):
        \"\"\"아이템 추출\"\"\"
        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return [el.text for el in elements]
    
    def save_to_json(self, data, filename):
        \"\"\"JSON 저장\"\"\"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

# 사용 예
crawler = DynamicWebCrawler(headless=False)
try:
    crawler.start()
    crawler.get_page('https://example.com')
    crawler.scroll_to_bottom()
    items = crawler.extract_items('.item')
    crawler.save_to_json(items, 'result.json')
finally:
    crawler.stop()
"""
    
    print(example_code)

# ============================================
# Main 실행
# ============================================
if __name__ == "__main__":
    handle_infinite_scroll()
    handle_alerts()
    handle_iframes()
    handle_windows()
    execute_javascript()
    mouse_actions()
    keyboard_actions()
    handle_cookies()
    capture_screen()
    comprehensive_crawler()
    
    print("\n" + "=" * 50)
    print("  Section 5 완료!")
    print("=" * 50)

"""
실습 문제:

1. 무한 스크롤 페이지에서 모든 아이템을 수집하는 프로그램을 작성하세요.
   - 스크롤하며 모든 콘텐츠 로드
   - 중복 제거
   - JSON 파일로 저장

2. iframe이 포함된 페이지에서 iframe 내부의 데이터를 추출하세요.
   - iframe으로 전환
   - 데이터 추출
   - 메인 프레임으로 복귀

3. 링크 클릭 시 새 탭이 열리는 경우를 처리하세요:
   - 새 탭으로 전환
   - 데이터 수집
   - 원래 탭으로 복귀

4. JavaScript로 동적 생성되는 요소를 기다렸다가 추출하세요:
   - Explicit Wait 사용
   - 요소가 나타날 때까지 대기
   - 데이터 추출

5. 마우스 호버 시 나타나는 메뉴를 클릭하는 프로그램을 작성하세요:
   - ActionChains 사용
   - 마우스 이동
   - 클릭

주의사항:
- 실제 웹사이트 크롤링 시 이용약관 확인
- 서버에 과부하 주지 않도록 적절한 대기 시간 설정
- robots.txt 준수
"""

