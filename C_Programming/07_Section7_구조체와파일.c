/*
 * Section 7: 구조체와 파일 입출력
 * - 구조체의 정의와 사용
 * - 구조체 배열
 * - 구조체 포인터
 * - typedef
 * - 공용체 (Union)
 * - 열거형 (Enum)
 * - 파일 입출력
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// ============================================
// 1. 구조체의 기초
// ============================================
struct Person {
    char name[50];
    int age;
    float height;
};

void structure_basics() {
    printf("\n=== 구조체 기초 ===\n");
    
    // 구조체 변수 선언 및 초기화
    struct Person p1;
    
    strcpy(p1.name, "홍길동");
    p1.age = 25;
    p1.height = 175.5;
    
    printf("이름: %s\n", p1.name);
    printf("나이: %d\n", p1.age);
    printf("키: %.1f cm\n", p1.height);
    
    // 초기화와 동시에 값 할당
    struct Person p2 = {"김철수", 30, 180.0};
    
    printf("\n두 번째 사람:\n");
    printf("이름: %s\n", p2.name);
    printf("나이: %d\n", p2.age);
    printf("키: %.1f cm\n", p2.height);
}

// ============================================
// 2. 구조체 배열
// ============================================
struct Student {
    int id;
    char name[50];
    float score;
};

void structure_array() {
    printf("\n=== 구조체 배열 ===\n");
    
    struct Student students[3] = {
        {1, "김민수", 85.5},
        {2, "이영희", 92.0},
        {3, "박지훈", 78.5}
    };
    
    printf("학생 명단:\n");
    printf("%-5s %-10s %s\n", "학번", "이름", "점수");
    printf("---------------------------\n");
    
    for (int i = 0; i < 3; i++) {
        printf("%-5d %-10s %.1f\n", 
               students[i].id, 
               students[i].name, 
               students[i].score);
    }
    
    // 평균 계산
    float sum = 0;
    for (int i = 0; i < 3; i++) {
        sum += students[i].score;
    }
    printf("\n평균 점수: %.2f\n", sum / 3);
}

// ============================================
// 3. 구조체 포인터
// ============================================
void structure_pointer() {
    printf("\n=== 구조체 포인터 ===\n");
    
    struct Student s = {100, "박철수", 88.5};
    struct Student *ptr = &s;
    
    // 접근 방법
    printf("일반 접근: %s\n", s.name);
    printf("포인터 접근 1: %s\n", (*ptr).name);
    printf("포인터 접근 2: %s\n", ptr->name);
    
    // 포인터를 통한 수정
    ptr->score = 95.0;
    printf("\n점수 수정 후: %.1f\n", s.score);
}

// ============================================
// 4. 구조체와 함수
// ============================================
void print_student(struct Student s) {
    printf("학번: %d, 이름: %s, 점수: %.1f\n", s.id, s.name, s.score);
}

void update_score(struct Student *s, float new_score) {
    s->score = new_score;
}

void structure_function() {
    printf("\n=== 구조체와 함수 ===\n");
    
    struct Student s = {101, "이민호", 80.0};
    
    printf("원본 학생:\n");
    print_student(s);
    
    // 점수 업데이트
    update_score(&s, 90.5);
    
    printf("\n점수 업데이트 후:\n");
    print_student(s);
}

// ============================================
// 5. typedef 사용
// ============================================
typedef struct {
    char title[100];
    char author[50];
    int year;
    float price;
} Book;

void typedef_example() {
    printf("\n=== typedef 사용 ===\n");
    
    Book book1 = {"C 프로그래밍", "김프로", 2023, 25000};
    
    printf("책 정보:\n");
    printf("제목: %s\n", book1.title);
    printf("저자: %s\n", book1.author);
    printf("출판년도: %d\n", book1.year);
    printf("가격: %.0f원\n", book1.price);
}

// ============================================
// 6. 중첩 구조체
// ============================================
typedef struct {
    char street[100];
    char city[50];
    int zipcode;
} Address;

typedef struct {
    char name[50];
    int age;
    Address addr;  // 중첩 구조체
} Employee;

void nested_structure() {
    printf("\n=== 중첩 구조체 ===\n");
    
    Employee emp = {
        "최영수",
        35,
        {"테헤란로 123", "서울", 12345}
    };
    
    printf("직원 정보:\n");
    printf("이름: %s\n", emp.name);
    printf("나이: %d\n", emp.age);
    printf("주소: %s, %s, %d\n", 
           emp.addr.street, 
           emp.addr.city, 
           emp.addr.zipcode);
}

// ============================================
// 7. 공용체 (Union)
// ============================================
union Data {
    int i;
    float f;
    char str[20];
};

void union_example() {
    printf("\n=== 공용체 (Union) ===\n");
    
    union Data data;
    
    printf("공용체 크기: %lu bytes\n", sizeof(data));
    
    data.i = 10;
    printf("data.i = %d\n", data.i);
    
    data.f = 220.5;
    printf("data.f = %.1f\n", data.f);
    printf("data.i = %d (덮어씌워짐)\n", data.i);
    
    strcpy(data.str, "C Programming");
    printf("data.str = %s\n", data.str);
}

// ============================================
// 8. 열거형 (Enum)
// ============================================
enum Weekday {
    MON = 1, TUE, WED, THU, FRI, SAT, SUN
};

enum Status {
    PENDING, APPROVED, REJECTED
};

void enum_example() {
    printf("\n=== 열거형 (Enum) ===\n");
    
    enum Weekday today = WED;
    
    printf("오늘은 ");
    switch(today) {
        case MON: printf("월요일\n"); break;
        case TUE: printf("화요일\n"); break;
        case WED: printf("수요일\n"); break;
        case THU: printf("목요일\n"); break;
        case FRI: printf("금요일\n"); break;
        case SAT: printf("토요일\n"); break;
        case SUN: printf("일요일\n"); break;
    }
    
    enum Status order_status = APPROVED;
    printf("\n주문 상태: ");
    if (order_status == PENDING) {
        printf("대기 중\n");
    } else if (order_status == APPROVED) {
        printf("승인됨\n");
    } else {
        printf("거절됨\n");
    }
}

// ============================================
// 9. 파일 쓰기
// ============================================
void file_write() {
    printf("\n=== 파일 쓰기 ===\n");
    
    FILE *fp = fopen("output.txt", "w");
    
    if (fp == NULL) {
        printf("파일 열기 실패\n");
        return;
    }
    
    fprintf(fp, "C 언어 파일 입출력\n");
    fprintf(fp, "첫 번째 줄\n");
    fprintf(fp, "두 번째 줄\n");
    fprintf(fp, "숫자: %d\n", 100);
    fprintf(fp, "실수: %.2f\n", 3.14);
    
    fclose(fp);
    printf("파일 쓰기 완료: output.txt\n");
}

// ============================================
// 10. 파일 읽기
// ============================================
void file_read() {
    printf("\n=== 파일 읽기 ===\n");
    
    FILE *fp = fopen("output.txt", "r");
    
    if (fp == NULL) {
        printf("파일 열기 실패\n");
        return;
    }
    
    char line[100];
    printf("파일 내용:\n");
    printf("--------------------\n");
    
    while (fgets(line, sizeof(line), fp) != NULL) {
        printf("%s", line);
    }
    
    printf("--------------------\n");
    fclose(fp);
}

// ============================================
// 11. 구조체를 파일에 저장
// ============================================
void structure_file_io() {
    printf("\n=== 구조체 파일 입출력 ===\n");
    
    // 쓰기
    FILE *fp = fopen("students.dat", "wb");
    
    if (fp == NULL) {
        printf("파일 열기 실패\n");
        return;
    }
    
    struct Student students[3] = {
        {1, "김철수", 85.5},
        {2, "이영희", 92.0},
        {3, "박민수", 78.5}
    };
    
    fwrite(students, sizeof(struct Student), 3, fp);
    fclose(fp);
    printf("구조체 데이터 저장 완료\n");
    
    // 읽기
    fp = fopen("students.dat", "rb");
    
    if (fp == NULL) {
        printf("파일 열기 실패\n");
        return;
    }
    
    struct Student read_students[3];
    fread(read_students, sizeof(struct Student), 3, fp);
    fclose(fp);
    
    printf("\n읽어온 학생 데이터:\n");
    printf("%-5s %-10s %s\n", "학번", "이름", "점수");
    printf("---------------------------\n");
    
    for (int i = 0; i < 3; i++) {
        printf("%-5d %-10s %.1f\n", 
               read_students[i].id, 
               read_students[i].name, 
               read_students[i].score);
    }
}

// ============================================
// 12. 파일 추가 모드
// ============================================
void file_append() {
    printf("\n=== 파일 추가 모드 ===\n");
    
    FILE *fp = fopen("output.txt", "a");
    
    if (fp == NULL) {
        printf("파일 열기 실패\n");
        return;
    }
    
    fprintf(fp, "\n--- 추가된 내용 ---\n");
    fprintf(fp, "세 번째 줄 (추가)\n");
    fprintf(fp, "네 번째 줄 (추가)\n");
    
    fclose(fp);
    printf("파일에 내용 추가 완료\n");
}

// ============================================
// 13. 텍스트 파일 복사
// ============================================
void file_copy() {
    printf("\n=== 파일 복사 ===\n");
    
    FILE *source = fopen("output.txt", "r");
    FILE *dest = fopen("output_copy.txt", "w");
    
    if (source == NULL || dest == NULL) {
        printf("파일 열기 실패\n");
        return;
    }
    
    char ch;
    while ((ch = fgetc(source)) != EOF) {
        fputc(ch, dest);
    }
    
    fclose(source);
    fclose(dest);
    
    printf("파일 복사 완료: output_copy.txt\n");
}

// ============================================
// Main 함수
// ============================================
int main() {
    printf("====================================\n");
    printf("  C 언어 Section 7: 구조체와 파일\n");
    printf("====================================\n");
    
    structure_basics();
    structure_array();
    structure_pointer();
    structure_function();
    typedef_example();
    nested_structure();
    union_example();
    enum_example();
    
    // 파일 입출력
    file_write();
    file_read();
    file_append();
    file_read();  // 추가된 내용 확인
    structure_file_io();
    file_copy();
    
    printf("\n====================================\n");
    printf("  Section 7 완료!\n");
    printf("====================================\n");
    
    return 0;
}

/*
 * 실습 문제:
 * 
 * 1. 도서 관리 프로그램을 만드세요:
 *    - 도서 정보 구조체 (제목, 저자, ISBN, 가격)
 *    - 도서 추가, 조회, 삭제 기능
 *    - 파일로 저장 및 불러오기
 * 
 * 2. 학생 성적 관리 프로그램을 만드세요:
 *    - 학생 구조체 (이름, 학번, 과목별 점수)
 *    - 평균 계산, 석차 정렬
 *    - CSV 형식으로 파일 저장
 * 
 * 3. 간단한 주소록 프로그램을 만드세요:
 *    - 연락처 구조체 (이름, 전화번호, 이메일, 주소)
 *    - 검색, 추가, 수정, 삭제 기능
 *    - 파일로 저장 및 불러오기
 */

