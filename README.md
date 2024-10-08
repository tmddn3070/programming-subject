# 문제 1
## 문제 
선린인터넷고등학교의 최고 기만자인 은교는 매일매일 열심히 기만질을 실천하고 있다. 하지만 은교의 기만질로 인해 기분이 상한 은수는 은교를 특검해 기만질을 막아야겠다 생각하였다. 그래서 특검하기 위해 은교가 보내는 메시지를 도청하여 고발하려고 한다. 하지만 기만자 은교는 이 음모를 고발로 이미 알아채고 은수가 도청을 하지 못하게 주파수를 모두 다르게 만들어서 손쉽게 도청하지 못하게 하였다. 이때 은수가 기만자 은교를 특검하기 위해 주파수 신호를 출력하자.

## 입력
첫 번째 줄에 신호의 길이 N이 주어진다. N은 항상 2의 거듭제곱 형태로 주어진다. (예: 2, 4, 8, 16, 32, ...) ( 1 ≤ N ≤ 2^20 )
두 번째 줄에 길이 N의 정수 배열이 주어진다. 이 배열은 시간 도메인에서 측정된 신호의 값을 나타낸다. 

## 출력
주파수 도메인에서의 복소수 성분을 차례로 출력하라.
각 주파수 성분은 실수부와 허수부로 나뉘며, 각 성분은 공백으로 구분한다.
소수점 이하 2자리까지 출력해야 한다

## 예제 입력
```
8
1 2 3 4 5 6 7 8
```

## 예제 출력
```
36.00 0.00
-4.00 9.66
-4.00 4.00
-4.00 1.66
-4.00 0.00
-4.00 -1.66
-4.00 -4.00
-4.00 -9.66
```

## 풀이
이 문제는 은수가 은교를 특검하기 위해 주파수 신호를 출력하는 문제이다. 주어진 신호를 푸리에 변환을 통해 주파수 도메인으로 변환하여 출력하면 된다.
푸리에 변환을 하기 위해서는 주어진 신호를 복소수로 변환해야 한다. 주어진 신호를 복소수로 변환하기 위해서는 주어진 신호의 길이 N만큼 복소수 배열을 만들어주고, 주어진 신호의 값을 복소수 배열에 넣어주면 된다.

이때 푸리에 변환의 식은 다음과 같다.
```math
X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-2\pi i \frac{k n}{N}}
```
이때 $x[n]$은 주어진 신호의 n번째 값이고, $X[k]$는 주파수 도메인에서의 $k$번째 성분이다. 이를 증명하면,
복소 지수 함수는 오일러의 공식에 의해 다음과 같이 표현된다:
$e^{ix} = \cos(x) + i \cdot \sin(x)$ \
따라서 푸리에 변환의 기본 식에서 지수 부분을 확장하면:
```math
X[k] = \sum_{n=0}^{N-1} x[n] \cdot \left( \cos\left( -2\pi \frac{k n}{N} \right) + i \cdot \sin\left( -2\pi \frac{k n}{N} \right) \right)
```

이 식을 실수 부분과 허수 부분으로 나누어 보면:
```math
X[k] = \sum_{n=0}^{N-1} \left( x[n] \cdot \cos\left( -2\pi \frac{k n}{N} \right) \right) + i \cdot \sum_{n=0}^{N-1} \left( x[n] \cdot \sin\left( -2\pi \frac{k n}{N} \right) \right)
```

이때 $\cos(-x) = \cos(x)$이고, $\sin(-x) = -\sin(x)$이므로, 각 항을 정리하면 다음과 같은 식을 얻을 수 있다. 
```math
X[k] = \sum_{n=0}^{N-1} x[n] \cdot \cos\left( 2\pi \frac{k n}{N} \right) - i \cdot \sum_{n=0}^{N-1} x[n] \cdot \sin\left( 2\pi \frac{k n}{N} \right)
```
즉, $X[k]$는 실수부와 허수부로 나뉘어 표현될 수 있다:
- 실수부: $\sum_{n=0}^{N-1} x[n] \cdot \cos\left( 2\pi \frac{k n}{N} \right)$ 

- 허수부: $-\sum_{n=0}^{N-1} x[n] \cdot \sin\left( 2\pi \frac{k n}{N} \right)$

