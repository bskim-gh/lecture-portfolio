/*
 * Section 5: 배열
 * - 1차원 배열
 * - 배열의 초기화
 * - 배열과 반복문
 * - 다차원 배열
 * - 문자열과 배열
 * - 배열의 활용
 */

#include <stdio.h>
#include <string.h>

// ============================================
// 1. 1차원 배열의 기초
// ============================================
void basic_array() {
    printf("\n=== 1차원 배열 기초 ===\n");
    
    // 배열 선언과 초기화
    int numbers[5] = {10, 20, 30, 40, 50};
    
    // 배열 요소 접근
    printf("배열 요소 출력:\n");
    for (int i = 0; i < 5; i++) {
        printf("numbers[%d] = %d\n", i, numbers[i]);
    }
    
    // 배열 크기 계산
    int size = sizeof(numbers) / sizeof(numbers[0]);
    printf("\n배열의 크기: %d\n", size);
    
    // 배열 요소 수정
    numbers[2] = 100;
    printf("numbers[2]를 100으로 변경\n");
    printf("변경 후: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");
}

// ============================================
// 2. 배열 초기화 방법
// ============================================
void array_initialization() {
    printf("\n=== 배열 초기화 ===\n");
    
    // 방법 1: 모든 요소 지정
    int arr1[5] = {1, 2, 3, 4, 5};
    
    // 방법 2: 일부만 초기화 (나머지는 0)
    int arr2[5] = {1, 2};  // {1, 2, 0, 0, 0}
    
    // 방법 3: 모두 0으로 초기화
    int arr3[5] = {0};
    
    // 방법 4: 크기 자동 결정
    int arr4[] = {10, 20, 30, 40};  // 크기 4
    
    printf("arr1: ");
    for (int i = 0; i < 5; i++) printf("%d ", arr1[i]);
    
    printf("\narr2: ");
    for (int i = 0; i < 5; i++) printf("%d ", arr2[i]);
    
    printf("\narr3: ");
    for (int i = 0; i < 5; i++) printf("%d ", arr3[i]);
    
    printf("\narr4: ");
    int size4 = sizeof(arr4) / sizeof(arr4[0]);
    for (int i = 0; i < size4; i++) printf("%d ", arr4[i]);
    printf("\n");
}

// ============================================
// 3. 배열의 입력과 출력
// ============================================
void array_input_output() {
    printf("\n=== 배열 입출력 ===\n");
    
    int scores[5];
    
    // 시뮬레이션용 데이터
    int simulated_input[] = {85, 90, 78, 92, 88};
    
    printf("5명의 점수 입력 (시뮬레이션):\n");
    for (int i = 0; i < 5; i++) {
        scores[i] = simulated_input[i];
        printf("학생 %d: %d\n", i + 1, scores[i]);
    }
    
    // 합계와 평균 계산
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += scores[i];
    }
    
    float average = sum / 5.0f;
    printf("\n총점: %d\n", sum);
    printf("평균: %.2f\n", average);
}

// ============================================
// 4. 배열 정렬 (버블 정렬)
// ============================================
void bubble_sort() {
    printf("\n=== 버블 정렬 ===\n");
    
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("정렬 전: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // 버블 정렬 알고리즘
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // 교환
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    
    printf("정렬 후: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// ============================================
// 5. 배열 검색 (선형 검색)
// ============================================
void linear_search() {
    printf("\n=== 선형 검색 ===\n");
    
    int arr[] = {10, 23, 45, 70, 11, 15};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 70;
    
    printf("배열: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // 검색
    int found = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            found = i;
            break;
        }
    }
    
    if (found != -1) {
        printf("%d를 인덱스 %d에서 찾았습니다.\n", target, found);
    } else {
        printf("%d를 찾을 수 없습니다.\n", target);
    }
}

// ============================================
// 6. 2차원 배열
// ============================================
void two_dimensional_array() {
    printf("\n=== 2차원 배열 ===\n");
    
    // 2차원 배열 선언 및 초기화
    int matrix[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    
    printf("3x4 행렬:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%3d ", matrix[i][j]);
        }
        printf("\n");
    }
    
    // 각 행의 합 계산
    printf("\n각 행의 합:\n");
    for (int i = 0; i < 3; i++) {
        int row_sum = 0;
        for (int j = 0; j < 4; j++) {
            row_sum += matrix[i][j];
        }
        printf("행 %d: %d\n", i, row_sum);
    }
}

// ============================================
// 7. 행렬 연산
// ============================================
void matrix_operations() {
    printf("\n=== 행렬 연산 ===\n");
    
    int A[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int B[2][3] = {{7, 8, 9}, {10, 11, 12}};
    int C[2][3];  // 결과 행렬
    
    // 행렬 덧셈
    printf("행렬 A:\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%3d ", A[i][j]);
        }
        printf("\n");
    }
    
    printf("\n행렬 B:\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%3d ", B[i][j]);
        }
        printf("\n");
    }
    
    // 덧셈 수행
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
    
    printf("\n행렬 A + B:\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%3d ", C[i][j]);
        }
        printf("\n");
    }
}

