/*
 * Section 1: C 언어 기초
 * - C 언어 소개
 * - 개발 환경 설정
 * - 첫 프로그램 작성
 * - 기본 자료형과 변수
 * - 입출력 함수
 */

#include <stdio.h>

// ============================================
// 1. Hello World - 첫 프로그램
// ============================================
void hello_world() {
    printf("Hello, World!\n");
    printf("C 언어에 오신 것을 환영합니다!\n");
}

// ============================================
// 2. 변수와 자료형
// ============================================
void variables_and_types() {
    // 정수형
    int age = 25;
    short small_num = 100;
    long big_num = 1000000L;
    
    // 실수형
    float height = 175.5f;
    double weight = 68.5;
    
    // 문자형
    char grade = 'A';
    
    // 출력
    printf("\n=== 변수와 자료형 ===\n");
    printf("나이: %d\n", age);
    printf("작은 수: %d\n", small_num);
    printf("큰 수: %ld\n", big_num);
    printf("키: %.1f cm\n", height);
    printf("몸무게: %.1f kg\n", weight);
    printf("학점: %c\n", grade);
    
    // 자료형 크기 확인
    printf("\n=== 자료형 크기 ===\n");
    printf("int: %lu bytes\n", sizeof(int));
    printf("short: %lu bytes\n", sizeof(short));
    printf("long: %lu bytes\n", sizeof(long));
    printf("float: %lu bytes\n", sizeof(float));
    printf("double: %lu bytes\n", sizeof(double));
    printf("char: %lu bytes\n", sizeof(char));
}

// ============================================
// 3. 상수
// ============================================
void constants() {
    const int MAX_STUDENTS = 30;
    const float PI = 3.14159f;
    
    printf("\n=== 상수 ===\n");
    printf("최대 학생 수: %d\n", MAX_STUDENTS);
    printf("원주율: %.5f\n", PI);
    
    // MAX_STUDENTS = 40;  // 에러! 상수는 변경 불가
}

// ============================================
// 4. 입출력 함수
// ============================================
void input_output() {
    int num;
    float decimal;
    char character;
    
    printf("\n=== 입출력 함수 ===\n");
    
    // 정수 입력
    printf("정수를 입력하세요: ");
    scanf("%d", &num);
    printf("입력한 정수: %d\n", num);
    
    // 실수 입력
    printf("실수를 입력하세요: ");
    scanf("%f", &decimal);
    printf("입력한 실수: %.2f\n", decimal);
    
    // 문자 입력 (버퍼 비우기)
    while(getchar() != '\n');
    printf("문자를 입력하세요: ");
    scanf("%c", &character);
    printf("입력한 문자: %c\n", character);
}

// ============================================
// 5. 형식 지정자
// ============================================
void format_specifiers() {
    int num = 123;
    float f = 45.678f;
    double d = 123.456789;
    char c = 'X';
    
    printf("\n=== 형식 지정자 ===\n");
    printf("정수 (기본): %d\n", num);
    printf("정수 (8자리): %8d\n", num);
    printf("정수 (왼쪽정렬): %-8d|\n", num);
    printf("정수 (0채우기): %08d\n", num);
    
    printf("\n실수 (기본): %f\n", f);
    printf("실수 (소수점 2자리): %.2f\n", f);
    printf("실수 (지수형): %e\n", d);
    
    printf("\n문자: %c\n", c);
    printf("문자열: %s\n", "Hello C!");
}

// ============================================
// Main 함수
// ============================================
int main() {
    printf("====================================\n");
    printf("  C 언어 Section 1: 기초\n");
    printf("====================================\n");
    
    // 각 예제 실행
    hello_world();
    variables_and_types();
    constants();
    format_specifiers();
    
    // 입출력 예제는 사용자 입력이 필요하므로 주석 처리
    // input_output();
    
    printf("\n====================================\n");
    printf("  Section 1 완료!\n");
    printf("====================================\n");
    
    return 0;
}

/*
 * 실습 문제:
 * 
 * 1. 자신의 이름, 나이, 키, 몸무게를 저장하는 변수를 만들고 출력하세요.
 * 2. 원의 반지름을 입력받아 넓이와 둘레를 계산하여 출력하세요.
 *    (넓이 = π × r², 둘레 = 2 × π × r)
 * 3. 섭씨 온도를 입력받아 화씨 온도로 변환하여 출력하세요.
 *    (화씨 = 섭씨 × 9/5 + 32)
 */

