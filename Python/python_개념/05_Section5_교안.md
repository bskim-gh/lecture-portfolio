# Section 5: 머신러닝 기초

## 📚 학습 목표
- Scikit-learn을 사용한 지도학습과 비지도학습 이해
- 회귀, 분류, 군집화 등 기본 알고리즘 학습
- 모델 평가 및 성능 향상 기법 습득

---

## 5-1. Scikit-learn을 사용한 지도학습과 비지도학습

Scikit-learn은 파이썬에서 머신러닝과 데이터 분석을 위한 라이브러리로, 간편하고 효과적인 API를 제공합니다.

### 지도학습 예제: 붓꽃 품종 분류

지도학습은 레이블이 있는 데이터를 사용하여 학습하고, 새로운 입력 데이터의 레이블을 예측하는 머신러닝 방법입니다.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 데이터 로드
iris = load_iris()
X = iris.data
y = iris.target

# 데이터 분할 (Train, Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# K-Nearest Neighbors 분류 모델 생성
knn = KNeighborsClassifier(n_neighbors=3)

# 모델 학습
knn.fit(X_train, y_train)

# 예측
y_pred = knn.predict(X_test)

# 정확도 평가
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

### 비지도학습 예제: 군집화 (K-Means Clustering)

비지도학습은 레이블이 없는 데이터를 사용하여 패턴을 찾거나 데이터를 그룹화하는 머신러닝 방법입니다.

```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 데이터 로드
iris = load_iris()
X = iris.data

# K-Means 군집화 모델 생성
kmeans = KMeans(n_clusters=3, random_state=42)

# 모델 학습
kmeans.fit(X)

# 각 데이터 포인트의 클러스터 할당
labels = kmeans.labels_

# 군집 중심 확인
centers = kmeans.cluster_centers_

# 군집 결과 시각화
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('K-Means Clustering')
plt.show()
```

---

## 5-2. 회귀, 분류, 군집화 등 기본 알고리즘 학습

### 1. 회귀(Regression)

회귀는 연속적인 값(종속 변수)과 그와 관련된 특성(독립 변수) 사이의 관계를 모델링하는 알고리즘입니다.

**예제: 단순 선형 회귀**

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 샘플 데이터 생성
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 3, 4, 5, 6])

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(X, y)

# 예측
X_test = np.array([6, 7, 8]).reshape(-1, 1)
y_pred = model.predict(X_test)

# 결과 시각화
plt.scatter(X, y, label='Actual Data')
plt.plot(X_test, y_pred, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```

### 2. 분류(Classification)

분류는 입력 데이터를 여러 개의 클래스 또는 범주로 분류하는 알고리즘입니다.

**예제: 로지스틱 회귀 (이진 분류)**

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# 샘플 데이터 생성
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# 로지스틱 회귀 모델 생성
model = LogisticRegression()

# 모델 학습
model.fit(X, y)

# 예측
X_test = np.array([3.5, 7.5]).reshape(-1, 1)
y_pred = model.predict(X_test)

# 결과 시각화
plt.scatter(X, y, label='Actual Data')
plt.plot(X_test, y_pred, color='red', marker='o', linestyle='dashed', label='Predicted Class')
plt.xlabel('X')
plt.ylabel('Class (0 or 1)')
plt.legend()
plt.show()
```

### 3. 군집화(Clustering)

군집화는 레이블이 없는 데이터를 비슷한 특성을 가지는 그룹으로 나누는 알고리즘입니다.

**예제: K-Means 군집화**

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 샘플 데이터 생성
X = np.array([[1, 2], [2, 3], [5, 8], [6, 7], [10, 12], [12, 13]])

# K-Means 군집화 모델 생성
kmeans = KMeans(n_clusters=2)

# 모델 학습
kmeans.fit(X)

# 각 데이터 포인트의 클러스터 할당
labels = kmeans.labels_

# 군집 중심 확인
centers = kmeans.cluster_centers_

# 결과 시각화
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', label='Clusters')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
```

---

## 5-3. 모델 평가와 성능 향상

모델 평가와 성능 향상은 머신러닝 모델을 구축하고 결과를 평가하며, 더 좋은 성능을 얻기 위한 과정입니다.

### 1. 모델 평가

**예제: 분류 모델의 평가**

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# 샘플 데이터 로드
iris = load_iris()
X = iris.data
y = iris.target

# 데이터 분할 (Train, Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 로지스틱 회귀 모델 생성
model = LogisticRegression()

# 모델 학습
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 평가 지표 계산
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:")
print(conf_matrix)
```

### 2. 성능 향상: 하이퍼파라미터 튜닝

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 샘플 데이터 로드
iris = load_iris()
X = iris.data
y = iris.target

# 데이터 분할 (Train, Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 랜덤 포레스트 분류 모델 생성
model = RandomForestClassifier()

# 하이퍼파라미터 튜닝을 위한 그리드 서치
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 5, 10, 15],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3)
grid_search.fit(X_train, y_train)

# 최적의 하이퍼파라미터 및 성능 출력
print("Best Parameters:", grid_search.best_params_)
print("Best Accuracy:", grid_search.best_score_)

# 테스트 데이터로 모델 평가
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", accuracy)
```

---

## 📝 정리

Section 5에서는 다음 내용을 다루었습니다:
- Scikit-learn을 사용한 지도학습 (K-Nearest Neighbors 분류)
- 비지도학습 (K-Means 군집화)
- 회귀 (Linear Regression), 분류 (Logistic Regression), 군집화 (K-Means)
- 모델 평가 지표: Accuracy, Precision, Recall, F1 Score, Confusion Matrix
- 하이퍼파라미터 튜닝 (GridSearchCV)

머신러닝의 기본 알고리즘과 평가 방법을 이해하면 다양한 데이터 분석 및 예측 문제를 해결할 수 있습니다.