// ============================================
// 8. 문자열 배열 (문자 배열)
// ============================================
void string_array() {
    printf("\n=== 문자열 배열 ===\n");
    
    // 문자열 선언 방법
    char str1[] = "Hello";
    char str2[20] = "World";
    char str3[] = {'C', ' ', 'L', 'a', 'n', 'g', '\0'};
    
    printf("str1: %s\n", str1);
    printf("str2: %s\n", str2);
    printf("str3: %s\n", str3);
    
    // 문자열 길이
    printf("\nstr1 길이: %lu\n", strlen(str1));
    
    // 문자열 복사
    char dest[20];
    strcpy(dest, str1);
    printf("복사된 문자열: %s\n", dest);
    
    // 문자열 연결
    strcat(dest, " ");
    strcat(dest, str2);
    printf("연결된 문자열: %s\n", dest);
    
    // 문자열 비교
    if (strcmp(str1, "Hello") == 0) {
        printf("\n문자열이 같습니다.\n");
    }
}

// ============================================
// 9. 문자열 배열 (여러 문자열)
// ============================================
void multiple_strings() {
    printf("\n=== 여러 문자열 저장 ===\n");
    
    char names[5][20] = {
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve"
    };
    
    printf("이름 목록:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d. %s\n", i + 1, names[i]);
    }
}

// ============================================
// 10. 배열 활용 예제
// ============================================
void array_applications() {
    printf("\n=== 배열 활용 예제 ===\n");
    
    // 최대값, 최소값 찾기
    int numbers[] = {45, 23, 78, 12, 90, 34, 67};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    
    int max = numbers[0];
    int min = numbers[0];
    
    for (int i = 1; i < size; i++) {
        if (numbers[i] > max) max = numbers[i];
        if (numbers[i] < min) min = numbers[i];
    }
    
    printf("배열: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");
    printf("최대값: %d\n", max);
    printf("최소값: %d\n", min);
    
    // 배열 역순으로 뒤집기
    printf("\n배열 뒤집기:\n");
    printf("원본: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", numbers[i]);
    }
    
    for (int i = 0; i < size / 2; i++) {
        int temp = numbers[i];
        numbers[i] = numbers[size - 1 - i];
        numbers[size - 1 - i] = temp;
    }
    
    printf("\n뒤집기 후: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");
}

// ============================================
// Main 함수
// ============================================
int main() {
    printf("====================================\n");
    printf("  C 언어 Section 5: 배열\n");
    printf("====================================\n");
    
    basic_array();
    array_initialization();
    array_input_output();
    bubble_sort();
    linear_search();
    two_dimensional_array();
    matrix_operations();
    string_array();
    multiple_strings();
    array_applications();
    
    printf("\n====================================\n");
    printf("  Section 5 완료!\n");
    printf("====================================\n");
    
    return 0;
}

/*
 * 실습 문제:
 * 
 * 1. 10개의 정수를 입력받아 짝수와 홀수를 각각 다른 배열에 저장하는
 *    프로그램을 작성하세요.
 * 
 * 2. 5x5 2차원 배열을 만들고 다음을 수행하세요:
 *    - 1부터 25까지 순서대로 채우기
 *    - 대각선 요소의 합 구하기
 * 
 * 3. 두 개의 정렬된 배열을 하나의 정렬된 배열로 병합하는
 *    프로그램을 작성하세요.
 * 
 * 4. 문자열을 입력받아 역순으로 출력하는 프로그램을 작성하세요.
 *    (string.h 함수 사용하지 않고)
 * 
 * 5. 3x3 행렬의 전치 행렬을 구하는 프로그램을 작성하세요.
 */

