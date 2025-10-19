"""
Section 5 - Selenium
====================

주요 내용:
- Selenium 라이브러리를 이용한 동적 웹 페이지 크롤링
- Chrome WebDriver 설정 및 사용
- implicitly_wait()를 이용한 대기 시간 설정
- WebDriverWait와 expected_conditions를 이용한 명시적 대기
- set_window_size()로 브라우저 크기 조절
- get()으로 페이지 이동
- page_source, session_id, title, current_url 확인
- get_cookies()로 쿠키 정보 확인
- find_element_by_css_selector()로 엘리먼트 선택
- send_keys()로 입력
- submit()으로 폼 제출
- save_screenshot()로 스크린샷 저장
- Headless 모드 (chrome_options)
- click()으로 버튼 클릭
- BeautifulSoup과 Selenium 조합
- 페이지 이동 크롤링
- 엑셀(xlsxwriter)로 크롤링 결과 저장
- 이미지 다운로드 및 엑셀 삽입
"""

import time
import urllib.request as req
from io import BytesIO
import xlsxwriter
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# ====================================
# 1. Selenium 기본 사용법
# ====================================

def selenium_basic():
    """Selenium 기본 사용법 및 웹 페이지 접근"""
    # webdriver 설정(Chrome, Firefox 등)
    browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

    # 크롬 브라우저 내부 대기
    browser.implicitly_wait(5)

    # 속성 확인
    print(dir(browser))

    # 브라우저 사이즈
    browser.set_window_size(1920, 1280)  # maximize_window(), minimize_window()

    # 페이지 이동
    browser.get('https://www.daum.net')

    # 페이지 내용
    print('Page Contents : {}'.format(browser.page_source))

    print()

    # 세션 값 출력
    print('Session ID : {}'.format(browser.session_id))

    # 타이틀 출력
    print('Title : {}'.format(browser.title))

    # 현재 URL
    print('URL : {}'.format(browser.current_url))

    # 쿠키 정보 확인
    print('Cookies : {}'.format(browser.get_cookies()))

    # 검색창 input 선택
    element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')

    # 검색어 입력
    element.send_keys('테스트 검색')

    # 검색(Form Submit)
    element.submit()

    # 스크린 샷 저장1
    browser.save_screenshot("c:/website_ch1.png")

    # 스크린 샷 저장2
    browser.get_screenshot_as_file("c:/website_ch2.png")

    # 브라우저 종료
    browser.quit()


# ====================================
# 2. Selenium + BeautifulSoup - 다나와 상품 크롤링
# ====================================

