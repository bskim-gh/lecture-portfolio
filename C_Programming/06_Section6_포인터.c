/*
 * Section 6: 포인터
 * - 포인터의 개념
 * - 포인터 선언과 사용
 * - 포인터 연산
 * - 포인터와 배열
 * - 포인터와 함수
 * - 다중 포인터
 * - 동적 메모리 할당
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ============================================
// 1. 포인터의 기초
// ============================================
void pointer_basics() {
    printf("\n=== 포인터 기초 ===\n");
    
    int num = 10;
    int *ptr;  // 포인터 선언
    
    ptr = &num;  // num의 주소를 ptr에 저장
    
    printf("변수 num의 값: %d\n", num);
    printf("변수 num의 주소: %p\n", (void*)&num);
    printf("포인터 ptr의 값 (num의 주소): %p\n", (void*)ptr);
    printf("포인터가 가리키는 값 (*ptr): %d\n", *ptr);
    
    // 포인터를 통한 값 변경
    *ptr = 20;
    printf("\n*ptr = 20 실행 후\n");
    printf("변수 num의 값: %d\n", num);
    printf("포인터가 가리키는 값 (*ptr): %d\n", *ptr);
}

// ============================================
// 2. 포인터와 변수
// ============================================
void pointer_and_variables() {
    printf("\n=== 포인터와 변수 ===\n");
    
    int a = 5, b = 10;
    int *p1, *p2;
    
    p1 = &a;
    p2 = &b;
    
    printf("초기 상태:\n");
    printf("a = %d, b = %d\n", a, b);
    printf("*p1 = %d, *p2 = %d\n", *p1, *p2);
    
    // 포인터를 통한 값 교환
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
    
    printf("\n포인터를 통한 교환 후:\n");
    printf("a = %d, b = %d\n", a, b);
    printf("*p1 = %d, *p2 = %d\n", *p1, *p2);
}

// ============================================
// 3. 포인터 연산
// ============================================
void pointer_arithmetic() {
    printf("\n=== 포인터 연산 ===\n");
    
    int arr[] = {10, 20, 30, 40, 50};
    int *ptr = arr;  // 배열의 첫 번째 요소 주소
    
    printf("배열 요소와 주소:\n");
    for (int i = 0; i < 5; i++) {
        printf("arr[%d] = %d, 주소: %p\n", i, arr[i], (void*)&arr[i]);
    }
    
    printf("\n포인터 연산:\n");
    printf("ptr = %p, *ptr = %d\n", (void*)ptr, *ptr);
    
    ptr++;  // 다음 요소로 이동
    printf("ptr++ 후: ptr = %p, *ptr = %d\n", (void*)ptr, *ptr);
    
    ptr += 2;  // 2칸 이동
    printf("ptr += 2 후: ptr = %p, *ptr = %d\n", (void*)ptr, *ptr);
    
    // 배열 순회
    ptr = arr;
    printf("\n포인터로 배열 순회:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", *(ptr + i));
    }
    printf("\n");
}

// ============================================
// 4. 포인터와 배열
// ============================================
void pointer_and_array() {
    printf("\n=== 포인터와 배열 ===\n");
    
    int arr[5] = {1, 2, 3, 4, 5};
    
    printf("배열 접근 방법 비교:\n");
    for (int i = 0; i < 5; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
        printf("*(arr + %d) = %d\n", i, *(arr + i));
        printf("\n");
    }
    
    // 배열 이름은 첫 번째 요소의 주소
    printf("arr = %p\n", (void*)arr);
    printf("&arr[0] = %p\n", (void*)&arr[0]);
}

// ============================================
// 5. 포인터를 이용한 함수 (Call by Reference)
// ============================================
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void pointer_function() {
    printf("\n=== 포인터와 함수 ===\n");
    
    int x = 10, y = 20;
    
    printf("교환 전: x = %d, y = %d\n", x, y);
    swap(&x, &y);
    printf("교환 후: x = %d, y = %d\n", x, y);
}

// ============================================
// 6. 배열을 반환하는 함수 (포인터 사용)
// ============================================
void modify_array(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        arr[i] *= 2;  // 각 요소를 2배로
    }
}

void array_function() {
    printf("\n=== 배열과 함수 (포인터) ===\n");
    
    int numbers[] = {1, 2, 3, 4, 5};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    
    printf("수정 전: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");
    
    modify_array(numbers, size);
    
    printf("수정 후: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");
}

// ============================================
// 7. 포인터 배열
// ============================================
void pointer_array() {
    printf("\n=== 포인터 배열 ===\n");
    
    int a = 10, b = 20, c = 30;
    int *ptr_arr[3];  // 포인터 배열
    
    ptr_arr[0] = &a;
    ptr_arr[1] = &b;
    ptr_arr[2] = &c;
    
    printf("포인터 배열을 통한 접근:\n");
    for (int i = 0; i < 3; i++) {
        printf("*ptr_arr[%d] = %d\n", i, *ptr_arr[i]);
    }
    
    // 문자열 배열 (포인터 배열로)
    char *names[] = {"Alice", "Bob", "Charlie"};
    
    printf("\n이름 목록:\n");
    for (int i = 0; i < 3; i++) {
        printf("%d. %s\n", i + 1, names[i]);
    }
}

// ============================================
// 8. 다중 포인터 (포인터의 포인터)
// ============================================
void double_pointer() {
    printf("\n=== 다중 포인터 ===\n");
    
    int num = 100;
    int *ptr = &num;      // 단일 포인터
    int **dptr = &ptr;    // 이중 포인터
    
    printf("num = %d\n", num);
    printf("*ptr = %d\n", *ptr);
    printf("**dptr = %d\n", **dptr);
    
    printf("\n주소 관계:\n");
    printf("&num = %p\n", (void*)&num);
    printf("ptr = %p\n", (void*)ptr);
    printf("&ptr = %p\n", (void*)&ptr);
    printf("dptr = %p\n", (void*)dptr);
    
    // 이중 포인터를 통한 값 변경
    **dptr = 200;
    printf("\n**dptr = 200 실행 후\n");
    printf("num = %d\n", num);
}

// ============================================
// 9. 동적 메모리 할당 (malloc, free)
// ============================================
void dynamic_memory() {
    printf("\n=== 동적 메모리 할당 ===\n");
    
    int n = 5;
    
    // malloc을 사용한 동적 할당
    int *arr = (int*)malloc(n * sizeof(int));
    
    if (arr == NULL) {
        printf("메모리 할당 실패\n");
        return;
    }
    
    printf("동적 배열에 값 입력:\n");
    for (int i = 0; i < n; i++) {
        arr[i] = (i + 1) * 10;
        printf("arr[%d] = %d\n", i, arr[i]);
    }
    
    // 메모리 해제
    free(arr);
    printf("\n메모리 해제 완료\n");
}

// ============================================
// 10. calloc과 realloc
// ============================================
void calloc_realloc() {
    printf("\n=== calloc과 realloc ===\n");
    
    // calloc: 0으로 초기화된 메모리 할당
    int *arr = (int*)calloc(5, sizeof(int));
    
    printf("calloc으로 할당 (0으로 초기화):\n");
    for (int i = 0; i < 5; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }
    
    // 값 설정
    for (int i = 0; i < 5; i++) {
        arr[i] = i + 1;
    }
    
    printf("\n값 설정 후:\n");
    for (int i = 0; i < 5; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }
    
    // realloc: 메모리 크기 재할당
    arr = (int*)realloc(arr, 10 * sizeof(int));
    
    printf("\nrealloc으로 크기 확장 (5 -> 10):\n");
    
    // 새로운 요소 초기화
    for (int i = 5; i < 10; i++) {
        arr[i] = i + 1;
    }
    
    for (int i = 0; i < 10; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }
    
    free(arr);
}

// ============================================
// 11. 구조체 포인터
// ============================================
struct Student {
    char name[50];
    int age;
    float grade;
};

void structure_pointer() {
    printf("\n=== 구조체 포인터 ===\n");
    
    struct Student s1 = {"홍길동", 20, 4.5};
    struct Student *ptr = &s1;
    
    printf("구조체 접근 방법:\n");
    printf("s1.name = %s\n", s1.name);
    printf("(*ptr).name = %s\n", (*ptr).name);
    printf("ptr->name = %s\n", ptr->name);
    
    printf("\n모든 정보:\n");
    printf("이름: %s\n", ptr->name);
    printf("나이: %d\n", ptr->age);
    printf("학점: %.1f\n", ptr->grade);
}

// ============================================
// 12. 함수 포인터
// ============================================
int add(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }
int multiply(int a, int b) { return a * b; }

void function_pointer() {
    printf("\n=== 함수 포인터 ===\n");
    
    // 함수 포인터 선언
    int (*operation)(int, int);
    
    int x = 10, y = 5;
    
    operation = add;
    printf("%d + %d = %d\n", x, y, operation(x, y));
    
    operation = subtract;
    printf("%d - %d = %d\n", x, y, operation(x, y));
    
    operation = multiply;
    printf("%d * %d = %d\n", x, y, operation(x, y));
}

// ============================================
// Main 함수
// ============================================
int main() {
    printf("====================================\n");
    printf("  C 언어 Section 6: 포인터\n");
    printf("====================================\n");
    
    pointer_basics();
    pointer_and_variables();
    pointer_arithmetic();
    pointer_and_array();
    pointer_function();
    array_function();
    pointer_array();
    double_pointer();
    dynamic_memory();
    calloc_realloc();
    structure_pointer();
    function_pointer();
    
    printf("\n====================================\n");
    printf("  Section 6 완료!\n");
    printf("====================================\n");
    
    return 0;
}

/*
 * 실습 문제:
 * 
 * 1. 두 변수의 값을 포인터를 사용하여 교환하는 함수를 작성하세요.
 * 
 * 2. 동적으로 할당된 배열에 사용자로부터 n개의 정수를 입력받아
 *    평균을 계산하는 프로그램을 작성하세요.
 * 
 * 3. 문자열을 역순으로 만드는 함수를 포인터를 사용하여 작성하세요.
 * 
 * 4. 2차원 배열을 동적으로 할당하고 값을 저장한 후 출력하는
 *    프로그램을 작성하세요.
 * 
 * 5. 함수 포인터 배열을 만들어 계산기 프로그램을 작성하세요.
 */