위 식을 통해 $X[k]$는 시간 도메인의 신호 $x[n]$의 각 성분을 주파수 도메인에서 대응되는 주파수 성분으로 변환한 것이다. 각 주파수 성분 $k$에 대해 시간 도메인 신호의 각 성분 $n$에 복소 지수 함수 값을 곱한 후, 이를 모두 합산함으로써 주파수 도메인에서의 $k$번째 성분을 구할 수 있다.

이 변환의 결과는 시간 도메인 신호가 주파수 도메인에서 어떻게 분포되어 있는지를 나타내며, 이는 각 주파수 성분의 크기와 위상 정보를 포함한다.


이를 코드로 구현하면 다음과 같다.
```python
import cmath 

def fft(a):
    n = len(a)
    if n <= 1:
        return a
    even = fft(a[0::2])
    odd = fft(a[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + T[k] for k in range(n // 2)] + [even[k] - T[k] for k in range(n // 2)]

n = int(input())
a = list(map(int, input().split()))

result = fft([complex(val, 0) for val in a])

for c in result:
    print(f"{c.real:.2f} {c.imag:.2f}")
```

## 시간 복잡도
푸리에 변환을 위해 재귀적으로 호출하며, 각 단계에서 n/2개의 원소를 처리하므로, 시간 복잡도는 O(nlogn)이다.

# 문제 2
## 문제
승엽이는 프로그래밍 시간에 매일매일 잔 나머지, 이후 웹프로그래밍 시간에 수행평가를 보았는데 안타깝게도 AND와 OR을 구별할 줄 몰라서 수행평가에서 0점을 받을 위기에 처했다. 이때 두 개의 1(True) 또는 0(False)을 입력했을 때 이것이 AND를 충족하는지, OR을 충족하는지, 아무것도 충족하지 못하는지 구별하는 프로그램을 만들어주자.

## 입력
첫 번째 줄에 테스트 케이스의 개수 N이 주어진다. (1 ≤ N ≤ 100) \
다음 N개의 줄에 각각 2개의 정수 A와 B가 주어진다. (0 ≤ A, B ≤ 1) A와 B는 각각 0(거짓) 또는 1(참)만 가질 수 있다.

## 출력
각 테스트 케이스에 대해 다음과 같이 출력한다. (복수의 조건이 만족될수 있다) \
• AND 조건을 만족하는 경우 "AND"를 출력한다. \
• OR 조건을 만족하는 경우 "OR"을 출력한다. \
• 두 조건이 모두 만족하지 않으면 "NONE"을 출력한다. \
• 이때 복수의 조건이 만족될 경우, 출력되는 조건의 순서는 AND -> OR -> NONE 순이다

## 예제 입력
```
3
1 1
1 0
0 0
```

## 예제 출력
```
AND OR 
OR 
NONE
```

## 풀이
이 문제는 두 개의 1(True) 또는 0(False)을 입력했을 때 이것이 AND를 충족하는지, OR을 충족하는지, 아무것도 충족하지 못하는지 구별하는 문제이다. 이를 구현하기 위해서는 각 조건을 만족하는지 확인하면 된다.

AND 조건을 만족하는지 확인하기 위해서는 두 값이 모두 1인지 확인하면 된다. 이때 두 값이 모두 1이면 AND 조건을 만족하므로 "AND"를 출력한다.

OR 조건을 만족하는지 확인하기 위해서는 두 값 중 하나라도 1인지 확인하면 된다. 이때 두 값 중 하나라도 1이면 OR 조건을 만족하므로 "OR"를 출력한다.

이 두 조건을 만족하지 않는 경우는 두 값이 모두 0인 경우이다. 이때는 아무 조건도 만족하지 않으므로 "NONE"을 출력한다.

이를 코드로 구현하면 다음과 같다.
```python
N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    if A == 1 and B == 1:
        print("AND ", end="")
    if A == 1 or B == 1:
        print("OR", end="")
    if not (A == 1 and B == 1) and not (A == 1 or B == 1):
        print("NONE", end="")
    print()
```

## 시간 복잡도
이 코드의 시간 복잡도는 O(N)이다.