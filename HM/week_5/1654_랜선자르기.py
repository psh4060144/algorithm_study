K, N = map(int, input().split())
wires = [int(input()) for _ in range(K)]
# 최소 길이 : 1 (start)
# 최대 길이 : 가장 긴 랜선 길이 (end)
# N개의 랜선을 만들기 위해 중간 길이를 구해서 wires의 랜선들 나눠보기 >> 이진탐색
# 만약 잘린 랜선 개수가 N보다 작다 >> 길이를 더 줄여보자 >> end = mid - 1
# 만약 잘린 랜선 개수가 N보다 크다 >> 길이를 더 늘려보자 >> start = mid + 1

start = 1
end = max(wires)
result = 0  # 결과값

# start > end가 되면 종료
while start <= end:
    mid = (start + end) // 2
    n = 0  # 잘린 랜선 개수를 측정할 변수
    for wire in wires:
        n += (wire // mid)

    if n < N:
        end = mid - 1
    elif n >= N:    # 문제에서 "N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다."고 했으므로..
        result = mid
        start = mid + 1
print(result)
