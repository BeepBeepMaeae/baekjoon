a, b, c, d, e, f = map(int, input().split())

# det = a*e - b*d
# [a, b], [d, e] 행렬식
det = a*e - b*d

# 크래머의 공식
x = (c*e - b*f) / det
y = (a*f - c*d) / det

print(int(x), int(y))