"""
Ch08 - Python 예외처리와 파일 입출력
====================================

주요 내용:
- 예외처리(Exception Handling)
- try-except 구문
- try-except-finally 구문
- try-except-else 구문
- 파일 입출력(File I/O)
- 텍스트 파일 읽기(open, read, readline)
- 텍스트 파일 쓰기(write)
- 파일 인코딩(UTF8)
- CSV 파일 처리
- Excel 파일 처리(pandas, openpyxl)
- Workbook, Sheet 다루기
"""

# ====================================
# 1. 예외처리 - try ~ except
# ====================================

def exception_basic():
    num1, num2 = 1, 0
    r1 = r2 = r3 = r4 = 0

    try:
        r1 = num1 + num2
        r2 = num1 - num2
        r3 = num1 * num2
        r4 = num1 / num2
    except:
        print('예외 발생...')

    print('r1 :', r1)
    print('r2 :', r2)
    print('r3 :', r3)
    print('r4 :', r4)


# ====================================
# 2. 예외처리 - try ~ except ~ finally
# ====================================

def exception_finally():
    people = ['김유신', '김춘추', '장보고']

    try:
        # 예외가 발생할 가능성이 있는 로직 영역
        for i in range(3):
            print(people[i])

    except:
        # 예외가 발생했을 때 처리할 로직 영역
        print('유효하지 않은 인덱스 사용')

    finally:
        # 예외 발생여부에 관계 없이 마지막에 실행되는 영역
        print('예외처리 완료...')


# ====================================
# 3. 예외처리 - try ~ except ~ else
# ====================================

def exception_else():
    animal = ['사자', '코끼리', '호랑이', '기린']
    result = None

    while True:
        try:
            # 예외가 발생할 가능성이 있는 로직 영역
            print('동물을 선택하세요')
            print('1:사자, 2:코끼리, 3:호랑이, 4:기린, 0: 종료')
            answer = int(input('선택 : '))

            if answer == 0:
                break

            result = animal[answer-1]

        except:
            # 예외가 발생했을 때 처리할 로직 영역
            print('오류: 숫자를 다시 정확히 입력해주세요.')

        else:
            # 예외가 발생하지 않았을 때 처리할 로직 영역
            print("선택한 동물 :", result)

    print('프로그램 종료')


# ====================================
# 4. 파일 읽기 - 단일 라인
# ====================================

def file_read_line():
    file = open('C:/Users/user/Desktop/Sample.txt', 'r', encoding='UTF8')
    line = file.readline()

    print('line :', line)
    file.close()


# ====================================
# 5. 파일 읽기 - 멀티 라인
# ====================================

def file_read_all():
    file = open('C:/Users/user/Desktop/Sample.txt', 'r', encoding='UTF8')

    while True:
        line = file.read()

        if not line:
            break

        print(line)

    file.close()


# ====================================
# 6. 파일 쓰기
# ====================================

def file_write():
    Sample2 = open('C:/Users/user/Desktop/Sample2.txt', 'w', encoding='UTF8')
    Sample2.write('안녕하세요.\n')
    Sample2.write('반갑습니다.\n')
    Sample2.write('감사합니다.')
    Sample2.close()


# ====================================
# 7. 구구단 파일 쓰기
# ====================================

def file_write_gugudan():
    gugudan = open('C:/Users/user/Desktop/gugudan.txt', 'w', encoding='UTF8')

    for i in range(2, 10):
        gugudan.write('\n=========%d단=========\n' % i)
        for j in range(1, 10):
            k = i * j
            gugudan.write('%d X %d = %d\n' % (i, j, k))

    gugudan.close()


# ====================================
# 8. CSV 파일 처리
# ====================================

def csv_read():
    import pandas as pd

    exam = pd.read_csv('C:/Users/user/Desktop/exam.csv')
    print(exam)


# ====================================
# 9. Excel 파일 처리
# ====================================

def excel_read():
    import pandas as pd

    exam = pd.read_excel('C:/Users/user/Desktop/exam.xlsx')
    print(exam)


def excel_write():
    from openpyxl import Workbook

    workbook = Workbook()

    # 현재 sheet 활성화
    sheet = workbook.active

    # 데이터 입력
    sheet['C2'] = '숫자'
    sheet.append([1, 2, 3])
    sheet.append(['김유신', '김춘추', '장보고', '강감찬', '이순신'])
    sheet.cell(5, 5, 'E열 5행 데이터')

    # 파일저장
    workbook.save('C:/Users/user/Desktop/Sample.xlsx')
    workbook.close()

    print('프로그램 종료')


if __name__ == '__main__':
    # 예외처리 예제 실행
    exception_basic()
    exception_finally()
    
    print('Ch08 예외처리와 파일 입출력 학습 완료')
    # 실행 예제: file_write(), file_write_gugudan(), excel_write() 등
