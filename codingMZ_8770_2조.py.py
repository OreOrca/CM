N = int(input())
K = list(map(int, input().split()))

K.sort(reverse=True)
max_power = 0
for i in range(N):
    current_power = K[i] * (i + 1)
    if current_power > max_power:
        max_power = current_power
        
print(max_power)