def danawa_crawling():
    """다나와 노트북 상품 정보 크롤링"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # webdriver 설정(Chrome, Firefox 등) - Headless 모드
    browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe', options=chrome_options)

    # webdriver 설정(Chrome, Firefox 등) - 일반 모드
    # browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

    # 크롬 브라우저 내부 대기
    browser.implicitly_wait(5)

    # 브라우저 사이즈
    browser.set_window_size(1920, 1280)  # maximize_window(), minimize_window()

    # 페이지 이동
    browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

    # 1차 페이지 내용
    # print('Before Page Contents : {}'.format(browser.page_source))

    # 제조사별 더 보기 클릭1
    # Explicitly wait
    WebDriverWait(browser, 3) \
        .until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

    # 제조사별 더 보기 클릭2
    # Implicitly wait
    # time.sleep(2)
    # browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

    # 원하는 모델 카테고리 클릭
    WebDriverWait(browser, 2) \
        .until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[14]/label'))).click()

    # 2차 페이지 내용
    # print('After Page Contents : {}'.format(browser.page_source))

    time.sleep(3)

    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # 소스코드 정리
    # print(soup.prettify())

    # 메인 상품 리스트 선택
    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

    # 상품 리스트 확인
    # print(pro_list)

    # 필요 정보 추출
    for v in pro_list:
        # 임시 출력
        # print(v)

        # 불필요한 영역 패스
        if not v.find('div', class_='ad_header'):
            # 태그 정보 출력
            # print('Name : {}, Img : {}, Price : {}'.format(v.select('p.prod_name > a'), v.select('a.thumb_link > img'), v.select('p.price_sect > a')))

            # 상품명, 이미지, 가격
            print(v.select('p.prod_name > a')[0].text.strip())
            print(v.select('a.thumb_link > img')[0]['data-original'])
            print(v.select('p.price_sect > a')[0].text.strip())

        print()

    # 브라우저 종료
    browser.quit()


# ====================================
# 3. 다나와 페이지 이동 크롤링
# ====================================

def danawa_crawling_multiple_pages():
    """다나와 노트북 상품 여러 페이지 크롤링"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # webdriver 설정(Chrome, Firefox 등) - Headless 모드
    browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe', options=chrome_options)

    # webdriver 설정(Chrome, Firefox 등) - 일반 모드
    # browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

    # 크롬 브라우저 내부 대기
    browser.implicitly_wait(5)

    # 브라우저 사이즈
    browser.set_window_size(1920, 1280)  # maximize_window(), minimize_window()

    # 페이지 이동
    browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

    # 1차 페이지 내용
    # print('Before Page Contents : {}'.format(browser.page_source))

    # 제조사별 더 보기 클릭1
    # Explicitly wait
    WebDriverWait(browser, 3) \
        .until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

    # 제조사별 더 보기 클릭2
    # Implicitly wait
    # time.sleep(2)
    # browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

    # 원하는 모델 카테고리 클릭
    WebDriverWait(browser, 2) \
        .until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[14]/label'))).click()

    # 2차 페이지 내용
    # print('After Page Contents : {}'.format(browser.page_source))

    # 3초간 대기
    time.sleep(3)

    # 현재 페이지
    cur_page_num = 1

    # 크롤링 페이지 수
    target_crawl_num = 5

    while cur_page_num <= target_crawl_num:

        # bs4 초기화
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # 소스코드 정리
        # print(soup.prettify())

        # 메인 상품 리스트 선택
        pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

        # 상품 리스트 확인
        # print(pro_list)

        # 페이지 번호 출력
        print('****** Current Page : {}'.format(cur_page_num), ' ******')
        print()

        # 필요 정보 추출(페이지 이동 크롤링)
        for v in pro_list:
            # 임시 출력
            # print(v)

            # 불필요한 영역 패스
            if not v.find('div', class_='ad_header'):
                # 태그 정보 출력
                # print('Name : {}, Img : {}, Price : {}'.format(v.select('p.prod_name > a'), v.select('a.thumb_link > img'), v.select('p.price_sect > a')))

                # 상품명, 이미지, 가격
                print(v.select('p.prod_name > a')[0].text.strip())
                print(v.select('a.thumb_link > img')[0]['data-original'])
                print(v.select('p.price_sect > a')[0].text.strip())

                # 이 부분에서 엑셀 저장(파일, DB 등)
                # CODE
                # CODE

            print()

        print()

        # 페이지 별 스크린 샷 저장
        browser.save_screenshot("c:/target_page{}.png".format(cur_page_num))

        # 페이지 증가
        cur_page_num += 1

        if cur_page_num > target_crawl_num:
            print('Crawling Succeed.')
            break

        # 페이지 이동 클릭
        WebDriverWait(browser, 2) \
            .until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.number_wrap > a:nth-child({})'.format(cur_page_num)))).click()

        # 소스코드 리로드
        # browser.refresh()

        # BeautifulSoup 인스턴스 삭제
        del soup

        # 4초간 대기
        time.sleep(4)

    # 브라우저 종료
    browser.quit()


# ====================================
# 4. 다나와 크롤링 결과를 엑셀로 저장
# ====================================

