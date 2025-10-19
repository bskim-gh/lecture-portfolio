/*
 * Section 4: 함수
 * - 함수의 정의와 호출
 * - 매개변수와 반환값
 * - 함수 프로토타입
 * - 재귀 함수
 * - 변수의 범위 (scope)
 * - 정적 변수
 */

#include <stdio.h>

// ============================================
// 함수 프로토타입 선언
// ============================================
void greet(void);
int add(int a, int b);
int subtract(int a, int b);
int multiply(int a, int b);
float divide(int a, int b);
void print_array(int arr[], int size);
int find_max(int arr[], int size);
int factorial(int n);
int fibonacci(int n);
void print_pattern(int n);

// ============================================
// 1. 함수의 기본 형태
// ============================================
void function_basics() {
    printf("\n=== 함수의 기본 형태 ===\n");
    
    // 반환값과 매개변수가 없는 함수
    greet();
    
    // 매개변수와 반환값이 있는 함수
    int sum = add(10, 20);
    printf("10 + 20 = %d\n", sum);
    
    int diff = subtract(30, 15);
    printf("30 - 15 = %d\n", diff);
}

// 함수 정의
void greet() {
    printf("안녕하세요! C 언어 함수 학습입니다.\n");
}

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

// ============================================
// 2. 사칙연산 함수
// ============================================
void calculator_functions() {
    printf("\n=== 사칙연산 함수 ===\n");
    
    int a = 20, b = 4;
    
    printf("a = %d, b = %d\n", a, b);
    printf("덧셈: %d\n", add(a, b));
    printf("뺄셈: %d\n", subtract(a, b));
    printf("곱셈: %d\n", multiply(a, b));
    printf("나눗셈: %.2f\n", divide(a, b));
}

int multiply(int a, int b) {
    return a * b;
}

float divide(int a, int b) {
    if (b == 0) {
        printf("오류: 0으로 나눌 수 없습니다!\n");
        return 0.0f;
    }
    return (float)a / b;
}

// ============================================
// 3. 배열을 매개변수로 받는 함수
// ============================================
void array_functions() {
    printf("\n=== 배열과 함수 ===\n");
    
    int numbers[] = {5, 2, 8, 1, 9, 3, 7};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    
    printf("배열 출력:\n");
    print_array(numbers, size);
    
    int max = find_max(numbers, size);
    printf("\n최대값: %d\n", max);
}

void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
}

