# Section 4: 데이터 분석 기초

## 📚 학습 목표
- NumPy와 Pandas의 기본 개념과 활용 이해
- 데이터 전처리 및 정제 기법 학습
- Matplotlib와 Seaborn을 활용한 데이터 시각화

---

## 4-1. NumPy와 Pandas 소개

### NumPy (Numerical Python)

NumPy는 파이썬에서 수치 계산을 위한 핵심 라이브러리로, 고성능의 다차원 배열과 행렬 연산을 지원합니다.

**NumPy의 주요 특징:**
- **다차원 배열 (ndarray):** 고성능의 다차원 배열을 제공하며, 효율적인 연산과 데이터 저장을 가능하게 합니다
- **브로드캐스팅 (Broadcasting):** 다양한 크기의 배열을 산술 연산할 때, 배열의 크기를 자동으로 맞춰주어 편리하게 연산
- **벡터화 (Vectorization):** 반복문 없이 배열 연산을 할 수 있어 코드의 간결성과 성능 향상
- 선형대수, 통계, 난수 발생 등 다양한 기능 제공

**NumPy 예제: 배열 생성과 연산**

```python
import numpy as np

# 1차원 NumPy 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])

# 2차원 NumPy 배열 생성
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 브로드캐스팅을 이용한 배열 연산
result = arr2 * 2

print("1차원 배열:")
print(arr1)
print("\n2차원 배열:")
print(arr2)
print("\n연산 결과:")
print(result)
```

### Pandas

Pandas는 데이터 분석과 조작을 위한 파이썬 라이브러리로, 구조화된 데이터를 효과적으로 처리하고 분석하는 도구를 제공합니다.

**Pandas의 주요 특징:**
- **Series:** 1차원 데이터를 처리하는 자료구조로, 인덱스와 값으로 이루어져 있습니다
- **DataFrame:** 2차원 데이터를 처리하는 자료구조로, 행과 열로 이루어진 테이블 형태의 데이터를 다룸
- 데이터 정렬, 필터링, 통계, 그룹화, 피봇 등 다양한 데이터 조작 기능 제공
- 결측치 처리, 데이터 합치기, 파일 입출력 등 데이터 처리에 유용한 기능 포함
- NumPy와 함께 사용하여 데이터를 효율적으로 분석 및 가공

**Pandas 예제: DataFrame 생성과 조작**

```python
import pandas as pd

# DataFrame 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 28],
    'Position': ['Manager', 'Engineer', 'Designer']
}

df = pd.DataFrame(data)

# 데이터 프레임 정보 출력
print("DataFrame:")
print(df)

# 필터링 및 정렬
engineers = df[df['Position'] == 'Engineer']
sorted_df = df.sort_values(by='Age', ascending=False)

print("\nEngineers:")
print(engineers)
print("\nSorted DataFrame:")
print(sorted_df)
```

---

## 4-2. 데이터 전처리와 정제

데이터 전처리와 정제는 데이터 분석 및 머신러닝 모델 구축에 앞서 데이터를 사전에 처리하여 데이터의 품질을 높이고 분석에 적합한 형태로 가공하는 작업입니다.

### 데이터 전처리 예제: 결측치 처리

```python
import pandas as pd

# 샘플 데이터 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [30, 25, None, 28, 35],
    'Salary': [50000, 45000, 60000, None, 55000]
}

df = pd.DataFrame(data)

# 결측치 확인
print("DataFrame with Missing Values:")
print(df)

# 결측치 처리: 평균 값으로 대체
mean_age = df['Age'].mean()
mean_salary = df['Salary'].mean()

df['Age'].fillna(mean_age, inplace=True)
df['Salary'].fillna(mean_salary, inplace=True)

print("\nDataFrame after Handling Missing Values:")
print(df)
```

### 데이터 정제 예제: 중복 데이터 처리

```python
import pandas as pd

# 샘플 데이터 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Bob', 'Eva'],
    'Age': [30, 25, 28, 25, 35],
    'Salary': [50000, 45000, 60000, 45000, 55000]
}

df = pd.DataFrame(data)

# 중복 데이터 확인
print("DataFrame with Duplicates:")
print(df)

# 중복 데이터 처리: 중복 제거
df.drop_duplicates(inplace=True)

print("\nDataFrame after Removing Duplicates:")
print(df)
```

---

## 4-3. 데이터 시각화(Matplotlib, Seaborn)

데이터 시각화는 데이터를 시각적으로 표현하여 데이터의 패턴과 관계를 쉽게 파악할 수 있도록 도와주는 중요한 작업입니다.

### Matplotlib 예제: 선 그래프 그리기

```python
import matplotlib.pyplot as plt

# 데이터 생성
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 20, 12]

# 선 그래프 그리기
plt.plot(x, y, marker='o', color='b', linestyle='--')

# 그래프 제목과 축 라벨 설정
plt.title('Line Chart Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 그래프 표시
plt.show()
```

### Seaborn 예제: 산점도 그래프 그리기

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 샘플 데이터 생성
data = {
    'Height': [165, 170, 155, 180, 160],
    'Weight': [55, 60, 50, 70, 45],
    'Gender': ['F', 'M', 'F', 'M', 'F']
}

df = pd.DataFrame(data)

# 산점도 그래프 그리기
sns.scatterplot(data=df, x='Height', y='Weight', hue='Gender', style='Gender')

# 그래프 제목 설정
plt.title('Scatter Plot Example')

# 그래프 표시
plt.show()
```

---

## 📝 정리

Section 4에서는 다음 내용을 다루었습니다:
- NumPy의 ndarray, 브로드캐스팅, 벡터화 개념
- Pandas의 Series, DataFrame 생성 및 조작
- 데이터 전처리: 결측치 처리 (fillna)
- 데이터 정제: 중복 데이터 제거 (drop_duplicates)
- Matplotlib를 활용한 선 그래프
- Seaborn을 활용한 산점도 그래프

NumPy와 Pandas는 데이터 분석의 핵심 도구이며, 시각화를 통해 데이터의 패턴과 인사이트를 얻을 수 있습니다.