def danawa_crawling_to_excel():
    """다나와 노트북 상품 크롤링 후 엑셀로 저장"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # webdriver 설정(Chrome, Firefox 등) - Headless 모드
    browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe', options=chrome_options)

    # 엑셀 처리 선언
    workbook = xlsxwriter.Workbook("C:/crawling_result.xlsx")

    # 워크 시트
    worksheet = workbook.add_worksheet()

    # webdriver 설정(Chrome, Firefox 등) - 일반 모드
    # browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

    # 크롬 브라우저 내부 대기
    browser.implicitly_wait(5)

    # 브라우저 사이즈
    browser.set_window_size(1920, 1280)  # maximize_window(), minimize_window()

    # 페이지 이동
    browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

    # 1차 페이지 내용
    # print('Before Page Contents : {}'.format(browser.page_source))

    # 제조사별 더 보기 클릭1
    # Explicitly wait
    WebDriverWait(browser, 3) \
        .until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

    # 제조사별 더 보기 클릭2
    # Implicitly wait
    # time.sleep(2)
    # browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

    # 원하는 모델 카테고리 클릭
    WebDriverWait(browser, 2) \
        .until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[14]/label'))).click()

    # 2차 페이지 내용
    # print('After Page Contents : {}'.format(browser.page_source))

    # 3초간 대기
    time.sleep(3)

    # 현재 페이지
    cur_page_num = 1

    # 크롤링 페이지 수
    target_crawl_num = 5

    # 엑셀 행 수
    ins_cnt = 1

    while cur_page_num <= target_crawl_num:

        # bs4 초기화
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # 소스코드 정리
        # print(soup.prettify())

        # 메인 상품 리스트 선택
        pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

        # 상품 리스트 확인
        # print(pro_list)

        # 페이지 번호 출력
        print('****** Current Page : {}'.format(cur_page_num), ' ******')
        print()

        # 필요 정보 추출(페이지 이동 크롤링)
        for v in pro_list:
            # 임시 출력
            # print(v)

            # 불필요한 영역 패스
            if not v.find('div', class_='ad_header'):
                # 상품명, 이미지, 가격
                prod_name = v.select('p.prod_name > a')[0].text.strip()
                prod_price = v.select('p.price_sect > a')[0].text.strip()

                # 이미지 요청 후 바이트 변환
                img_data = BytesIO(req.urlopen(v.select('a.thumb_link > img')[0]['data-original']).read())

                # 엑셀 저장(텍스트)
                worksheet.write('A%s' % ins_cnt, prod_name)
                worksheet.write('B%s' % ins_cnt, prod_price)

                # 엑셀 저장(이미지)
                worksheet.insert_image('C%s' % ins_cnt, prod_name, {'image_data': img_data})

                # 다음 행 증가
                ins_cnt += 1

            print()

        print()

        # 페이지 별 스크린 샷 저장
        browser.save_screenshot("c:/target_page{}.png".format(cur_page_num))

        # 페이지 증가
        cur_page_num += 1

        if cur_page_num > target_crawl_num:
            print('Crawling Succeed.')
            break

        # 페이지 이동 클릭
        WebDriverWait(browser, 2) \
            .until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.number_wrap > a:nth-child({})'.format(cur_page_num)))).click()

        # 소스코드 리로드
        # browser.refresh()

        # BeautifulSoup 인스턴스 삭제
        del soup

        # 4초간 대기
        time.sleep(4)

    # 브라우저 종료
    browser.quit()

    # 엑셀 파일 닫기
    workbook.close()


# 실행 예제
if __name__ == '__main__':
    # 1. Selenium 기본 사용
    selenium_basic()
    
    # 2. 다나와 크롤링 (단일 페이지)
    danawa_crawling()
    
    # 3. 다나와 크롤링 (여러 페이지)
    danawa_crawling_multiple_pages()
    
    # 4. 다나와 크롤링 (엑셀 저장)
    danawa_crawling_to_excel()

