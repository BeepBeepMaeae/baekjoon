def is_possible(channel, broken):
    # 채널 번호를 문자열로 바꾸고, 고장난 버튼이 하나라도 포함되면 False
    for ch in str(channel):
        if int(ch) in broken:
            return False
    return True

n = int(input())
m = int(input())
if m > 0:
    broken = list(map(int, input().split()))
else:
    broken = []

min_press = abs(n - 100)

for num in range(1000000):
    if is_possible(num, broken):
        # 목표까지 + 또는 - 로 이동한 횟수
        press = len(str(num)) + abs(num - n)
        min_press = min(min_press, press)

print(min_press)