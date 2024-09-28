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