int find_max(int arr[], int size) {
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

// ============================================
// 4. 재귀 함수
// ============================================
void recursive_functions() {
    printf("\n=== 재귀 함수 ===\n");
    
    // 팩토리얼
    printf("팩토리얼:\n");
    for (int i = 1; i <= 5; i++) {
        printf("%d! = %d\n", i, factorial(i));
    }
    
    // 피보나치 수열
    printf("\n피보나치 수열 (처음 10개):\n");
    for (int i = 0; i < 10; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");
}

// 재귀적 팩토리얼
int factorial(int n) {
    if (n <= 1) {
        return 1;  // 기저 조건
    }
    return n * factorial(n - 1);  // 재귀 호출
}

// 재귀적 피보나치
int fibonacci(int n) {
    if (n <= 1) {
        return n;  // 기저 조건
    }
    return fibonacci(n - 1) + fibonacci(n - 2);  // 재귀 호출
}

// ============================================
// 5. 변수의 범위 (Scope)
// ============================================

int global_var = 100;  // 전역 변수

void scope_demo() {
    printf("\n=== 변수의 범위 ===\n");
    
    int local_var = 50;  // 지역 변수
    
    printf("전역 변수: %d\n", global_var);
    printf("지역 변수: %d\n", local_var);
    
    // 블록 내부의 변수
    {
        int block_var = 30;
        printf("블록 변수: %d\n", block_var);
        printf("블록 내에서 전역 변수: %d\n", global_var);
    }
    
    // printf("블록 변수: %d\n", block_var);  // 오류! 범위 밖
    
    modify_global();
}

void modify_global() {
    printf("함수 내에서 전역 변수 수정 전: %d\n", global_var);
    global_var = 200;
    printf("함수 내에서 전역 변수 수정 후: %d\n", global_var);
}

// ============================================
// 6. 정적 변수 (Static Variable)
// ============================================
void static_variable_demo() {
    printf("\n=== 정적 변수 ===\n");
    
    printf("일반 변수 vs 정적 변수:\n");
    for (int i = 0; i < 5; i++) {
        counter();
    }
}

void counter() {
    int normal_count = 0;     // 일반 지역 변수
    static int static_count = 0;  // 정적 변수
    
    normal_count++;
    static_count++;
    
    printf("일반: %d, 정적: %d\n", normal_count, static_count);
}

// ============================================
// 7. 함수 포인터
// ============================================
void function_pointer_demo() {
    printf("\n=== 함수 포인터 ===\n");
    
    // 함수 포인터 선언
    int (*operation)(int, int);
    
    int a = 10, b = 5;
    
    // 덧셈 함수를 가리킴
    operation = add;
    printf("%d + %d = %d\n", a, b, operation(a, b));
    
    // 뺄셈 함수를 가리킴
    operation = subtract;
    printf("%d - %d = %d\n", a, b, operation(a, b));
    
    // 곱셈 함수를 가리킴
    operation = multiply;
    printf("%d * %d = %d\n", a, b, operation(a, b));
}

// ============================================
// 8. 가변 인자 함수 (Advanced)
// ============================================
#include <stdarg.h>

int sum_all(int count, ...) {
    va_list args;
    va_start(args, count);
    
    int sum = 0;
    for (int i = 0; i < count; i++) {
        sum += va_arg(args, int);
    }
    
    va_end(args);
    return sum;
}

void variadic_functions() {
    printf("\n=== 가변 인자 함수 ===\n");
    
    printf("2개의 수의 합: %d\n", sum_all(2, 10, 20));
    printf("4개의 수의 합: %d\n", sum_all(4, 1, 2, 3, 4));
    printf("6개의 수의 합: %d\n", sum_all(6, 5, 10, 15, 20, 25, 30));
}

// ============================================
// 9. 인라인 함수 (C99 이상)
// ============================================
inline int square(int x) {
    return x * x;
}

void inline_functions() {
    printf("\n=== 인라인 함수 ===\n");
    
    printf("5의 제곱: %d\n", square(5));
    printf("10의 제곱: %d\n", square(10));
}

// ============================================
// 10. 재귀를 이용한 패턴 출력
// ============================================
void print_pattern(int n) {
    if (n <= 0) return;
    
    print_pattern(n - 1);  // 재귀 호출
    
    for (int i = 0; i < n; i++) {
        printf("*");
    }
    printf("\n");
}

void recursive_pattern() {
    printf("\n=== 재귀 패턴 ===\n");
    print_pattern(5);
}

// ============================================
// Main 함수
// ============================================
int main() {
    printf("====================================\n");
    printf("  C 언어 Section 4: 함수\n");
    printf("====================================\n");
    
    function_basics();
    calculator_functions();
    array_functions();
    recursive_functions();
    scope_demo();
    static_variable_demo();
    function_pointer_demo();
    variadic_functions();
    inline_functions();
    recursive_pattern();
    
    printf("\n====================================\n");
    printf("  Section 4 완료!\n");
    printf("====================================\n");
    
    return 0;
}

/*
 * 실습 문제:
 * 
 * 1. 두 정수의 최대공약수(GCD)를 구하는 함수를 작성하세요.
 *    (유클리드 호제법 사용)
 * 
 * 2. 배열의 평균을 계산하는 함수를 작성하세요.
 * 
 * 3. 문자열의 길이를 반환하는 함수를 작성하세요.
 *    (string.h의 strlen을 사용하지 않고)
 * 
 * 4. 하노이 탑 문제를 재귀 함수로 해결하는 프로그램을 작성하세요.
 * 
 * 5. 소수 판별 함수를 작성하고, 1부터 100까지의 모든 소수를 출력하세요.
 */

