from collections import deque
import sys

n, w, L = map(int, input().split())

weights = deque(map(int, sys.stdin.readline().split()))

# 다리를 표현하는 큐, 초기 상태 0으로
bridge = deque([0] * w)

time = 0
current_weight = 0   # 현재 다리 위 무게 총합

# 모든 트럭이 다리를 건널 때까지
while bridge:
    time += 1

    # 다리를 건넌 트럭의 무게만큼 현재 무게에서 빼줌
    current_weight -= bridge.popleft()

    if weights:
        # 다음 트럭이 다리 위에 올라갈 수 있다면
        if current_weight + weights[0] <= L:
            truck = weights.popleft() # 대기 중인 트럭이 다리로 진입
            bridge.append(truck) # 트럭을 다리에 추가
            current_weight += truck # 다리 위의 무게 업데이트
        else:
            bridge.append(0) # 다리에 올라갈 수 없으면 0을 추가하여 대기 시간을 표현

print(time)