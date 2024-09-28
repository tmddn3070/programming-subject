import cmath # china math

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
